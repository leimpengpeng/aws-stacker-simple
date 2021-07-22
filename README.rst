### Description
- Simple project using stacker library for aws bucket s3 trigger lambda function

## Env setup
#### First time
* aws profile been setup
* init venv environment
```
    $ cd automatecfg
    $ poetry init
```    
#### Activate environment
```
    $ ./shell.sh
    $ pip install requirement - for first time
```
#### Deploy to aws
```
    $ stacker build -r ap-southeast-1 env/ci.yaml config.yaml --recreate-failed
```
