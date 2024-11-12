from flask import Flask
from datetime import datetime
import subprocess
import pwd
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Ankit Rajput"  
    username = "r-ajputankit"
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    <html>
        <head><title>HTOP Endpoint</title></head>
        <body>
            <h1>HTOP Data</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time in IST:</strong> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=6000)
