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