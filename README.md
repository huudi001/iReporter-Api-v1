[![Build Status](https://travis-ci.org/huudi001/iReporter-Api-v1.svg?branch=ch-tests)](https://travis-ci.org/huudi001/iReporter-Api-v1)


# iReporter-API

 iReporter is an application that enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

### What you can Achieve
1. A user can add a an incident
2. A user can get all incidents
3. A user can get a specific incident
4. A user can delete specific incident
5. A user can update a specific incident

### API Endpoints
| API Endpoint | Functionality |
| -----------  | ------------- |
| POST /api/v1/user/register |  Register a new user |
| POST /api/v1/user/login |  Logins in a user  |
| GET /api/v1/incidetns |  Fetch all incidents|
| POST /api/v1/incidents |  Create a single incident into incident list |
| GET /api/v1/incidents/<incidentsId> |  Fetch a single incident into incidents list |
| PUT /api/v1/incidents/<incidentsId> |  update a single incident |
| DELETE /api/v1/incidents/<incidentsId> |  delete a single incident |




### How to run tests
This project has been implemented using unit tests. This is how you can test the endpoints:
* `git clone https://github.com/huudi001/iReporter-Api-v1.git`
* `cd iReporter-Api-v1 `
* Activate the virtual environment `virtualenv venv'
* Install all dependencies required `pip install -r requirements.txt`
* Now run the unittests `nosetests` or `nosetests app/tests/v1`
* Test API endpoints in postman
