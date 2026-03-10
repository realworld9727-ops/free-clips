from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/api")
def api():
    return {"message": "Free Clips backend server running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
