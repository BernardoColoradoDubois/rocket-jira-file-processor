def project_parser(data:dict)->dict:
  
  if 'projectCategory' not in data['_airbyte_data']:
    data['_airbyte_data']['projectCategory'] = {}
  
  return {
    'project_id': data['_airbyte_data']['id'],
    'project_key': data['_airbyte_data']['key'],
    'project_name': data['_airbyte_data']['name'],
    'project_type_key': data['_airbyte_data']['projectTypeKey'],
    'project_category_id': data['_airbyte_data']['projectCategory'].get('id', None),
    'project_category_name': data['_airbyte_data']['projectCategory'].get('name', None),
    'lead_account_id': data['_airbyte_data']['lead']['accountId'],
    'lead_display_name': data['_airbyte_data']['lead']['displayName'],
    'is_private': data['_airbyte_data']['isPrivate'],
    'simplified': data['_airbyte_data']['simplified']
  }