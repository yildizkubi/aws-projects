from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def head():
    return 'Hello :)'

@app.route('/second')
def second():
    return 'This is second page'

@app.route('/third')
def third():
    return 'And this is 3rd page'

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'ID of this page is {id}'


if __name__ == '__main__':
    app.run(debug=True, port=8081)
    # app.run(host= '0.0.0.0', port=8081)