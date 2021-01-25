from flask import Flask
from flask_apispec.extension import FlaskApiSpec

from application import restapi
from application.restapi.resources import BasicProcessing
from application.restapi.documentation.api_spec import spec


def create_app():
    app = Flask(__name__)

    restapi.init_app(app)
    configure_swagger(app)

    return app

def configure_swagger(app):

    app.config.update({
        'APISPEC_SPEC': spec,
        'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
        })

    docs = FlaskApiSpec(app)
    docs.register(BasicProcessing, blueprint='restapi')
