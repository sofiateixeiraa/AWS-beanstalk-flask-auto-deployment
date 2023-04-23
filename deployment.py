import boto3
import os

REGION = 'eu-west-3'
APPLICATION_NAME = 'flask-sofia-app'
ENVIRONMENT_NAME = 'flask-sofia-env'

# Create  client
eb_client = boto3.client('elasticbeanstalk', region_name=REGION)

response = eb_client.create_application_version(
    ApplicationName=APPLICATION_NAME,
    VersionLabel='1.0',
    SourceBundle={
        'S3Bucket': os.environ['S3_BUCKET'],
        'S3Key': os.environ['S3_KEY']
    }
)

response = eb_client.update_environment(
    EnvironmentName=ENVIRONMENT_NAME,
    VersionLabel='1.0'
)

waiter = eb_client.get_waiter('environment_updated')
waiter.wait(
    EnvironmentName=ENVIRONMENT_NAME,
    IncludeDeleted=False
)

print("Flask application deployed successfully to Elastic Beanstalk!")
