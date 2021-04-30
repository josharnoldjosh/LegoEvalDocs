import os
from flask import Flask, render_template, send_file


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')

@app.route('/<item>')
def files(item):
    try:
        return send_file(item)
    except:
        return f"Couldn't find file {item}."

if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))