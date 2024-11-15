from flask import Flask , render_template


p = [
    {
    "Name": "Akash Maurya",
    "blog": "HEADLINE 1",
    "Created At": "April 20 2024",
    "Email": "akash@example.com",
    "City": "Mumbai"
},
{
    "Name": "Ritika Sharma",
    "blog": "TECH INSIGHTS",
    "Created At": "May 15 2024",
    "Email": "ritika@example.com",
    "City": "Delhi"
},
{
    "Name": "Arjun Verma",
    "blog": "FASHION TRENDS",
    "Created At": "June 10 2024",
    "Email": "arjun@example.com",
    "City": "Bangalore"
},
{
    "Name": "Priya Singh",
    "blog": "HEALTH TIPS",
    "Created At": "July 22 2024",
    "Email": "priya@example.com",
    "City": "Hyderabad"
},
{
    "Name": "Manish Kumar",
    "blog": "TRAVEL DIARIES",
    "Created At": "August 30 2024",
    "Email": "manish@example.com",
    "City": "Chennai"
},
{
    "Name": "Sneha Gupta",
    "blog": "COOKING RECIPES",
    "Created At": "September 18 2024",
    "Email": "sneha@example.com",
    "City": "Pune"
}

]

app = Flask(__name__)


@app.route("/")

def home():
   return "<h1>HElOO<h1> world"
@app.route('/<name>')

def user(name):
   return f'hello {name}'



if __name__ == "__main__":
   app.run()