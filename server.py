import os
from flask import Flask, render_template, send_file


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def sub_folder(path):
    try:
        return send_file(path)
    except Exception as e:
        print(e)
        return f"Couldn't find file {path}."


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000), debug=True)