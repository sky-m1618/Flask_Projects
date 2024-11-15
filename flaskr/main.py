from flask import Flask, request , render_template,flash,redirect,url_for
from forms import RegistrationForm, loginForm


posts = [
            {
                "name": "Akash Maurya",
                "HeadLine" : "from Varanasi",

            },
            {
                "name": "ks soijs",
                "HeadLine" : "from delhi",
            },
            {
                "name": "Maurya",
                "HeadLine" : "from kolkata",
            }
]

app = Flask(__name__)
app.debug = True


app.config['SECRET_KEY'] ='a8a6d20a89a34af6132c88e098203612'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def Home():
    return render_template('home1.html', posts = posts)

@app.route('/register', methods = ["GET","POST"])

def register():
    form =  RegistrationForm()
    if form.validate_on_submit():

        flash(f'Acount Created for {form.username.data}!','sucess')
        return redirect(url_for('home'))
    return render_template('registration.html',form = form)

@app.route('/login')

def login():
    form =  loginForm()
    return render_template('login.html',form = form)

if __name__ == '__main__':
    app.run()