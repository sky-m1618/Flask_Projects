from flask import Flask,redirect,url_for,render_template ,request

app = Flask(__name__)

# @app.route('/<name>')

# def Home(name):
#     return render_template('index.html',content = name,r =2)


@app.route('/')

def home():
    return "home"

@app.route('/login', methods = ['POST', 'GET'])

def login():
    if request.method == "POST":
        user = request.form["nm"]
        
        return redirect(url_for("user" ,usr = user))
    
    else:
        return render_template("login.html")
# x = open("user.csv","w")
@app.route('/<usr>')

def user(usr):
    return f"<h1> {usr} </h1>"






if __name__ == "__main__":
    app.run(debug=True)


