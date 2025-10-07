from flask import Flask, url_for

app = Flask(__name__) # il name verrà sostituito con il nome del file una volta avviata l'app

'''app.run(debug = True) #  host = "127.0.0.1", port = 5000
 # se scrivo solamente app.run l'app si avvia con i parametri di default 

# In produzione è importante che il debug sia 'False'
# '''

@app.route("/")

def home() -> str:
    return "<h3> Hello, world!</h3>"

@app.route("/user/<string:username>/age/<int:age>")
def show_user_profile(username:str, age:int) -> str:
    return f"Profilo di {username}, età: {age}"

@app.route("/post/<int:post_id>")
def show_post(post_id:int) -> str:
    return f"Post {post_id}"

with app.test_request_context():
    print(url_for("home"))
    print(url_for("show_user_profile", username = "Sergio De Guidi", age = 21))
    print(url_for("show_post", post_id = 42))