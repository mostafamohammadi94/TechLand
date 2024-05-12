from flask_restful import Resourse
from authz.controller.apiv1 import UserController

class UserResourse(Resource):
    def get(self, user_id=None):
        """
        GET /users --> Get list of users
        GET /users/<user_id> --> Get user.
        """
        if user_id is None:
            return UserController.get_users()
        else:
            return UserController.get_user(user_id)
    
    def post(self):
        """
        POST /user --> Create new user.
        POST /users/<user_id< --> Not allowed.
        """
        return UserController.create_user()

    
    def patch(self, user_id):
        """
        PATCH /users --> Not Allowed.
        PATCH /users/<user_id> --> Update Uesr.
        """
        return UserController.update_user(user_id)

    def delete(self, user_id):
        """
        DELETE /user --> Not allowed.
        DELETE /user/<user_id> --> Delete user.
        """
        return UserController.delete_user(user_id)



