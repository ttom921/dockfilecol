FROM alpine:3.9.3

RUN apk add --no-cache --update \
  nginx \
  python3 \
  python3-dev \
  py3-gevent \
  uwsgi \
  uwsgi-python3 \
  uwsgi-http \
  uwsgi-gevent3

# 升級pip，這一步同時會在/usr/bin/目錄下生成pip可執行檔案
RUN pip3 install --no-cache-dir --upgrade pip

# 建立軟連結
RUN ln -s /usr/bin/python3 /usr/bin/python

CMD ["sh"]                                                                                                                       
