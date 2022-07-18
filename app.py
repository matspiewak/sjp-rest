from markupsafe import escape
from flask import Flask
from word_request import request_word

app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/word/<word>')
def get_word(word):  # put application's code here
    data = request_word(escape(word))
    return data


if __name__ == '__main__':
    app.run()
