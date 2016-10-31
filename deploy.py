#!/usr/bin/env python

import boto3
import time
import json
import os
from termcolor import colored
from big_red import BigRedButton

client = boto3.client('elasticbeanstalk')

#env = 'reportal-docker-prod'
env = 'reportal-docker-dev'

class DeployButton(BigRedButton):
    def on_unknown(self):
	      print(colored('The button is in an unknown state.\n', 'yellow'))

    def on_cover_open(self):
        print(colored('WARNING!! The cover has been opened. DEPLOY AT YOUR RISK.\n', 'yellow', attrs=['bold']))
        os.system('mpg321 ./assets/siren.mp3 > /dev/null 2>&1 &')
        os.system('sleep 6 && pkill mpg321 &')

    def on_cover_close(self):
        print(colored('The cover has been closed.\n', 'white'))

    def on_button_press(self):
        print(colored('The button has been pressed. Release to deploy.\n', 'yellow'))

    def on_button_release(self):
        print(colored('---DEPLOY INITIATED---\n', 'green', attrs=['bold']))
        print(colored('Please close lid.\n', 'white'))
        print(colored('Working...\n', 'white'))
        deployLatestVersion()
        time.sleep(10)
        health_status = None
        message = None

        while not (health_status == 'Ok' or health_status == 'Severe'):
          time.sleep(5)
          last_health_status = health_status
          health_response = getEnvHealth()
          color = health_response['Color'].lower()
          status = health_response['Status']
          health_status = health_response['HealthStatus']
          refreshed_at = health_response['RefreshedAt']

          health_status_c = colored(health_status, color);

          if last_health_status != health_status:
            print('Health status: ' + health_status_c + '\n')

          env_events_response = getEnvEvents()

          for event in env_events_response['Events']:
              last_message = message
              message = event['Message']
              event_type = event['Severity']
              date = event['EventDate']
              if last_message != message:
                print(colored('> ', 'blue') + colored(message, 'white') + '\n')

        if health_status == 'Ok':
          print(colored('Deploy successful.\n', 'green', attrs=['bold']))
        else:
          print(colored('There was an error with deployment.\n', 'red', attrs=['bold']))


def deployLatestVersion():
    response = client.describe_application_versions(
        ApplicationName='reportal',
        MaxRecords=1
    )

    latest_version = response['ApplicationVersions'][0]['VersionLabel']

    response = client.update_environment(
        EnvironmentName=env,
        VersionLabel=latest_version
    )

    print(colored('Deploying latest version: ' + latest_version + '\n', 'white', attrs=['bold']))
    return response

def getEnvEvents(max_records=1):
    response = client.describe_events(
        EnvironmentName=env,
        MaxRecords=max_records
    )

    return response

def getEnvHealth():
    response = client.describe_environment_health(
        AttributeNames=[
            'All'
        ],
        EnvironmentName=env,
    )

    return response

if __name__ == '__main__':
    print(colored('On stand by..\n', 'white'))
    button = DeployButton()
    button.run()
