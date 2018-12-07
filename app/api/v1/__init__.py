from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config
from app.api.v1.views.incident_endpoint import Incidents, Getsingleincident, Deleteincident, Updateincident
from app.api.v1.views.users_endpoints import Register, Login


version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)




api.add_resource(Incidents, '/incidents')
api.add_resource(Getsingleincident, '/incidents/<incidentId>')
api.add_resource(Deleteincident, '/incidents/<incidentId>')
api.add_resource(Updateincident, '/incidents/<incidentId>')
api.add_resource(Register, '/user/register')
api.add_resource(Login, '/user/login')
