from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/analisa-data-aziz')
def analisa_data():
    return 'Ini data data aziz'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)