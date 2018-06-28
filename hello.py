from flask import Flask
import atexit
import os
import json
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
