from flask import Flask
import time
app = Flask(__name__)

@app.route('/slow')
def hello_world():
    time.sleep(100000)
    return "Slow App"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
