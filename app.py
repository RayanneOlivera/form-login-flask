from flask import Flask, render_template, request, redirect, url_for
from utils import valida_cadastro

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    # Verifica se o método de requisição é POST
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        # Verifica se o usuário e a senha são iguais a 'admin'
        if usuario == 'admin' and senha == 'admin':
            # Redireciona para a rota 'admin' se as credenciais estiverem corretas
            return redirect(url_for('admin'))
        else:
            # Redireciona para a rota 'index' se as credenciais estiverem incorretas
            return redirect(url_for('index'))
    else:
        # Renderiza o template 'login.html' se o método de requisição for GET
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Obtém os parâmetros de URL 'erro' e 'mensagem'
    erro = request.args.get("erro")
    mensagem = request.args.get("mensagem")
    # Renderiza o template 'register.html' com os parâmetros 'erro' e 'mensagem'
    return render_template('register.html', erro=erro, mensagem=mensagem)

@app.route('/register', methods=['POST'])
def register():
    # Obtém os valores dos campos do formulário
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    
    # Chama a função 'valida_cadastro' para validar os campos do formulário
    msg = valida_cadastro(nome, email, senha, confsenha)

    if msg is not None:
        # Redireciona para a rota 'signup' com o parâmetro 'erro' se a validação falhar
        return redirect(url_for('signup', erro=msg))
    
    # Se o cadastro for bem-sucedido, renderiza o template 'register.html' com a mensagem de sucesso
    return render_template('register.html', mensagem='Usuário cadastrado com sucesso!')


@app.route('/admin')
def admin():
    # Renderiza o template 'admin.html'
    return render_template('admin.html')
    
if __name__ == '__main__':
    # Executa o aplicativo Flask em modo de depuração
    app.run(debug=True)
