# Elastic Beanstalk Deploy Button

> Deploy latest application release on Elastic Beanstalk to an environment using the [Dream Cheeky Big Red Button](http://dreamcheeky.com/big-red-button).

<img src="./assets/big_red_button.jpg" width="200">

## Requirements

- Python 2.7+
- `mpg321` (for audio)
- `espeak` (for speech)
- Python libs
	- `boto3` (AWS library)
	- `pyusb`
	- `termcolor`

## Configure

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
export EB_ENV_NAME="YOUR_ELASTIC_BEANSTALK_ENVIRONMENT_NAME"
export EB_APP_NAME="YOUR_ELASTIC_BEANSTALK_APPLICATION_NAME"
```

## Run

```bash
pi@raspberrypi:~/dev/eb-deploy-button $ python deploy.py
On stand by..

WARNING!! The cover has been opened. DEPLOY AT YOUR RISK.

The button has been pressed. Release to deploy.

---DEPLOY INITIATED---

Please close lid.

Deploying latest version: moogs.moogs-docker-prod.3b526833072.20161104-001943

Health status: Info

> Deploying new version to instance(s).

> Environment health has transitioned from Ok to Info. Application update in progress on 1 instance. 0 out of 1 instance completed (running for 11 seconds).

> Docker container 870734c71e15 is running aws_beanstalk/current-app.

Health status: Ok

> Environment update completed successfully.

Deploy successful.
```

# Credits

- [big_red](https://github.com/patricksmith/big_red) Python lib

# License

MIT
