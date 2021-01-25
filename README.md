
# Solução para o desafio de [back-end na PGMais](https://github.com/pgmais/teste-dev)


#### Tecnologias e Ferramentas utilizadas:
* [Python 3.6.9](https://www.python.org/downloads/release/python-369/)
* [Flask](https://flask.palletsprojects.com/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [flask-apispec](https://flask-apispec.readthedocs.io/en/latest/index.html)
* [gunicorn](https://gunicorn.org/)
* [pandas](https://pandas.pydata.org/)
* [requests](https://requests.readthedocs.io/en/master/)
* [VScode](https://code.visualstudio.com/)
* [Ubuntu](https://ubuntu.com/download)
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)


#### Pré-requisitos
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)


#### Para executar:

       $ git clone https://github.com/jeffersonfragoso/message_processing.git
       $ cd message_processing
       $ docker-compose up --build --force-recreate

#### Para testar:

1. Acesse a interface do swagger no browser `http://localhost:5000/swagger-ui/`.

2. Click em Try it out.

3. Selecione o arquivo de teste `mensagens.csv` que está na raiz do projeto.

4. Click em execute e aguarde o retorno.
