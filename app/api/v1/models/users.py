users = []

class User():
    def save_user(self, first_name, last_name, other_names, email, phone_number,user_name, registered,is_admin):
        user_id = len(users) + 1
        user = {
        "user_id": user_id,
        "first_name": first_name,
        "last_name":  last_name,
        "other_names": other_names,
        "email": email,
        "phone_number":  phone_number,
        "user_name": user_name,
        "registered": registered,
        "is_admin": is_admin



        }
        users.append(user)

        return user
