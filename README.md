# Chicken_disease_classification

1. Create environment
`conda create -p chicken python==3.8 -y`

2. Install dependencies
`pip install -r requirements.txt`

## Workflows

1. update config.yaml
2. update the secrets.yaml [optional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml

## Run tensorboard
tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/

## DVC

`dvc init`

`dvc repro`

`dvc dag`


## AWS Deployment 

Save the URI = "331777385192.dkr.ecr.us-east-1.amazonaws.com/chicken-disease"

## Run commands in EC2 

`sudo apt-get update -y`

`sudo apt-get upgrade`

`curl -fsSL https://get.docker.com -o get-docker.sh`

`sudo sh get-docker.sh`

`sudo usermod -aG docker ubuntu`

`newgrp docker`

### Check if docker in running 

`docker --version`

