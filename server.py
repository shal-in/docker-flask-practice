from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'this is a test index page'

@app.route('/second')
def second():
    return 'this is a test second page'

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=8080)
