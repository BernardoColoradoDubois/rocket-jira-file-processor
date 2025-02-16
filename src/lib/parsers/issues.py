import json
def issue_parser(data:dict)->dict:
  
  if 'assignee' not in data['_airbyte_data']['fields'].keys():
    data['_airbyte_data']['fields']['assignee'] = {}
  
  if 'priority' not in data['_airbyte_data']['fields'].keys():
    data['_airbyte_data']['fields']['priority'] = {}
  
  dict_data = {
    
      #tarea
      'issue_id': data['_airbyte_data']['id'],
      'issue_key': data['_airbyte_data']['key'],
      
      #proyecto
      'project_id': data['_airbyte_data']['fields']['project']['id'],
      'project_key': data['_airbyte_data']['fields']['project']['key'],
      
      #usuario que crea la tarea
      'creator_account_id': data['_airbyte_data']['fields']['creator']['accountId'],
      'creator_display_name': data['_airbyte_data']['fields']['creator']['displayName'],
      
      #usuario asignado a la tarea
      'assignee_account_id': data['_airbyte_data']['fields']['assignee'].get('accountId', None),  
      'assignee_display_name': data['_airbyte_data']['fields']['assignee'].get('displayName', None),
      
      #usuario que reporta la tarea
      'reporter_account_id': data['_airbyte_data']['fields']['reporter']['accountId'],
      'reporter_display_name': data['_airbyte_data']['fields']['reporter']['displayName'],

      #textos
      'summary': data['_airbyte_data']['fields']['summary'],
      'description': json.dumps(data['_airbyte_data']['fields'].get('description', {})), 
      
      #prioridades
      'priority_id': data['_airbyte_data']['fields']['priority'].get('id',None),
      'priority_name': data['_airbyte_data']['fields']['priority'].get('name',None),
      
      #estados
      'status_id': data['_airbyte_data']['fields']['status']['id'],
      'status_name': data['_airbyte_data']['fields']['status']['name'],
      
      #tiempos
      'time_estimate': data['_airbyte_data']['fields'].get('timeestimate',0),
      'duedate' : data['_airbyte_data']['fields'].get('duedate', None),
      'resolution_date': data['_airbyte_data']['fields'].get('resolutiondate', None),

      #fechas de creacion y actualizacion
      'created_date': data['_airbyte_data']['fields']['created'],
      'updated_date': data['_airbyte_data']['fields']['updated'],
  }

  #formateamos fecha de vencimiento
  if dict_data['duedate'] is not None:
    dict_data['duedate']=dict_data['duedate']+'T18:00:00.000-0600'
  
  return dict_data
