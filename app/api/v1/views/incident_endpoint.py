import datetime
from flask import Flask, abort, request, make_response, jsonify, Blueprint
from flask_restful import Resource, Api

from app.api.v1.models.incidents import IncidentsData, incidents

class Incidents(Resource):

    def get(self):
        """Fetch all incidents:
            Returns: json incidents
        """
        return make_response(jsonify(
            {
                'Incidents':incidents
            }
        ),200)


    def post(self):
        """post an incident to list
            return : json single incident confirmation 
        """

        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"})
        now = datetime.datetime.now()
        created_on = now
        created_by= data.get('created_by')
        type = data.get("type")
        location = data.get('location')
        status= data.get('status')
        images = data.get("images")
        videos = data.get('videos')
        comment = data.get('comment')

        IncidentsData().save_incident(created_on, created_by, type, location, status, images , videos, comment)

        return jsonify( {'message':'New incident added successfully'})

class Getsingleincident(Resource):
    ''' fetch a single incident '''

    def get(self, incidentId):
        """Fetch a single incident record
            param:
            <int:incidentId>
        """
        try:
            isinstance(int(incidentId), int)
            print('string')
            for incident in incidents:
                if incident['incidentId'] == int(incidentId):
                    return jsonify(
                        {
                            'response':incident
                        }
                    )
        except ValueError:
            print('not string')
            response = jsonify({'message':'not allowed'})
            return response

        return jsonify({'response':'Incident Not Available'})

class Deleteincident(Resource):
    ''' delete a single incident '''

    def get(self, incidentId):
        """Delete a single incident record
            param:
            <int:incidentId>
        """
        try:
            isinstance(int(incidentId), int)
            print('string')
            for incident in incidents:
                if incident['incidentId'] == int(incidentId):
                    incidents.remove(incident)
                    response = jsonify({'message':'incident successfully deleted'})
                    return response
        except ValueError:
            print('not string')
            response = jsonify({'message':'not allowed'})
            return response

        return jsonify({'response':'Incident Not Available'})
