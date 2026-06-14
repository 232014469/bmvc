from app.controllers.application import Application

from bottle import (
    Bottle,
    run,
    request,
    static_file,
    redirect,
    response,
    template
)

from app.controllers.auth import (
    register_user,
    login_user
)

from app.models.transacao_manager import (
    TransacaoManager
)

app = Bottle()
ctl = Application()

manager = TransacaoManager()

# ARQUIVOS ESTÁTICOS

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

# LOGIN / CADASTRO

@app.route('/')
@app.route('/login')
def login():
    return ctl.render('login')


@app.route('/cadastro')
def cadastro():
    return ctl.render('cadastro')

# DASHBOARD

@app.route('/dashboard')
def dashboard():

    user = request.get_cookie("user")

    if not user:
        redirect('/login')

    return template(
        "app/views/html/dashboard",
        saldo=manager.calcular_saldo(),
        transacoes=manager.listar()[-5:]
    )

# ENTRADAS

@app.route('/entradas')
def entradas():

    user = request.get_cookie("user")

    if not user:
        redirect('/login')

    return ctl.render('entradas')


@app.post('/salvar_entrada')
def salvar_entrada():

    descricao = request.forms.get('descricao')
    valor = float(request.forms.get('valor'))

    manager.adicionar(
        "entrada",
        descricao,
        valor
    )

    redirect('/dashboard')

# SAÍDAS

@app.route('/saidas')
def saidas():

    user = request.get_cookie("user")

    if not user:
        redirect('/login')

    return ctl.render('saidas')


@app.post('/salvar_saida')
def salvar_saida():

    descricao = request.forms.get('descricao')
    valor = float(request.forms.get('valor'))

    manager.adicionar(
        "saida",
        descricao,
        valor
    )

    redirect('/dashboard')

# TRANSAÇÕES

@app.route('/transacoes')
def transacoes():

    user = request.get_cookie("user")

    if not user:
        redirect('/login')

    return template(
        "app/views/html/transacoes",
        transacoes=manager.listar()
    )

# EXCLUIR TRANSAÇÃO

@app.route('/excluir_transacao/<indice:int>')
def excluir_transacao(indice):

    manager.excluir(indice)

    redirect('/transacoes')

# EDITAR TRANSAÇÃO

@app.route('/editar_transacao/<indice:int>')
def editar_transacao(indice):

    return template(
        "app/views/html/editar_transacao",
        indice=indice,
        transacao=manager.obter(indice)
    )

# ATUALIZAR TRANSAÇÃO

@app.post('/atualizar_transacao/<indice:int>')
def atualizar_transacao(indice):

    descricao = request.forms.get('descricao')
    valor = float(request.forms.get('valor'))

    manager.atualizar(
        indice,
        descricao,
        valor
    )

    redirect('/transacoes')

# AUTENTICAÇÃO

@app.post('/cadastro')
def cadastrar():

    nome = request.forms.get('nome')
    email = request.forms.get('email')
    senha = request.forms.get('senha')

    success = register_user(
        nome,
        email,
        senha
    )

    if success:
        redirect('/login')

    return "Email já cadastrado."


@app.post('/login')
def login_submit():

    email = request.forms.get('email')
    senha = request.forms.get('senha')

    user = login_user(
        email,
        senha
    )

    if user:

        response.set_cookie(
            "user",
            user["email"]
        )

        redirect('/dashboard')

    return "Usuário ou senha inválidos."


@app.route('/logout')
def logout():

    response.delete_cookie("user")

    redirect('/login')

# SERVIDOR

if __name__ == '__main__':

    run(
        app,
        host='0.0.0.0',
        port=8080,
        debug=True
    )