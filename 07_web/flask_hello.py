from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/first">Go first</a>
        <a href="/second">Go second</a>
    '''

@app.route("/first")
def first():
    return '''
        <p>first page</p>
        <a href="/">Go home</a>
    '''

@app.route("/second")    
def second():
    return '''
        <p>second page</p>
        <a href="/">Go home</a>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")