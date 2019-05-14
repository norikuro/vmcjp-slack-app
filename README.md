# vmc-demo

## Abstract
SDDC.py can back up VMware Cloud on AWS configurations like following.
* VMware Cloud on AWS SDDC's id and name.
* Number of hosts
* Management CIDR block
* SDDC version


## Installing vmc-demo to local

See example below for specifying the --extra-index-url parameter.

```cmd
git clone https://github.com/norikuro/vmc-demo.git
```

## First, set PYTHONPATH to use this  

* Linux/Mac:

    export PYTHONPATH=${PWD}:$PYTHONPATH

* Windows:

    set PYTHONPATH=%cd%;%PYTHONPATH%

### Run scripts

```cmd
$ python sddc.py
```
