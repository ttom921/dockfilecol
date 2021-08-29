from gevent import monkey
monkey.patch_all()

from time import sleep
from flask import Flask, jsonify


app = Flask(__name__)
# app.debug = True


@app.route('/long-polling')
def long_polling():
    i = 0
    while True:
        if i == 2:
            return jsonify({'error': 0})
        else:
            i += 1
            sleep(3)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
