#!/bin/bash


# run server
if [ $GEVENT = "1" ]; then 
    echo 'Run Gevent'
    /usr/local/bin/uwsgi uwsgi_g.ini
else
    echo 'Run Threading'
    /usr/local/bin/uwsgi uwsgi.ini
fi

