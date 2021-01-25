import os
import pytest
from werkzeug.datastructures import FileStorage

class TestBasicProcessing(object):

    @pytest.mark.skip(reason="adsasdasd")
    def test_basic_processinging(self, client):
        """
            DADO que tenha solicitado processar um arquivo CSV
                 através do endpoint '/api/v1.0/basic_processing/' (POST)
            ENTAO retorna apenas os registros validos
        """
        payload = {}
        # resposta_esperada = ""
        MY_PATH = os.path.dirname(os.path.abspath(__file__))
        FILE_PATH = os.path.join(MY_PATH, '../test_data', 'mensagens.csv')

        # with open(FILE_PATH, 'rb') as file:
        #     payload = {'file': file}

        file = FileStorage(
            filename="mensagens.csv",
            stream=open(FILE_PATH, "rb"),
            content_type="text/csv",
        )

        payload['file'] = file

        response = client.post('/api/v1.0/basic_processing/', data=payload, content_type="multipart/form-data")
        assert response.status_code == 200

        "verificar string de saída"