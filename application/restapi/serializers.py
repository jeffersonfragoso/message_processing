from marshmallow import Schema, fields, post_dump
from application.restapi.documentation.api_spec import CustomFieldFileUpload


class UploadFileSchema(Schema):
    file = CustomFieldFileUpload(required=True,
                                 description="Arquivo csv contendo as mensagens para validação",
                                 validate=lambda file: file.mimetype == 'text/csv'
                                )


class BasicProcessingResponseSchema(Schema):
    mensagens = fields.Str(description="Mensagens processadas e no padrão de CSV")
