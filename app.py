from flask import Flask
import os
import socket
import _mysql

app = Flask(__name__)

@app.route("/")
def hello():
    try:
    	db =_mysql.connect(host="test.ce1eimqaujzw.us-west-1.rds.amazonaws.com", user="test", passwd="testtest", port=3306, db="test")
    	visits = "connected to mysql"
    except Exception as e:
        visits = e

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)