from pyscript import document

def sign_up(e):
    username = document.getElementById("username_input").value
    password = document.getElementById("password_input").value
    result = document.getElementById("result1")

    if username == "admin" and password == "676767":
        result.innerHTML = "<b>Success</b>"
    elif password != "676767":
        result.innerHTML = "Invalid password"
    else:
        result.innerHTML = "Wrong username"


