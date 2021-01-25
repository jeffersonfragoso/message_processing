from flask import Blueprint
from flask_restful import Api

from application.restapi.resources import BasicProcessing


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(BasicProcessing, "/basic_processing/")
    app.register_blueprint(bp)
