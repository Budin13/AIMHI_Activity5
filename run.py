from flask import render_template, jsonify, request, session, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint
from app.models import UserData, import_models
from app import app, SWAGGER_URL, API_URL, db


app.secret_key = "random"

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "To Do List"},  # Swagger UI config overrides
)
app.register_blueprint(
    swaggerui_blueprint,
    url_prefix=SWAGGER_URL,
)


@app.route("/home")
@app.route("/")
def home():
    if session.permanent:
        return render_template("welcome.html", data=session["username"])
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.permanent = False
    return redirect(url_for("home"))


@app.route("/login", methods=["PUT", "GET"])
def login():
    if session.permanent and request.method != "PUT":
        return render_template("welcome.html", data=session["username"])

    else:
        data = request.json
        print(data)
        email = data.get("Email")
        password = data.get("Password")
        user = UserData.sample.query.filter_by(
            User_Email=email, User_Password=password
        ).first()
        print(user)

        if user:
            session["username"] = user.User_Name
            session.permanent = True
            return jsonify(success=True)
        else:
            return jsonify(success=False)


@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        data = request.json
        name = data.get("Name")
        email = data.get("Email")
        password = data.get("Password")

        user = (
            UserData.sample.query.filter_by(User_Email=email).first()
            or UserData.sample.query.filter_by(User_Name=name).first()
        )
        print(user)

        if user:
            return jsonify(success=True)
        else:
            data = UserData.sample(
                User_Email=email, User_Name=name, User_Password=password
            )
            db.session.add(data)
            db.session.commit()
            return jsonify(success=False)
    else:
        return render_template("add.html")


@app.route("/delete_user", methods=["DELETE", "GET"])
def delete_user():
    if request.method == "DELETE":
        data = request.json
        print(data)
        name = data.get("Name")
        user = UserData.sample.query.filter_by(User_Name=name).first()
        print(user)

        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify(success=True)
        else:
            return jsonify(success=False)
    else:
        return render_template("delete.html")


def configure():
    import_models()
    UserData.sample()


configure()

if __name__ == "__main__":
    app.run(debug=True)
