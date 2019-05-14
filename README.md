# vmc-demo

## Abstract
SDDC.py will back up VMware Cloud on AWS configurations to AWS S3 like following information.
* VMware Cloud on AWS SDDC's id and name.
* Number of hosts
* Management CIDR block
* SDDC version


## Clone vmc-demo to local

```cmd
git clone https://github.com/norikuro/vmc-demo.git
```

## First, set PYTHONPATH to use this  
```cmd
export PYTHONPATH=${PWD}:$PYTHONPATH
```

## Run scripts

```cmd
$ python sddc.py
```
