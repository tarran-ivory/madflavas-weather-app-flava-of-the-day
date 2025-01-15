from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Madflavas Weather App: Flava of the Day!"

if __name__ == '__main__':
    app.run(debug=True)