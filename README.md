# IoT Platform Data Handler
This data handler uses `paho-mqtt` Python package. It **subscribes** to the room entry/exit event topic. Then, according to the events, it **keeps a count** of people in the seminar room **and publishes** it back to the [IoT platform](iotplatform.caps.in.tum.de) at every event occurrence.

## **Installing Dependencies:**
* Install Python3 either system-wide, user-wide or as a virtual environment,
* Run `pip install pip-tools` command via the `pip` command associated with the installed Python,
* Run `pip-sync` inside the project root folder.

## **Usage:**
    usage: main.py [-h] [--sub-broker-hostname SUB_BROKER_HOSTNAME]
                [--sub-broker-port SUB_BROKER_PORT] --sub-credentials-path
                SUB_CREDENTIALS_PATH [--sub-topic-name SUB_TOPIC_NAME]
                [--pub-broker-hostname PUB_BROKER_HOSTNAME]
                [--pub-broker-port PUB_BROKER_PORT] --pub-credentials-path
                PUB_CREDENTIALS_PATH [--username USERNAME]

    optional arguments:
    -h, --help            show this help message and exit
    --sub-broker-hostname SUB_BROKER_HOSTNAME
                            Host name of the MQTT broker to subscribe.
    --sub-broker-port SUB_BROKER_PORT
                            Port of the MQTT broker to subscribe.
    --sub-credentials-path SUB_CREDENTIALS_PATH
                            Path to the .json file containing credentials to use
                            for MQTT subscription. It has the following format:
                            {'username': <username>, 'password': <password>}
    --sub-topic-name SUB_TOPIC_NAME
                            MQTT topic to subscribe.
    --pub-broker-hostname PUB_BROKER_HOSTNAME
                            Host name of the MQTT broker to publish.
    --pub-broker-port PUB_BROKER_PORT
                            Port of the MQTT broker to publish.
    --pub-credentials-path PUB_CREDENTIALS_PATH
                            Path to the .json file containing credentials to use
                            for MQTT publishing. It has the following format:
                            {'user_id': <user_id>, 'device_id': <device_id>,
                            'token': <token>}
    --username USERNAME   Username to use as part of the published count
                            payloads.
