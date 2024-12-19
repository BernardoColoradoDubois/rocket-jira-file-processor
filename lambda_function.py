import json
from src.lib.process import ProcessBus
from src.jira.issues import IssuesHandler,Issues
from src.jira.projects import ProjectsHandler,Projects
from src.jira.users import UsersHandler,Users

def lambda_handler(event, context):
  
  bus = ProcessBus()
  bus.subscribe( IssuesHandler() )
  bus.subscribe( ProjectsHandler() )
  bus.subscribe( UsersHandler() )
          
  for record in event['Records']: 

    # obtenemos nombre del bucket
    bucket_name = record['s3']['bucket']['name'] 
    
    # obtenemos nombre del archivo
    file_key = record['s3']['object']['key'] 
    
    
