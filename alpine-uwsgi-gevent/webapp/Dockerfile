# 使用基礎映象庫
FROM ttom/nginx_uwsgi_py3:alpine3.9
 
# 创建工作路径
RUN mkdir /app
 
# 指定容器启动时执行的命令都在app目录下执行
WORKDIR /app
 
# 替换nginx的配置
COPY nginx.conf /etc/nginx/nginx.conf
 
# 将本地app目录下的内容拷贝到容器的app目录下
COPY ./app/ /app/
 
# pip读取requirements.txt内容安装所需的库
RUN pip install --no-cache-dir -r /app/requirements.txt 
# 启动nginx和uwsgi
ENTRYPOINT nginx -g "daemon on;" && uwsgi --ini /app/uwsgi.ini
