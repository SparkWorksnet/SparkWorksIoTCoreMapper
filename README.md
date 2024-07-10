# Spark Works IoT Core Mapper

Libraries and helpers for interacting with the Spark Works IoT core using the mapper interfaces.

## Creating a mapper

Visit the Things page of your deployment's web console and create a new mapper device.
This will provide you with the following:

+ DeviceId: in the form of `{Deployment}_mapper_{someId}`
+ Device Certificate

````shell
-----BEGIN CERTIFICATE-----
ABCDEFG....ABCDEFG
-----END CERTIFICATE-----
````

+ Device Private Key

````shell
-----BEGIN RSA PRIVATE KEY-----
ABCDEFG....ABCDEFG
-----END RSA PRIVATE KEY-----
````

+ Device Public Key

````shell
-----BEGIN PUBLIC KEY-----
ABCDEFG....ABCDEFG
-----END PUBLIC KEY-----
````

Download these keys as this is the only time you will have access to them.

## Publishing Data to Spark Works IoT

+ Using [Python](python)
