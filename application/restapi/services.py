from application.utils.processar_mensagem import (load_data,
                                                                     validar_tamanho_mensagem,
                                                                     remover_ddd_sp,
                                                                     validar_hora_agendamento,
                                                                     validar_celular,
                                                                     remover_destinatario_duplicado,
                                                                     identiticar_broker,
                                                                     validar_black_list,
                                                                     montar_mensagem)


class BasicProcessingServie():

    @staticmethod
    def execute(file):
        df = load_data(file)
        df = validar_tamanho_mensagem(df)
        df = remover_ddd_sp(df)
        df = validar_hora_agendamento(df)
        df = validar_celular(df)
        df = remover_destinatario_duplicado(df)
        df = identiticar_broker(df)
        df = validar_black_list(df)
        response = montar_mensagem(df)

        return response