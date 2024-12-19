include .env

update-lambda:
	rm lambda.zip;\
	zip lambda.zip lambda_function.py;\
	zip -r lambda.zip src;\
	aws lambda update-function-code --function-name ${AWS_LAMBDA_CONFIG_NAME} --zip-file fileb://lambda.zip --region ${AWS_LAMBDA_CONFIG_REGION} --profile ${AWS_CONFIG_PROFILE}

update-layer:
	rm -r ./python;\
	mkdir python;\
	cp -r ./venv/lib ./python;\
	rm python.zip;\
	zip -r python.zip ./python;\
	aws s3 cp ./python.zip s3://${AWS_LAYER_CONFIG_S3_DEPLOYMENT_BUCKET}/lambda/layer/python.zip --profile ${AWS_CONFIG_PROFILE} --region ${AWS_LAYER_CONFIG_REGION};\
	aws lambda publish-layer-version --layer-name ${AWS_LAYER_CONFIG_NAME} --content S3Bucket=${AWS_LAYER_CONFIG_S3_DEPLOYMENT_BUCKET},S3Key=lambda/layer/python.zip --compatible-runtimes python3.10 --compatible-architectures "x86_64" "arm64"  --region ${AWS_LAYER_CONFIG_REGION} --profile ${AWS_CONFIG_PROFILE}