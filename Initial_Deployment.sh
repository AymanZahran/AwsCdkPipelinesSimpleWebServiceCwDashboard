#!/bin/bash
export $(cat .env | xargs)
aws configure set default.region $AWS_REGION
aws configure set aws_access_key_id $AWS_ACCESS_KEY
aws configure set aws_secret_access_key $AWS_SECRET_KEY
aws secretsmanager create-secret --name github-token --secret-string $GITHUB_TOKEN
source .venv/bin/activate
pip install -r requirements.txt
cdk bootstrap
cdk deploy --require-approval never
