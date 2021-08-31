# sudo docker build --tag ttom921/nginx-uwsgi-gevent:3.6 . --no-cache

FROM python:3.6
LABEL maintainer="s8901489@gmail.com"

# nginx

# Version of Nginx to use
ENV NGINX_VERSION nginx-1.19.10
# Install dependencies
RUN apt-get update &&  \
 	apt-get install -y wget libpcre3-dev build-essential libssl-dev zlib1g-dev ca-certificates openssl  && \
    rm -rf /var/lib/apt/lists/*

# Download and decompress Nginx
RUN mkdir -p /tmp/build/nginx && \
	cd /tmp/build/nginx && \
    wget -O ${NGINX_VERSION}.tar.gz https://nginx.org/download/${NGINX_VERSION}.tar.gz && \
	tar -zxf ${NGINX_VERSION}.tar.gz

# Build and instll Nginx
# The default puts everything under /usr/local/nginx,so it's neede to change
# it explicitly. Not jst for order but to have it in the PATH
RUN cd /tmp/build/nginx/${NGINX_VERSION} && \
    ./configure \
        --sbin-path=/usr/sbin/nginx \
		--modules-path=/usr/lib/nginx/modules \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --pid-path=/var/run/nginx/nginx.pid \
        --lock-path=/var/lock/nginx/nginx.lock \
        --http-log-path=/var/log/nginx/access.log \
        --http-client-body-temp-path=/var/cache/nginx/client_temp \
        --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \ 
        --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
        --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
		--user=www-data \
        --group=www-data \
        --with-compat \ 
        --with-file-aio \ 
		--with-pcre \
		--with-pcre-jit \
		--with-openssl-opt=no-nextprotoneg \
        --with-threads \
        --with-http_addition_module \ 
        --with-http_auth_request_module \
        --with-http_dav_module \
        --with-http_flv_module \
        --with-http_gunzip_module \ 
        --with-http_gzip_static_module \
        --with-http_mp4_module \
        --with-http_random_index_module \ 
        --with-http_realip_module \
        --with-http_secure_link_module \ 
        --with-http_slice_module \
        --with-http_ssl_module \
        --with-http_stub_status_module \ 
        --with-http_sub_module \
        --with-http_v2_module \
		--with-http_xslt_module=dynamic \
        --with-ipv6 \
		--with-stream=dynamic \
        --with-stream_realip_module \
        --with-stream_ssl_preread_module \
		--with-stream_ssl_module && \
	make -j $(getconf _NPROCESSORS_ONLN) && \
    make install && \
    mkdir /var/lock/nginx && \
    rm -rf /tmp/build

# Forward logs to Docker
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

# Remove default configuration from Nginx
#RUN rm /etc/nginx/conf.d/default.conf

# 設定nginx的pid權限
RUN mkdir -p /var/cache/nginx
RUN touch /var/run/nginx/nginx.pid \
    && chown www-data:www-data /var/run/nginx.pid \
    && chown -R www-data:www-data /var/run/nginx/nginx.pid /var/cache/nginx


EXPOSE 80 443 

CMD /usr/sbin/nginx -g "daemon off;"

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install uwsgi gevent flask --no-cache-dir \
    && rm -rf /tmp/*

# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/

# Install Supervisord                                                                                                                                                                 
RUN apt-get update && apt-get install -y supervisor \
&& rm -rf /var/lib/apt/lists/*

# Custom Supervisord config
COPY supervisord-debian.conf /etc/supervisor/conf.d/supervisord.conf

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
ENV NGINX_MAX_UPLOAD 0

# By default, Nginx will run a single worker process, setting it to auto
# will create a worker for each CPU core
ENV NGINX_WORKER_PROCESSES 1

# By default, Nginx listens on port 80.
# To modify this, change LISTEN_PORT environment variable.
# (in a Dockerfile or with an option for `docker run`)
ENV LISTEN_PORT 80


# Copy start.sh script that will check for a /app/prestart.sh script and run it before starting the app
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Copy the entrypoint that will generate Nginx additional configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Add demo app
COPY ./app /app
WORKDIR /app

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["/start.sh"]

