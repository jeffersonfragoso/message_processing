import pandas as pd
import numpy as np
import requests


def load_data(file):
    colunas = ['id_mensagem', 'ddd', 'celular', 'operadora', 'hora_agendamento', 'texto_msg']
    df = pd.read_csv(file, sep=";", names=colunas)
    return df


def validar_tamanho_mensagem(df):
    # Remove mensagens com mais de 140 caracteres

    filter_len_msg = (df['texto_msg'].str.len() < 140)
    df = df.loc[filter_len_msg]
    return df


def remover_ddd_sp(df):
    # Remove mensagens para DDD de SP
    # Os DDD's para a região de SP são de 11 ate o 19.
    # Utilizo o "~" para negar o filtro, dessa forma serão retornados os itens que não são de SP

    filter_ddd_sp = df['ddd'].between(11, 19)
    df = df.loc[~filter_ddd_sp]
    return df


def validar_hora_agendamento(df):
    # Remove as mensagens que possuem hora de agendamento maior que 19:59:59

    filter_hora_agendamento = (df['hora_agendamento'] < "19:59:59")
    df = df.loc[filter_hora_agendamento]
    return df


def validar_celular(df):
    # Validar nº celular
    # DDD com 2 digitos
    # DDD deve ser válido
    # número do celular deve conter 9 dígitos
    # numero do celular deve começar com o dígito 9
    # o segundo dígito deve ser > 6

    filter_celular_valido = (
                            (df['ddd'].astype(str).map(len) == 2) &
                            (df['celular'].astype(str).map(len) == 9) &
                            (df['celular'].astype(str).str.startswith('9')) &
                            (df['celular'].apply(lambda x: str(x)[1] > '6'))
                            )
    df = df.loc[filter_celular_valido]
    return df


def remover_destinatario_duplicado(df):
    # Manter a mensagem de menor horário para destinatários repetidos.
    # destinatario = ddd+celular

    df['destinatario'] = df.apply(lambda row: f"{row['ddd']}{row['celular']}", axis=1)
    duplicated = df.loc[df["destinatario"].duplicated(keep=False)]
    max_horario = duplicated[duplicated['hora_agendamento'].values == duplicated['hora_agendamento'].max()]
    df = df.drop(max_horario.index)
    return df


def isin_black_list(destinatario):
    url = f"https://front-test-pg.herokuapp.com/blacklist/{destinatario}"
    response = requests.get(url)

    if (response.status_code == 200):
        return destinatario


def validar_black_list(df):
    # Verificar BlackList
    # remover destinatário que estiver na Black List
    # https://front-test-pg.herokuapp.com/blacklist
    # Colocar implace para ter o df processado por todas as etapas

    # black = pd.Series(isin_black_list(row.destinatario) for row in df.itertuples()).dropna()
    # black = pd.Series(np.vectorize(isin_black_list)(df['destinatario'])).dropna()
    # black = df.swifter.apply(lambda row: isin_black_list(row.destinatario), axis=1)
    black = df['destinatario'].map(isin_black_list).dropna()
    df = df.drop(black.index)
    return df


def identiticar_broker(df):
    # Identifica o Broker correspodente:
    # ID_BROKER	  OPERADORAS
    # ______________________
    #   1	      VIVO, TIM
    #   2	      CLARO, OI
    #   3	      NEXTEL

    conds = [
          (df["operadora"].str.contains("VIVO|TIM")),
          (df["operadora"].str.contains("CLARO|OI")),
          (df["operadora"].str.contains("NEXTEL"))
    ]

    actions = [1, 2, 3]
    df['id_broker'] = np.select(conds, actions)

    return df


def montar_mensagem(df):
    # Monta a mensagem de retorno
    # IDMENSAGEM;IDBROKER

    df = df[['id_mensagem', 'id_broker']]
    mensagem = df.to_csv(header=False, index=False, sep=';')
    return mensagem
