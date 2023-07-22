# Chicken-Disease-Classificatin-Project


## Workflows

1. Update config.yaml
2. update secrets.yaml [optional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml


# How to Run?

### STEPS:
Clone the repository

```bash
https://github.com/imsiraj/Chicken-Disease-Classificatin-Project/
```

### STEP 01- Create a conda environment after opening the repository
```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag