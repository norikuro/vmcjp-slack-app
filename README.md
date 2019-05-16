# vmc-demo

## Abstract
SDDC.py will back up VMware Cloud on AWS configurations like following information to AWS S3.
* VMware Cloud on AWS SDDC's id and name.
* Number of hosts
* Management CIDR block
* SDDC version
You can run this script on AWS EC2 or AWS Lambda.

## Scrips
followings are main scripts
* sddc.py
* networks.py

followings are helper scripts
* firewall_rules.py
* security_groups.py
* vmcutils/*.py

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

| file          | file localtion | description |
|---|---|---|
| s3config.json | vmc-demo | This file contains S3 information like bucket and file name. |
| token.json | S3 | This file contains VMC's refresh token. |
| config.json | S3 | This file contains VMC's org id, SDDC's name, id, connected customer AWS account id and subnet id. |

### config file exsample
* s3config.json
  * location: vmc-demo/s3config.json
```cmd
{
  "bucket": "vmc-env", #S3 bucket name
  "token": "token.json", #VMC's refresh token file name
  "config": "config.json" #config file name 
}
```

* token.json
  * location: s3://vmc-env/token.json  
vmc-env is bucket name, specified in s3config.json
```cmd
{"token": "Refresh token number"}
```

* config.json
  * location: s3://vmc-env/config.json  
vmc-env is bucket name, specified in s3config.json
```cmd
{
  "org":
  {
    "id": "VMC's Organization ID"
  },
  "sddc": 
  {
    "name": "VMC SDDC name",
    "id": "SDDC ID",
    "customer_aws": 
    {
      "account_number": "Customer AWS Account ID",
      "subnet_id": "Customer AWS Subnet ID"
    }
  }
}
```

## Run scripts

```cmd
$ python sddc.py
```
