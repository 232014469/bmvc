from app.controllers.application import Application
import json
import os

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

app = Bottle()
ctl = Application()

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

    # Transações
    caminho = "app/controllers/database/transactions.json"

    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            try:
                transacoes = json.load(arquivo)
            except:
                transacoes = []
    else:
        transacoes = []

    saldo = 0

    for t in transacoes:

        if t["tipo"] == "entrada":
            saldo += float(t["valor"])

        elif t["tipo"] == "saida":
            saldo -= float(t["valor"])

    # Saídas fixas
    caminho_fixas = "app/controllers/database/fixed_expenses.json"

    if os.path.exists(caminho_fixas):
        with open(caminho_fixas, "r", encoding="utf-8") as arquivo:
            try:
                fixas = json.load(arquivo)
            except:
                fixas = []
    else:
        fixas = []

    for fixa in fixas:
        saldo -= float(fixa["valor"])

    return template(
        "app/views/html/dashboard",
        saldo=saldo,
        transacoes=transacoes[-5:]
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

    caminho = "app/controllers/database/transactions.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:
            try:
                transacoes = json.load(arquivo)
            except:
                transacoes = []

    else:
        transacoes = []

    transacoes.append({
        "tipo": "entrada",
        "descricao": descricao,
        "valor": valor
    })

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            transacoes,
            arquivo,
            indent=4,
            ensure_ascii=False
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

    caminho = "app/controllers/database/transactions.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:
            try:
                transacoes = json.load(arquivo)
            except:
                transacoes = []

    else:
        transacoes = []

    transacoes.append({
        "tipo": "saida",
        "descricao": descricao,
        "valor": valor
    })

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            transacoes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    redirect('/dashboard')


# SAÍDAS FIXAS


@app.route('/fixas')
def fixas():

    user = request.get_cookie("user")

    if not user:
        redirect('/login')

    caminho = "app/controllers/database/fixed_expenses.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:

            try:
                fixas = json.load(arquivo)
            except:
                fixas = []

    else:
        fixas = []

    return template(
        "app/views/html/fixas",
        fixas=fixas
    )


@app.post('/salvar_fixa')
def salvar_fixa():

    descricao = request.forms.get('descricao')
    valor = float(request.forms.get('valor'))

    caminho = "app/controllers/database/fixed_expenses.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:

            try:
                fixas = json.load(arquivo)
            except:
                fixas = []

    else:
        fixas = []

    fixas.append({
        "descricao": descricao,
        "valor": valor
    })

    with open(caminho, "w", encoding="utf-8") as arquivo:

        json.dump(
            fixas,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    redirect('/fixas')


# TRANSAÇÕES


@app.route('/transacoes')
def transacoes():

    user = request.get_cookie("user")

    if not user:
        redirect('/login')

    caminho = "app/controllers/database/transactions.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:

            try:
                lista = json.load(arquivo)
            except:
                lista = []

    else:
        lista = []

    return template(
        "app/views/html/transacoes",
        transacoes=lista
    )


# COFRE


@app.route('/cofre')
def cofre():

    user = request.get_cookie("user")

    if not user:
        redirect('/login')

    caminho = "app/controllers/database/vault.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:

            try:
                dados = json.load(arquivo)
            except:
                dados = {"saldo": 0}

    else:
        dados = {"saldo": 0}

    return template(
        "app/views/html/cofre",
        saldo=dados["saldo"]
    )


@app.post('/depositar_cofre')
def depositar_cofre():

    valor = float(request.forms.get('valor'))

    caminho = "app/controllers/database/vault.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:

            try:
                cofre = json.load(arquivo)
            except:
                cofre = {"saldo": 0}

    else:
        cofre = {"saldo": 0}

    cofre["saldo"] += valor

    with open(caminho, "w", encoding="utf-8") as arquivo:

        json.dump(
            cofre,
            arquivo,
            indent=4
        )

    redirect('/cofre')

@app.post('/retirar_cofre')
def retirar_cofre():

    valor = float(request.forms.get('valor'))

    caminho = "app/controllers/database/vault.json"

    if os.path.exists(caminho):

        with open(caminho, "r", encoding="utf-8") as arquivo:

            try:
                cofre = json.load(arquivo)
            except:
                cofre = {"saldo": 0}

    else:
        cofre = {"saldo": 0}

    cofre["saldo"] -= valor

    with open(caminho, "w", encoding="utf-8") as arquivo:

        json.dump(
            cofre,
            arquivo,
            indent=4
        )

    redirect('/cofre')



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