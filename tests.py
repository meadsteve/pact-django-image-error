import atexit
import os
import socket

from pact import Consumer, Provider
from requests import put

def _pact_mock_server():

    port = 3141

    pact_address = socket.gethostbyname(socket.gethostname())
    pact = Consumer('TestConsumer').has_pact_with(
        Provider('TestProvider'),
        host_name='0.0.0.0',
        port=port,
        log_dir="/app"
    )
    pact.start_service()
    atexit.register(pact.stop_service)
    server_address_pair = pact, "http://{}:{}".format(pact_address, port)
    return server_address_pair


def test_image_upload():
    pact, pact_endpoint = _pact_mock_server()

    image = open(os.path.dirname(os.path.realpath(__file__)) + '/image.jpg', 'rb')

    result = put(pact_endpoint, data=image)

    assert result.status_code == 200, "Error: %s" % result.json().get("message", "unknown")