import argparse
import json
from typing import Dict

from tasks import DataHandler


def main(args: argparse.Namespace):
    with open(args.sub_credentials_path, "rt") as f:
        sub_credentials: Dict[str, str] = json.load(f)
    with open(args.pub_credentials_path, "rt") as f:
        pub_credentials: Dict[str, str] = json.load(f)
    DataHandler(
        args.sub_broker_hostname,
        args.sub_broker_port,
        sub_credentials,
        args.sub_topic_name,
        args.pub_broker_hostname,
        args.pub_broker_port,
        pub_credentials,
        args.username,
    ).start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sub-broker-hostname",
        type=str,
        default="iotplatform.caps.in.tum.de",
        help="Host name of the MQTT broker to subscribe.",
    )
    parser.add_argument(
        "--sub-broker-port",
        type=int,
        default=1885,
        help="Port of the MQTT broker to subscribe.",
    )
    parser.add_argument(
        "--sub-credentials-path",
        type=str,
        required=True,
        help="Path to the .json file containing credentials to use for MQTT subscription."
        " It has the following format: {'username': <username>, 'password': <password>}",
    )
    parser.add_argument(
        "--sub-topic-name",
        type=str,
        default="ROOM_EVENTS",
        help="MQTT topic to subscribe.",
    )
    parser.add_argument(
        "--pub-broker-hostname",
        type=str,
        default="131.159.35.132",
        help="Host name of the MQTT broker to publish.",
    )
    parser.add_argument(
        "--pub-broker-port",
        type=int,
        default=1883,
        help="Port of the MQTT broker to publish.",
    )
    parser.add_argument(
        "--pub-credentials-path",
        type=str,
        required=True,
        help="Path to the .json file containing credentials to use for MQTT publishing."
        " It has the following format: {'user_id': <user_id>, 'device_id': <device_id>,"
        " 'token': <token>}",
    )
    parser.add_argument(
        "--username",
        type=str,
        default="group4_2021_ss",
        help="Username to use as part of the published count payloads.",
    )
    main(parser.parse_args())
