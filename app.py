from flask import Flask

from mysql_helper import mysql_helper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    print(mysql_helper)
