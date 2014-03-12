from flask import Flask, jsonify
from checkisbn import is_valid as check_isbn

app = Flask(__name__)

@app.route('/')
def main():
    return app.send_static_file('index.html')


@app.route('/check/<isbn>')
def hello_world(isbn):
    is_valid = check_isbn(isbn)
    return jsonify({
        "isbn": isbn,
        "status": is_valid
    })


if __name__ == '__main__':
    app.debug = True
    app.run()
