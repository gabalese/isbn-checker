from flask import Flask, jsonify, make_response
import os
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
    port = int(os.environ.get("PORT", 5000))  # Required by Heroku
    app.debug = True
    app.run(host="0.0.0.0", port=port)
