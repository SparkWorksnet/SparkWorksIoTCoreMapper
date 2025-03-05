import json
import time

import paho.mqtt.client as paho
import ssl
import logging

LOGGING_FORMAT = '%(filename)s:%(lineno)d - %(levelname)s - %(message)s'
# initialize logger
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)


class SparkWorksIoTCoreMapper(object):

    def __init__(self, deployment, device_id, ca_crt_path, device_crt_path, device_key_path, iot_endpoint,
                 iot_port=8883):
        self.iot_endpoint = iot_endpoint
        self.iot_port = iot_port
        self.deployment = deployment
        self.device_id = device_id
        self.ca_crt_path = ca_crt_path
        self.device_crt_path = device_crt_path
        self.device_key_path = device_key_path
        self.logger = logging.getLogger('SparksIoTMapper')
        self.connected = False

    def __on_connect(self, client, userdata, flags, rc):
        self.connected = True
        self.logger.info(f"{rc}")
        self.mqtts_client.loop_start()

    def __on_message(self, client, userdata, msg):
        self.logger.info(f"{userdata}, {msg.topic} - {msg.payload}")

    def __on_log(self, client, userdata, level, buf):
        self.logger.info(f"{client}, {userdata}, {level}, {buf}")

    def __on_publish(self, client, userdata, mid):
        self.logger.info(f"on_publish, mid {mid}")

    def __on_disconnect(self, client, userdata, rc):
        self.logger.info(f"on_disconnect, mid {rc}")

    def bootstrap_mqtt(self):
        self.mqtts_client = paho.Client(client_id=self.device_id)
        self.mqtts_client.tls_set(ca_certs=self.ca_crt_path,
                                  certfile=self.device_crt_path,
                                  keyfile=self.device_key_path,
                                  cert_reqs=ssl.CERT_REQUIRED,
                                  tls_version=ssl.PROTOCOL_TLSv1_2,
                                  ciphers=None)

        self.mqtts_client.on_log = self.__on_log
        self.mqtts_client.on_connect = self.__on_connect
        self.mqtts_client.on_message = self.__on_message
        self.mqtts_client.on_publish = self.__on_publish
        self.mqtts_client._on_disconnect = self.__on_disconnect

        self.mqtts_client.connect("a2ukebs5veg22d-ats.iot.eu-west-1.amazonaws.com",
                                  port=8883,
                                  keepalive=120)

    def send_payload_for_self(self, data):
        self.send_string_payload_for_self(json.dumps(data))

    def send_string_payload_for_self(self, data):
        topic = f"{self.deployment}/{self.device_id}/{self.device_id}"
        print(f"[{topic}] {data}")
        self.mqtts_client.publish(topic=topic, payload=data, qos=0)
        self.mqtts_client.loop(timeout=1000)

    def send_payload_for_other(self, other_device, data):
        self.send_string_payload_for_other(other_device=other_device, data=json.dumps(data))

    def send_string_payload_for_other(self, other_device, data):
        topic = f"{self.deployment}/{self.device_id}/{other_device}"
        self.logger.info(f"[{topic}] {data}")
        self.mqtts_client.publish(topic=topic, payload=data, qos=0)
        self.mqtts_client.loop(timeout=1000)
