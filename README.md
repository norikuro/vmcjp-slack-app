# vmc-demo

## Abstract
SDDC.py will back up VMware Cloud on AWS configurations like following information to AWS S3.
* VMware Cloud on AWS SDDC's id and name.
* Number of hosts
* Management CIDR block
* SDDC version
You can run this script on AWS EC2 or AWS Lambda.


## Clone vmc-demo to local

```cmd
git clone https://github.com/norikuro/vmc-demo.git
```

## First, set PYTHONPATH to use this  
```cmd
export PYTHONPATH=${PWD}:$PYTHONPATH
```

## Prepare config files
We need following JSON files to run this script.  

| file          | description                                                  |
|---------------|--------------------------------------------------------------|
| s3cinfig.json | This file contains S3 information like bucket and file name. |



## Run scripts

```cmd
$ python sddc.py
```
