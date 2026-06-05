<!DOCTYPE html>
<html>

<head>
    <title>Nova Saída</title>
</head>

<body>

    <h1>Nova Saída</h1>

    <form action="/salvar_saida" method="post">

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