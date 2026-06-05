<!DOCTYPE html>
<html>

<head>

    <title>Login</title>

    <link rel="stylesheet" href="/static/css/login.css">

</head>

<body>

    <div class="container">

        <div class="left-panel">

            <h1>Controle Financeiro</h1>

            <p>
                Organize suas entradas,
                saídas e acompanhe sua
                saúde financeira.
            </p>

        </div>

        <div class="right-panel">

            <h2>Entrar</h2>

            <form action="/login" method="post">

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
                    Entrar
                </button>

            </form>

            <div class="link-cadastro">

                <a href="/cadastro">
                    Criar conta
                </a>

            </div>

        </div>

    </div>

</body>

</html>