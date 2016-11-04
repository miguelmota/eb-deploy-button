# Elastic Beanstalk Deploy Button

> Deploy latest application release on Elastic Beanstalk to an environment.

<img src="./assets/big_red_button.jpg" width="400">

## Requirements

- Python 2.7+
- `mpg321` (for audio)
- Python libs
	- `boto3` (AWS library)
	- `pyusb`
	- `termcolor`

# Configure

AWS keys

`~/.aws/config`

```text
[default]
region = YOUR_AWS_REGION
```

`~/.aws/credentials`

```text
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

Environment variables

```bash
export EB_ENV_NAME='reportal-docker-prod'
export EB_APP_NAME='reportal'
```

## Run

```bash
python deploy.py
```
