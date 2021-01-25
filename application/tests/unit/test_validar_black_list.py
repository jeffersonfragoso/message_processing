import pandas as pd
from application.utils.processar_mensagem import validar_black_list


class TestBlackList(object):

    def load_data(self):
        """
            Carrega um conjunto de mensagens contendo um destinatário válido (10976666666) e
            outro que está na blacklist (2498672208)

            bff58d7b-8b4a-456a-b852-5a3e000c0e63;10;976666666;NEXTEL;15:24:03;Mensagem será enviada.
            bff58d7b-8b4a-456a-vg52-395c8875ad30;24;986722083;OI;10:24:03;Mensagem bloqueada (Destinatário na black list).

        """
        data_tesst = {'id_mensagem': ['bff58d7b-8b4a-456a-b852-5a3e000c0e63', 'bff58d7b-8b4a-456a-vg52-395c8875ad30'],
                      'ddd': ['10', '24'],
                      'celular': ['976666666', '986722083'],
                      'operadora': ['NEXTEL', 'OI'],
                      'hora_agendamento': ['15:24:03', '10:24:03'],
                      'texto_msg': ['Mensagem será enviada.', 'Mensagem bloqueada (Destinatário na black list).']}

        df = pd.DataFrame(data_tesst)
        df['destinatario'] = df.apply(lambda row: f"{row['ddd']}{row['celular']}", axis=1)
        return df

    def test_validar_black_list(self, request_context):

        """
            Remove registro que contenha destinatário na Black List.

            DADO que tenha um conjunto de mensagens onde contém o destinatário (2498672208)
            QUANDO solicitar validar o destinatário na blacklist
            ENTAO deve remover as mensagens desse destinatario

        """
        df = self.load_data()
        df = validar_black_list(df)

        # Verifica se o destinatário (2498672208) foi removido
        black_target = df.loc[(df['destinatario'] == '24986722083')]

        # Verifica se o destinatário (10976666666) permanece
        ok_target = df.loc[(df['destinatario'] == '10976666666')]

        assert black_target.empty == True
        assert not ok_target.empty
