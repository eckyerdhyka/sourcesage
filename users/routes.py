from flask_restful import Api
from users.views import LoginApi, ForgotPassword, SignUpApi, ResetPassword,Profile


def create_authentication_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(SignUpApi, "/sign-up")
    api.add_resource(LoginApi, "/login")
    api.add_resource(ForgotPassword, "/forgot-password")
    api.add_resource(ResetPassword, "/reset-password/<token>")
    api.add_resource(Profile, "/me")
