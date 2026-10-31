from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

from app import app

def test_home_returns_200():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200