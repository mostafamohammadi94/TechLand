from os import environ

class Config:

    ENV = environ.get("TECHLAN_AUTHZ_ENV", "production")

    DEBUG = bool(int(environ.get("TECHLAND_AUTHZ_DEBUG", "0")))

    TESTING = bool(int(environ.get("TECHLAND_AUTHZ_TESTING", "0")))

    SECRET_KEY = environ.get("TECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")

    TIMEZONE = environ.get("TECHLAND_AUTHZ_TIMEZONE", "Asia/Tehran")

    SQLALCHEMY_DATABASE_URI = environ.get("TECHLAND_AUTHZ_DATABASE_URI", "mysql+pymysql://root:test@localhost:3306/test")

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_RECORD_QUERIES = DEBUG

    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

# SQLALCHEMY_BINDS = environ.get("TECHLAND_AUTHZ_DATABASE_BINDS", None)

    USER_DEFAULT_ROLE = environ.get("TECHLAND_AUTHZ_USER_DEFAULT_ROLE", "member")
    
    USER_DEFAULT_EXPIRY = int(environ.get("TECHLAND_AUTHZ_USER_DEFAULT_EXPIRY", "365"))

    USER_DEFAULT_STATUS = int(environ.get("TECHLAND_AUTHZ_USER_DEFAULT_STATUS", "3"))