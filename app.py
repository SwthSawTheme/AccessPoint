from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

users = {}
items = []

# Rota para login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('item'))
        return "Login inválido", 403
    return render_template('login.html')
