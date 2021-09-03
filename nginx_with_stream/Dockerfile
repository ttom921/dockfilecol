# sudo docker build -f Dockerfile -t ttom921/nginx:v1.20.1_with_stream  . --no-cache
FROM debian:stretch

LABEL mantainer ="ttom <ttom921@hotmail.com>"

# Version of Nginx to use
ENV NGINX_VERSION nginx-1.20.1

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
        --sbin-path=/usr/local/sbin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --pid-path=/var/run/nginx/nginx.pid \
        --lock-path=/var/lock/nginx/nginx.lock \
        --http-log-path=/var/log/nginx/access.log \
        --http-client-body-temp-path=/tmp/nginx-client-body \
        --with-http_ssl_module \
		--with-http_stub_status_module \
		--with-http_realip_module \
		--with-ipv6 \
        --with-threads \
		--with-stream \
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

# Set up config file
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443
CMD ["nginx","-g","daemon off;"]

