<!DOCTYPE html>
<html>

<head>
    <title>Cofre</title>
</head>

<body>

    <h1>Cofre</h1>

    <h2>Saldo do Cofre</h2>

    <h3>R$ {{saldo}}</h3>

    <hr>

    <form action="/depositar_cofre" method="post">

        <input
            type="number"
            step="0.01"
            name="valor"
            placeholder="Valor para depositar"
            required>

        <button type="submit">
            Depositar
        </button>

    </form>

    <br>

    <form action="/retirar_cofre" method="post">

        <input
            type="number"
            step="0.01"
            name="valor"
            placeholder="Valor para retirar"
            required>

        <button type="submit">
            Retirar
        </button>

    </form>

    <br>

    <a href="/dashboard">
        Voltar
    </a>

</body>

</html>