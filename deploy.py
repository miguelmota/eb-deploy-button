import boto3
import json

client = boto3.client('elasticbeanstalk')

env = 'reportal-docker-dev'

def deployLatestVersion():
    response = client.describe_application_versions(
        ApplicationName='reportal',
        MaxRecords=1
    )

    latestVersion = response['ApplicationVersions'][0]['VersionLabel']

    response = client.update_environment(
        EnvironmentName=env,
        VersionLabel=latestVersion
    )

    print(response)
    return response

def getEnvEvents():
    response = client.describe_events(
        EnvironmentName=env,
        MaxRecords=25
    )

    for event in response['Events']:
        message = event['Message']
        eventType = event['Severity']
        date = event['EventDate']
        print(message)

    return response

def getEnvHealth():
    response = client.describe_environment_health(
        AttributeNames=[
            'All'
        ],
        EnvironmentName=env,
    )

    color = response['Color']
    status = response['Status']
    health_status = response['HealthStatus']
    refreshed_at = response['RefreshedAt']

    print(health_status)
    return response

if __name__ == '__main__':
    getEnvHealth();
