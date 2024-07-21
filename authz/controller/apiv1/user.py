from authz.model import User
from authz.schema.apiv1 import UserSchema
from authz.util import jsonify

class UserController:

    def get_users():
        users = User.query.all()
        users_schema = UserSchema(many=True) 
        return {
            "users": users_schema.dump(users)
        }

    def get_user(user_id):
        return jsonify(status=501, code=107)

    def create_user():
        return jsonify(status=501, code=107)

    def update_user(user_id):
        return jsonify(status=501, code=107)

    def delete_user(user_id):
        return jsonify(status=501, code=107)
