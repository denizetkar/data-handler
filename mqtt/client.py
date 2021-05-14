import threading

import paho.mqtt.client as mqtt


class SafeClient(mqtt.Client):
    def __init__(self, client_id="", clean_session=None, userdata=None, protocol=mqtt.MQTTv311, transport="tcp"):
        super().__init__(
            client_id=client_id,
            clean_session=clean_session,
            userdata=userdata,
            protocol=protocol,
            transport=transport,
        )
        self._pub_sub_lock = threading.RLock()

    def publish(self, topic, payload=None, qos=0, retain=False, properties=None):
        print("Would have published {} to topic {}".format(payload, topic))
        return
        with self._pub_sub_lock:
            return super().publish(topic, payload=payload, qos=qos, retain=retain, properties=properties)

    def subscribe(self, topic, qos=0, options=None, properties=None):
        with self._pub_sub_lock:
            return super().subscribe(topic, qos=qos, options=options, properties=properties)
