from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    output = "hello world"
    return render_template('index.html', title='hello2', output=output)

if __name__ == "__main__":
    app.run(debug=False, port=8888, threaded=True)  
