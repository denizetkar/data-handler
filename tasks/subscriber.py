import time
from typing import Any, Dict

from mqtt import MQTTMessage, SafeClient
from utils import SafeInt

ENTER_MSG = "enter"
EXIT_MSG = "leave"
ROOM_COUNT = SafeInt(0)
PAYLOAD_TEMPLATE = '{"username":"%s","%s":%d,"device_id":%d,"timestamp":%u}'
COUNT_SENSOR_NAME = "count"
RESTART_SENSOR_NAME = "restart"


def periodic_publisher_task(client: SafeClient, userdata: Dict[str, Any], period: int):
    while True:
        client.publish(
            userdata["pub_topic_name"],
            PAYLOAD_TEMPLATE
            % (
                userdata["username"],
                COUNT_SENSOR_NAME,
                ROOM_COUNT.value,
                userdata["pub_credentials"]["device_id"],
                time.time_ns() // 1e6,
            ),
            qos=1,
        )
        time.sleep(period)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client: SafeClient, userdata: Dict[str, Any], flags: Dict[str, int], rc: int):
    print(
        "Subscriber '{}' connected with result code {}".format(
            client._client_id.decode("utf-8") if isinstance(client._client_id, bytes) else client._client_id, str(rc)
        )
    )
    client.subscribe(userdata["sub_topic_name"], qos=2)


def on_message(client: SafeClient, userdata: Dict[str, Any], mqtt_msg: MQTTMessage):
    global ROOM_COUNT
    msg = mqtt_msg.payload.decode("utf-8")
    print(
        "Subscriber '{}' received message {} on topic {}".format(
            client._client_id.decode("utf-8") if isinstance(client._client_id, bytes) else client._client_id,
            msg,
            mqtt_msg.topic,
        )
    )
    pub_client: SafeClient = userdata["pub_client"]
    if msg == ENTER_MSG:
        ROOM_COUNT.increment()
    elif msg == EXIT_MSG:
        ROOM_COUNT.decrement(0)
    pub_client.publish(
        userdata["pub_topic_name"],
        PAYLOAD_TEMPLATE
        % (
            userdata["username"],
            COUNT_SENSOR_NAME,
            ROOM_COUNT.value,
            userdata["pub_credentials"]["device_id"],
            time.time_ns() // 1e6,
        ),
        qos=1,
    )
