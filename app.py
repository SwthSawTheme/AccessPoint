from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

# Simulação de base de dados (apenas para teste)
users = {} # {'username': 'password'}
items = [] # [{'name': 'item', 'quantity': 2, 'value': 10.5}]

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

# Rota para cadastro de itens
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "Usuário ja existe", 409
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

