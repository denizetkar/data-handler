import time
from typing import Any, Dict

from mqtt import MQTTMessage, SafeClient

ENTER_MSG = "enter"
EXIT_MSG = "leave"
ROOM_COUNT = 0
PAYLOAD_TEMPLATE = '{"username":"%s","%s":%d,"device_id":%d,"timestamp":%u}'


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
        ROOM_COUNT += 1
    elif msg == EXIT_MSG:
        ROOM_COUNT = max(0, ROOM_COUNT - 1)
    pub_client.publish(
        userdata["pub_topic_name"],
        PAYLOAD_TEMPLATE
        % (userdata["username"], "count", ROOM_COUNT, userdata["pub_credentials"]["device_id"], time.time_ns() // 1e6),
        qos=1,
    )
