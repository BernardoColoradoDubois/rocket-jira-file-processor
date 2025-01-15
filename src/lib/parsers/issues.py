

def issue_parser(data:dict)->dict:
  
  
  
  return {
      'issue_id': data['_airbyte_data']['id'],
      'issue_key': data['_airbyte_data']['key'],
      'project_key': data['_airbyte_data']['fields']['project']['key'],
      'created_date': data['_airbyte_data']['fields']['created'],
      'updated_date': data['_airbyte_data']['fields']['updated'],
      'summary': data['_airbyte_data']['fields']['summary'],
      'description': data['_airbyte_data']['fields'].get('description', ''),  # Manejar descripciones vacías
      'assignee_account_id': data['_airbyte_data']['fields']['assignee'].get('accountId', None),  # Manejar asignados nulos
      'assignee_display_name': data['_airbyte_data']['fields']['assignee'].get('displayName', None),
      'status_name': data['_airbyte_data']['fields']['status']['name'],
      'priority_name': data['_airbyte_data']['fields']['priority']['name'],
      'reporter_account_id': data['_airbyte_data']['fields']['reporter']['accountId'],
      'reporter_display_name': data['_airbyte_data']['fields']['reporter']['displayName'],
      'creator_account_id': data['_airbyte_data']['fields']['creator']['accountId'],
      'creator_display_name': data['_airbyte_data']['fields']['creator']['displayName'],
  }