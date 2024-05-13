from authz.authz import apiv1 as api
from authz.resource.apiv1.user import UserResourse

api.add_resource(
    UserResourse,
    "/users",
    methods=["GET", "POST"],
    endpoint="users"
)

api.add_resource(
    UserResourse,
    "/user/<user_id>",
    methods=["GET", "PATCH", "DELETE"],
    endpoint="user"
)