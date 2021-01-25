FROM python:3.8-slim

WORKDIR /src
ENV PYTHONPATH "${PYTONPATH}:/src/"
COPY ./application/requirements.txt /src/application/requirements.txt
RUN pip3 install -r ./application/requirements.txt
COPY . .

EXPOSE 5000

CMD ["gunicorn", "-c", "application/config.py", "application:app"]