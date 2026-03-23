from flask import render_template, request, redirect, url_for
from app import app

user_data_list = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        age = request.form.get("age")

        if name and city and hobby and age:
            user_data = {
                "name": name,
                "city": city,
                "hobby": hobby,
                "age": age,
            }
            user_data_list.append(user_data)
            return redirect(url_for("index"))

    # передаём список ВСЕХ анкет в шаблон
    return render_template("index.html", user_data_list=user_data_list)
