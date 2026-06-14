<!DOCTYPE html>
<html>

<head>
    <title>Editar Transação</title>
</head>

<body>

    <h1>Editar Transação</h1>

    <form action="/atualizar_transacao/{{indice}}" method="post">

        <p>Tipo: {{transacao["tipo"]}}</p>

        <input
            type="text"
            name="descricao"
            value="{{transacao['descricao']}}"
            required>

        <br><br>

        <input
            type="number"
            step="0.01"
            name="valor"
            value="{{transacao['valor']}}"
            required>

        <br><br>

        <button type="submit">
            Salvar Alterações
        </button>

    </form>

    <br>

    <a href="/transacoes">
        Cancelar
    </a>

</body>

</html>