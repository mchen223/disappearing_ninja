from flask import Flask, render_template, request, redirect, Markup
app = Flask(__name__)
app.secret_key = 'SecretClubhousePassword'

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/ninja/')
def ninjas():
    ninja = Markup('<img src="{{ url_for("static", filename="img/TMNT.png") }}" alt="TMNT">')
    return render_template("result.html", ninja=ninja)

@app.route('/ninja/<color>')
def ninja(color):
   ninja = Markup('<img src="{{ url_for("static", filename="img/' + color + '.jpg") }}" alt src="{{ url_for("static", filename="img/april.jpg") }}">')
   return render_template("result.html", ninja=ninja)

app.run(debug=True)
