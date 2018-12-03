import re
from flask import request, jsonify
from flask_restful import Resource

from app.api.v1.models.users import User, users

email_format = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"

  
user = User()

class Login(Resource, User):

    def post(self):
        data = request.get_json()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_names = data.get("other_names")
        email = data.get("email")
        phone_number  = data.get("phone_number")
        user_name  = data.get("user_name")
        registered = data.get("registered")
        is_admin  = data.get("is_admin")





        if not data:
            return jsonify("Fields cannot be empty")
        if not email or not user_name:
            return jsonify("You must provide username and email")

        if not re.match(email_format, email):
            return jsonify({"message": "Invalid Email address"})

        user_exists = [user for user in users if email == user["email"]]

        if not user_exists:
            return jsonify({
                "message":"User does not exist"
            })
        if user_name != user_exists[0]["user_name"]:
            return jsonify({
                "message":"Wrong user_name",
                "status": 400
            })


        return jsonify( message = "Login succesfull")



class Register(Resource, User):


    def post(self):
        data = request.get_json()

        data = request.get_json()


        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_names = data.get("other_names")
        email = data.get("email")
        phone_number  = data.get("phone_number")
        user_name  = data.get("user_name")
        registered = data.get("registered")
        is_admin  = data.get("is_admin")




        if not data:
            return jsonify("Data must be in json format")
        if not email or not user_name:
            return jsonify({"message":"You must provide email and user_name"})

        if not re.match(email_format, email):
            return jsonify({"message": "Invalid email address"})

        user_exists = [user for user in users if email == user["email"]]

        if user_exists:
            return jsonify({"message":"Email address already exists"})

        else:
            User.save_user(self, first_name, last_name, other_names, email, phone_number,user_name, registered, is_admin )

            return jsonify({
                "message":"User has been registered successfully"
            })
