

def lambda_handler(event, context):

  for record in event['Records']: 

    # obtenemos nombre del bucket
    bucket = record['s3']['bucket']['name'] 
    
    # obtenemos nombre del archivo
    key = record['s3']['object']['key'] 