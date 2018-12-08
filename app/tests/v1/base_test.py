import unittest
import json
from app import create_app
import datetime


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

        self.incident = {
            "created_on":"12-3-2018",
            "created_by":"khalid Hashi",
            "type":"corruption",
            "location":"1.291', 36.8219",
            "status": "pending",
            "images": "images",
            "videos": "videos",
            "comment": "comment"

        }


        self.user_register = self.client.post(
            '/api/v1/user/register',
            data=json.dumps(dict(
                first="khalid",
                last_name="Hashi",
                other_names="Shirwa",
                email="khalud@gmail.com",
                phone_number="0706673533",
                user_name = "huudi01",
                registered = "yes",
                is_admin  = " True"



            )),
            content_type='application/json'
        )

        self.user_response = self.client.post(
            '/api/v1/user/login',
            data=json.dumps(dict(
                email='khalud@gmail.com',
                password='maneed12'
            )),
            content_type='application/json'
        )
