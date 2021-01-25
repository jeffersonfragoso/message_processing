from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import fields

ma_plugin = MarshmallowPlugin()
spec = APISpec(title='PGMais - RestAPI para processar mensagens',
               version='v1',
               openapi_version='2.0',
               plugins=(ma_plugin,)

)

@ma_plugin.map_to_openapi_type('file', None)
class CustomFieldFileUpload(fields.Field):
    pass