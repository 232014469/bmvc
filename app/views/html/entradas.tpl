<!DOCTYPE html>
<html>

<head>
    <title>Nova Entrada</title>
</head>

<body>

    <h1>Nova Entrada</h1>

    <form action="/salvar_entrada" method="post">

        <input
            type="text"
            name="descricao"
            placeholder="Descrição"
            required>

        <input
            type="number"
            step="0.01"
            name="valor"
            placeholder="Valor"
            required>

        <button type="submit">
            Salvar
        </button>

    </form>

    <br>

    <a href="/dashboard">
        Voltar
    </a>

</body>

</html>