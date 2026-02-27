from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return f"""
    <h1>Hello! This is a simple Flask app running in a container.!</h1>
    <p><strong>Hostname:</strong> {hostname}</p>
    <p><strong>IP Address:</strong> {ip_address}</p>
    <p><strong>Current Time:</strong> {current_time}</p>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)