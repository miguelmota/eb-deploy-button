import boto3
import json

client = boto3.client('elasticbeanstalk')

def deployLatestVersion():
    response = client.describe_application_versions(
        ApplicationName='reportal',
        MaxRecords=1
    )

    latestVersion = response['ApplicationVersions'][0]['VersionLabel']

    response = client.update_environment(
        EnvironmentName='reportal-docker-dev',
        VersionLabel=latestVersion
    )

    print(response)
