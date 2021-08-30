# sudo docker build -f Dockerfile -t webfms:python3.6  . --no-cache

# 使用自制的 Python 執行環境作為基本的 Docker 影像
FROM ttom921/nginx-uwsgi-gevent:3.6

# Custom Supervisord config
COPY resources/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# install pip modules
RUN pip install flask PyYAML pynng
COPY resources/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Add demo app
COPY ./app /app
WORKDIR /app

# 讓 80 連接埠可以從 Docker 容器外部存取
EXPOSE 80

# Expose 443, in case of LTS / HTTPS
EXPOSE 443

# 定義環境變數
# ENV NAME World

# 當 Docker 容器啟動時，自動執行 app.py
# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["/start.sh"]

