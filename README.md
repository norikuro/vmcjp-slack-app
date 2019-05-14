# vmc-demo

## Abstract
This document describes the vSphere Automation Python SDK samples that use the vSphere Automation
python client library. Additionally, some of the samples demonstrate the combined use of the
vSphere Automation and vSphere APIs. To support this combined use, the vSphere Automation Python SDK
samples require the vSphere Management SDK packages (pyVmomi) to be installed on the client.
The samples have been developed to work with python 2.7.x and 3.3+


## Installing vmc-demo to local

See example below for specifying the --extra-index-url parameter.

```cmd
git clone https://github.com/norikuro/vmc-demo/
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
