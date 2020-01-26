from flask import Flask, render_template

from mysql_helper import mysql_helper

app = Flask(__name__)

#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/musician')
def index():
    return render_template('musician.html')

if __name__ == '__main__':
    app.run()
    print(mysql_helper)
