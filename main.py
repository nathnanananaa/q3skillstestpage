from pyscript import document

def sign_up(e):
    username = document.getElementById("username_input").value
    password = document.getElementById("password_input").value
    #these codes gets the input from the html
    result = document.getElementById("result1")
    #this is for the result

    if username == "admin" and password == "676767":
        result.innerHTML = "<b>Success</b>"
    #this if statement makes sure that the username is = admin and the password is 676767
    elif password != "676767":
        result.innerHTML = "Invalid password"
    else:
        result.innerHTML = "Wrong username"

    #if the password and or username isnt equal to admin or 676767 it shows invalid password or wrong username



