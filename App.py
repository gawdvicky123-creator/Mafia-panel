from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>VICKY PANEL LIVE HAI 🔥</h1><p>Panel chal raha hai.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
