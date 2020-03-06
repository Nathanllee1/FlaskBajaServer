from flask import Flask, request, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/api/graphs')
def graphData():
    return('graph api')

@app.route('/api/table')
def tableData():
    return('table')

if __name__ == '__main__':
    app.run(debug=True)
