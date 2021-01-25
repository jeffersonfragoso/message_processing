from flask_restful import Resource, request
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource

from application.restapi.serializers import UploadFileSchema, BasicProcessingResponseSchema

from application.restapi.services import BasicProcessingServie


class BasicProcessing(MethodResource, Resource):

    @doc(description="Endpoint para executar o fluxo básico de processamento",
         tags=["Basic Processing"],
         consumes=['multipart/form-data'],
    )
    @use_kwargs(UploadFileSchema, location="files")
    @marshal_with(BasicProcessingResponseSchema)
    def post(self, file):
        """
            Processa o arquivo CSV utilizando um fluxo básico

            Parameters:
            - file (file): Arquivo csv
            - response (dict): Mensagens processadas e no padrão de CSV

            Exemplo de resposta:
            {"mensagens": "bff58d7b-8b4a-456a-b852-5a3e000c0e63;3\n
                           b7e2af69-ce52-4812-adf1-f28e653ac25e;2\n
                           d81b2696-8b62-4b8b-af82-ffff653ac25e;1\n" }

        """
        try:
            file = request.files['file']
            data = BasicProcessingServie.execute(file)

            response = {"mensagens": data}
        except Exception as ex:
            return {'errors': str((ex, str(ex.__doc__)))}

        return BasicProcessingResponseSchema().dump(response)
