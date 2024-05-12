from authz.util import jsonify

class UserController:

    def get_users():
        return jsonify(status=501, code=107)

    def get_user(user_id):
        return jsonify(status=501, code=107)

    def create_user():
        return jsonify(status=501, code=107)

    def update_user(user_id):
        return jsonify(status=501, code=107)

    def delete_user(user_id):
        return jsonify(status=501, code=107)
