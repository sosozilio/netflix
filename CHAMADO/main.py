from flask import Flask, render_template, request, session, redirect, jsonify
from flask_mysqldb import MySQL 
from flask_bcrypt import Bcrypt 
from datetime import date

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db-mysql-nyc3-13529-do-user-15782594-0.c.db.ondigitalocean.com'
app.config['MYSQL_USER'] = 'senac'
app.config['MYSQL_PASSWORD'] = 'AVNS_LLmbm2FIz247B-a25cH'
app.config['MYSQL_DB'] = 'db_sophia'
app.config['MYSQL_PORT'] = 25060

mysql = MYSQL(app)

if __name__ == '__main__':
    app.run(debug=True)

app.secret_key = 'ola brasil amado'
bcrypt = Bcrypt(app)

# Rota principal da aplicação

@app.route("/")
def login():
    return render_template('login.html', is_home = True)

# Rota da dashboard

@app.route("/")
def dashboard():
    return render_template('dashboard.html', is_home = False)

# Rota do formulário

@app.route("/consumidor/formulario")
def formulario():
    return render_template('formulario.html', is_home = False)

# Inserir registros na tabela tb_consumidor

@app.route("/consumidor/insert", methods = ['POST'])
def consumidorInsert():
     
    
 if request.method == 'POST':
     nomeDoConsumidor = request.form['nomeDoConsumidor']
     email = request.form['email']
     celular = request.form['celular']
     senha = request.form['senha']
     dataAtual = date.today()
     
     hashPassword = bcrypt.generate_password_hash(senha).decode('utf-8')
     
     cur = mysql.connection.cursor()
     cur.execute("INSERT INTO tb_consumidor (nomeDoConsumidor, email, celular, senha, created_at) VALUES(%s, %s, %s, %s, %s)",
    (nomeDoConsumidor, email, int(celular), hashPassword, dataAtual))
     mysql.connection.commit()
     
     return render_template('login.html', is_home = True, mensagem = Consumidor)
 
 # Login do usuário
 
 
    
    
