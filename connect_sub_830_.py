from awsiot import mqtt_connection_builder

import time
from datetime import datetime

import sys

ENDPOINT = "dxi-iot-endpoint.cvda.qa-ph3.dconnect2.daihatsu.co.jp"
CLIENT_ID = "SHIFT830-dcm18"
TOPIC="dt/dxi/bcall/SHIFT830-dcm18/response"
PATH_TO_CERTIFICATE = "crt/crt/certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "crt/crt/private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "crt/crt/aws-ca.pem"

MESSAGE = ""

limit = datetime(2026,5,27,0,0)
current = datetime.now()

if current > limit:
    print("not ready")
    sys.exit()
else:
    print("entering program") 


mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERTIFICATE,
    pri_key_filepath=PATH_TO_PRIVATE_KEY,
    ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
    client_id=CLIENT_ID,
    keep_alive_secs=120
)

connect_future = mqtt_connection.connect()

# result() waits until a result is available
connect_future.result()

client_id=CLIENT_ID
print(f'{client_id} is connected!')



# call back to trigger when a message is received
def on_message_received(topic, payload, dup, qos, retain, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    current_timestamp = time.time()
    print("my_simulator recieved timestamp : ", current_timestamp)
    current_time = datetime.now()
    print("my_simulator recieved time : ", current_time)

##### subscribe to topic
from awscrt import mqtt
subscribe_future, packet_id = mqtt_connection.subscribe(
    topic=TOPIC,
    qos=mqtt.QoS.AT_LEAST_ONCE,
    callback=on_message_received
)

# result() waits until a result is available
subscribe_result = subscribe_future.result()
##print("ss")
print(f'Subscribed to {TOPIC}')

import threading
threading.Event().wait()
