#Gunicorn Configs
bind = "00000:5000"
workers = 3
timeout = 60
keepalive = 24 * 60 * 60  # 1 day
threads = 3