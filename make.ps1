# Importar variables de entorno desde .env
$env = Get-Content .env | ForEach-Object {
  $key, $value = $_ -split '=', 2
  Set-Item -Path Env:$key -Value $value
}

# Función para actualizar la función Lambda
function update-lambda {
  # Eliminar el archivo lambda.zip si existe
  if (Test-Path lambda.zip) {
    Remove-Item lambda.zip
  }

  # Comprimir lambda_function.py en lambda.zip
  Compress-Archive -Path lambda_function.py -DestinationPath lambda.zip

  # Comprimir la carpeta src en lambda.zip
  Compress-Archive -Path src -DestinationPath lambda.zip -Update

  # Actualizar el código de la función Lambda
  aws lambda update-function-code `
    --function-name $env:AWS_LAMBDA_CONFIG_NAME `
    --zip-file fileb://lambda.zip `
    --region $env:AWS_LAMBDA_CONFIG_REGION `
    --profile $env:AWS_CONFIG_PROFILE
}

# Función para actualizar la capa Lambda
function update-layer {
  # Eliminar la carpeta python si existe
  if (Test-Path python) {
    Remove-Item python -Recurse -Force
  }

  # Crear la carpeta python
  New-Item python -ItemType Directory

  # Copiar la carpeta venv/lib a python
  Copy-Item -Path venv/lib -Destination python -Recurse

  # Eliminar el archivo python.zip si existe
  if (Test-Path python.zip) {
    Remove-Item python.zip
  }

  # Comprimir la carpeta python en python.zip
  Compress-Archive -Path python -DestinationPath python.zip

  # Copiar python.zip a S3
  aws s3 cp ./python.zip s3://$env:AWS_LAYER_CONFIG_S3_DEPLOYMENT_BUCKET/lambda/layer/python.zip `
    --profile $env:AWS_CONFIG_PROFILE `
    --region $env:AWS_LAYER_CONFIG_REGION

  # Publicar una nueva versión de la capa Lambda
  aws lambda publish-layer-version `
    --layer-name $env:AWS_LAYER_CONFIG_NAME `
    --content S3Bucket=$env:AWS_LAYER_CONFIG_S3_DEPLOYMENT_BUCKET,S3Key=lambda/layer/python.zip `
    --compatible-runtimes python3.10 `
    --compatible-architectures "x86_64" "arm64" `
    --region $env:AWS_LAYER_CONFIG_REGION `
    --profile $env:AWS_CONFIG_PROFILE
}