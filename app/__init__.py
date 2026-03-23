from flask import Flask
from app import routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY не задан в .env")

app.config['SECRET_KEY'] = SECRET_KEY
