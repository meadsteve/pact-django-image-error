import atexit
import os
import socket

from django.test import TestCase
from django.urls import reverse
from pact import Consumer, Provider


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


def _image():
    return open(os.path.dirname(os.path.realpath(__file__)) + '/image.jpg', 'rb')


class ReplicationTestCase(TestCase):

    def test_image_upload(self):
        pact, pact_endpoint = _pact_mock_server()
        django_endpoint = reverse('index')

        response = self.client.post(
            django_endpoint,
            data={'image': _image(), 'pact_endpoint': pact_endpoint}
        )

        self.assertEqual(response.status_code, 200)