from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_env_string():
    return f(34.5)

def f(x):
    return str(2*x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8121)
