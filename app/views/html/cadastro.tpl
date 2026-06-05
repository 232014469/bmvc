<!DOCTYPE html>
<html>

<head>
    <title>Cadastro</title>

    <link rel="stylesheet" href="/static/css/cadastro.css">
</head>

<body>

    <div class="container">

        <div class="left-panel">

            <h1>Controle Financeiro</h1>

            <p>
                Crie sua conta e comece
                a organizar sua vida financeira.
            </p>

        </div>

        <div class="right-panel">

            <h2>Criar Conta</h2>

            <form action="/cadastro" method="post">

                <input
                    type="text"
                    name="nome"
                    placeholder="Nome"
                    required>

                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    required>

                <input
                    type="password"
                    name="senha"
                    placeholder="Senha"
                    required>

                <button type="submit">
                    Cadastrar
                </button>

            </form>

            <div class="link-cadastro">

                <a href="/login">
                    Já possui conta? Entrar
                </a>

            </div>

        </div>

    </div>

</body>

</html>