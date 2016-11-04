# Portal Deploy Button

> Deploy latest reportal application release on Elastic Beanstalk to production.

<img src="./assets/big_red_button.jpg" width="400">

## Requirements

- Python 2.7+
- `mpg321` (for audio)
- Python libs
	- `boto3` (AWS library)
	- `pyusb`
	- `termcolor`

# Configure

```bash
export EB_ENV_NAME='reportal-docker-prod'
export EB_APP_NAME='reportal'
```

## Run

```bash
python deploy.py
```
