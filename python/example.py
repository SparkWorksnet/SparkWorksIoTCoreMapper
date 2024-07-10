import logging
import time

_deployment = "REPLACE_DEPLOYMENT"
_device_id = "REPLACE_MAPPER"
_ca_crt_path = "AmazonRootCA1.pem"
_device_crt_path = f"{_device_id}.crt"
_device_key_path = f"{_device_id}.key"

LOGGING_FORMAT = '%(filename)s:%(lineno)d - %(levelname)s - %(message)s'
# initialize logger
logger = logging.getLogger('main')
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)

from SparkWorksIoTCoreMapper import SparkWorksIoTCoreMapper

if __name__ == '__main__':
    mapper = SparkWorksIoTCoreMapper(iot_endpoint="REPLACE_IOT_ENDPOINT",
                                     deployment=_deployment, device_id=_device_id,
                                     device_crt_path=_device_crt_path,
                                     device_key_path=_device_key_path,
                                     ca_crt_path=_ca_crt_path)
    mapper.bootstrap_mqtt()

    data = {"timestamp": int(time.time()) * 1000, "temperature": 27}
    mapper.send_payload_for_self(data=data)

    data = {"timestamp": int(time.time()) * 1000, "temperature": 24}
    mapper.send_payload_for_other(other_device=f"{_device_id}_subdevice", data=data)
