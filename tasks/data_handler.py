from typing import Any, Dict

from mqtt import SafeClient

from .publisher import on_connect as pub_on_connect
from .subscriber import on_connect as sub_on_connect
from .subscriber import on_message as sub_on_message


class DataHandler:
    def __init__(
        self,
        sub_broker_hostname: str,
        sub_broker_port: int,
        sub_credentials: Dict[str, str],
        sub_topic_name: str,
        pub_broker_hostname: str,
        pub_broker_port: int,
        pub_credentials: Dict[str, str],
        username: str,
    ):
        self._sub_broker_hostname = sub_broker_hostname
        self._sub_broker_port = sub_broker_port
        self._sub_credentials = sub_credentials
        self._sub_topic_name = sub_topic_name
        self._pub_broker_hostname = pub_broker_hostname
        self._pub_broker_port = pub_broker_port
        self._pub_credentials = pub_credentials
        self._username = username

        self._sub_client = SafeClient()
        self._pub_client = SafeClient()

        self._sub_client.on_connect = sub_on_connect
        self._sub_client.on_message = sub_on_message
        self._pub_client.on_connect = pub_on_connect
        user_data: Dict[str, Any] = {
            "sub_topic_name": self._sub_topic_name,
            "pub_topic_name": "{}_{}".format(self._pub_credentials["user_id"], self._pub_credentials["device_id"]),
            "sub_client": self._sub_client,
            "pub_client": self._pub_client,
            "username": self._username,
            "pub_credentials": self._pub_credentials,
        }
        self._sub_client.user_data_set(user_data)
        self._pub_client.user_data_set(user_data)
        self._sub_client.username_pw_set(sub_credentials["username"], sub_credentials["password"])
        self._pub_client.username_pw_set("JWT", pub_credentials["token"])
        self._sub_client.connect(self._sub_broker_hostname, self._sub_broker_port)
        self._pub_client.connect(self._pub_broker_hostname, self._pub_broker_port)

    def start(self):
        self._sub_client.loop_start()
        self._pub_client.loop_forever()
