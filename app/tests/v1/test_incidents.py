import json
from app.tests.v1.base_test import BaseTest

class TestIncidents(BaseTest):


    def test_post_incident(self):
        with self.client:
            response = self.client.post(
                '/api/v1/incidents',

                data = json.dumps(self.incident),
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertTrue(result['message'] !=  'New Incident recorded')
            self.assertEqual(response.status_code, 200)


    def test_get_incident(self):
        with self.client:
            response = self.client.get(
                '/api/v1/incidents',

                content_type = 'application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Incidents'])


    def test_get_single_incident(self):
        with self.client:
            response = self.client.get(
                '/api/v1/incidents/1',

                content_type = 'application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertTrue(result['response'])
            self.assertEqual(response.status_code, 200, result['response'])

    def test_single_incident_not_available(self):
        with self.client:
            response = self.client.get(
                '/api/v1/incidents/1234455',

                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertTrue(result['response'] == 'Incident Not Available')
            self.assertEqual(response.status_code, 200)
