from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

secret_key = os.getenv("SECRET_KEY")
if secret_key is None:
    raise ValueError("SECRET_KEY не задан в .env")

app.config["SECRET_KEY"] = secret_key

# ВАЖНО: импорт маршрутов В КОНЦЕ файла
from app import routes  # именно так, чтобы index был зарегистрирован
