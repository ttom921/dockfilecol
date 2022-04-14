FROM centos:7
LABEL maintainer=ttom<ttom921@hotmail.com> description="MairaDB Base Image"

COPY mariadb.repo /etc/yum.repos.d/mariadb.repo

RUN groupadd -r mysql \
    && useradd -r -g mysql mysql \
    && yum clean all \
    && yum makecache \
    && yum install -y epel-release \
    && yum install -y telnet socat pv \
       MariaDB-server MariaDB-client MariaDB-backup \
    && yum clean all \
    && rm -rf /var/cache/yum \
    && rm -rf /var/lib/mysql/* 

ENV TERM=linux \
    base_dir=/data/mariadb-galera

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["mysqld_safe"]
