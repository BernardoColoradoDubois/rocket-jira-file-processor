import json
import pandas as pd
import boto3
from src.lib.process import Process, ProcessHandler
from src.lib.parsers.users import users_parser
from src.lib.connections.postgres import PostgresConnection


class Users(Process):
  _name = 'users'


class UsersHandler(ProcessHandler):
  _name = 'users'
  
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
    
    # Inicializa la lista de usuarios
    table = []
    
    # Itera sobre las líneas del archivo
    for line in obj['Body'].read().decode('utf-8').splitlines():
        
      data = json.loads(line)
      parsed_data = users_parser(data)
      table.append(parsed_data)
      
    df = pd.DataFrame.from_dict(table)
    
    self.postgres_connection.load_df(table_schema='rocket',table_name='jira_users',df=df)