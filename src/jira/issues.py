import json
import pandas as pd
import boto3
from src.lib.process import Process, ProcessHandler
from src.lib.parsers.issues import issue_parser
from src.lib.connections.postgres import PostgresConnection



class Issues(Process):
  _name = 'issues'


class IssuesHandler(ProcessHandler):
  _name = 'issues'
  
  def __init__(self,s3_client,postgres_connection:PostgresConnection):
    self.s3 = s3_client
    self.postgres_connection = postgres_connection
  
  def execute(self,process:Process)->None:
    # Configura el cliente de S3
    s3 = boto3.client('s3')

    # Reemplaza con el nombre de tu bucket y la clave del objeto
    bucket_name = process.get_bucket_name()
    file_key = process.get_file_key()

    # Obtén el objeto
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    
    table = []
    
    # Itera sobre las líneas del archivo
    for line in obj['Body'].read().decode('utf-8').splitlines():
        
      data = json.loads(line)
      parsed_data = issue_parser(data)
      table.append(parsed_data)
      
    df = pd.DataFrame.from_dict(table)
    
    self.postgres_connection.load_df(table_schema='rocket',table_name='stg_jira_issues',df=df)
    
    self.postgres_connection.execute_sql_command(sql="""
      drop table if exists rocket.jira_priorities;
      drop table if exists rocket.jira_priorities;
      create table if not exists rocket.jira_priorities as 
      select 
	      priority_id, 
	      priority_name 
      from rocket.stg_jira_issues;      
      """)
    
    self.postgres_connection.execute_sql_command(sql="""
      drop table if exists rocket.jira_statuses; 
      create table if not exists rocket.jira_statuses as 
        select 
	      status_id , 
	      status_name  
      from rocket.stg_jira_issues;                                         
    """)
    
    self.postgres_connection.execute_sql_command(sql="""
      DROP TABLE IF EXISTS rocket.jira_issues; 
      CREATE TABLE IF NOT EXISTS rocket.jira_issues AS 
      SELECT 
        issue_id, 
        issue_key, 
        project_id, 
        project_key, 
        creator_account_id, 
        assignee_account_id, 
        reporter_account_id, 
        summary, 
        description, 
        priority_id, 
        status_id, 
        time_estimate, 
        duedate, 
        resolution_date,  
        created_date,  
        updated_date 
      FROM rocket.stg_jira_issues; 
    """)
    
