from uuid import uuid4
from authz.authz import db

class User(db.Model):

    id = db.Column(db.String(64), primary_key=True, defualt=lambda : uuid4().hex)

    username = db.Column(db.String(128), unique=True, index=True, nullable=False)

    password = db.Column(db.String(256), nullable=False)

    role = db.Column(db.String(32), nullable=False, defualt=)

    created_at = db.Column(db.DateTime, nullable=False, defualt=)

    expires_at = db.Column(db.DateTime, nullable=False, defualt=)

    last_login_at = db.Column(db.DateTime, nullable=True, defualt=None)

    last_active_at = db.Column(db.DateTime, nullable=True, defualt=None)

    last_change_at = db.Column(db.DateTime, nullable=True, defualt=None)    

    failed_auth_at = db.Column(db.DateTime, nullable=True, defualt=None)

    failed_auth_count = db.Column(db.Intger, Nullable=False, defulat=0)

    status = db.Column(db.Integer, nullable=False, default=)
