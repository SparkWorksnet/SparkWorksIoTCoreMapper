# Spark Works IoT Core Mapper for Python

Python Library for interacting with the Spark Works IoT core using the mapper interfaces.

## Requirements

+ Install the needed python requirements from the `requirements.txt` file using:

````shell
pip3 install -r requirements.txt
````

+ Download the Amazon CA certificate from [here](https://www.amazontrust.com/repository/AmazonRootCA1.pem) and name
  it `AmazonRootCA1.pem`

## Running the example

Update in the example file the following:

+ `_deployment` : Add your deployment name
+ `_device_id`: Add your mapper's device id
+ `iot_endpoint`: Set to your IoT endpoint
