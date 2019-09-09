import unittest
import mock
import json

import requests

import urbanairship as ua
from tests import TEST_KEY, TEST_SECRET


class TestExperiment(unittest.TestCase):
    def setUp(self):
        self.airship = ua.Airship(TEST_KEY, TEST_SECRET)

        push_1 = self.airship.create_push()
        push_1.notification = ua.notification(alert='test message 1')

        push_2 = self.airship.create_push()
        push_2.notification = ua.notification(alert='test message 2')

        variant_1 = ua.Variant(push_1,
                               description='A description of the variant',
                               name='Testing')
        variant_2 = ua.Variant(push_2)

        self.name = "Experiment Test"
        self.audience = 'all'
        self.device_types = ['android', 'ios']
        self.campaigns = ua.campaigns(categories=['campaign', 'categories'])
        self.operation_id = 'd67d4de6-934f-4ebb-aef0-250d89699b6b'
        self.experiment_id = 'f0c975e4-c01a-436b-92a0-2a360f87b211'
        self.push_id = '0edb9e6f-2198-4c42-aada-5a49eb03bcbb'
        self.variants = [variant_1, variant_2]

    def test_simple_experiment(self):
        with mock.patch.object(ua.Airship, '_request') as mock_request:
            response = requests.Response()
            response._content = json.dumps({
                "ok": True,
                "operation_id": self.operation_id,
                "experiment_id": self.experiment_id,
                "push_id": self.push_id
            }).encode('utf-8')
            response.status_code = 201
            mock_request.return_value = response

            experiment_object = ua.Experiment(name=self.name,
                                              audience=self.audience,
                                              device_types=self.device_types,
                                              campaigns=self.campaigns,
                                              variants=self.variants
                                              )
            experiment_payload = {
                "name":"Experiment Test",
                "audience":"all",
                "device_types":["android", "ios"],
                "campaigns":{
                    "categories":[
                        "campaign","categories"
                    ]},
                "variants":[{
                    "description":"A description of the variant",
                    "name":"Testing",
                    "push":{
                        "notification":{
                            "alert":"test message 1"
                        }
                    }
                },
                {
                    "push":{
                        "notification":{
                            "alert":"test message 2"
                        }
                    }
                }
                ]
            }
            self.assertEqual(experiment_object.payload, experiment_payload)
