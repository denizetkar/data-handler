from typing import Any, Dict

from mqtt import SafeClient


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client: SafeClient, userdata: Any, flags: Dict[str, int], rc: int):
    print(
        "Publisher '{}' connected with result code {}".format(
            client._client_id.decode("utf-8") if isinstance(client._client_id, bytes) else client._client_id, str(rc)
        )
    )
