def users_parser(data:dict)->dict:
  
  if 'avatarUrls' not in data['_airbyte_data']:
    data['_airbyte_data']['avatarUrls'] = {}
  
  return {
      'account_id': data['_airbyte_data'].get('accountId', None),
      'account_type': data['_airbyte_data']['accountType'],
      'display_name': data['_airbyte_data']['displayName'],
      'email_address': data['_airbyte_data'].get('emailAddress', None),
      'avatar_url': data['_airbyte_data']['avatarUrls'].get('48x48',None),
      'active': data['_airbyte_data']['active']
  }