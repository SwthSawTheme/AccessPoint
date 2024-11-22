from flask import Flask, render_template, request, redirect,url_for,flash

app = Flask(__name__)
app.secret_key = 'chave_secreta'

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
        flash("Usuário ou senha inválidos. Tente novamente.")
        return redirect(url_for('login'))
    return render_template('login.html')

# Rota para cadastro de itens
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash("Usuário já registrado!")
            return redirect(url_for('register'))
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

# Rota para cadastro de itens
@app.route('/item', methods=['GET','POST'])
def item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        value = float(request.form['value'])
        items.append({'name': name, 'quantity': quantity, 'value': value})
        return "Item cadastrado com sucesso!"
    return render_template('item.html')

if __name__ == '__main__':
    app.run(debug=True)