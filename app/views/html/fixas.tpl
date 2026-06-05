<!DOCTYPE html>
<html>

<head>

    <title>Saídas Fixas</title>

</head>

<body>

    <h1>Saídas Fixas</h1>

    <form action="/salvar_fixa" method="post">

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

    <hr>

    <h2>Pagamentos agendados</h2>

    <ul>

        % for fixa in fixas:

            <li>

                {{fixa["descricao"]}}
                -
                R$ {{fixa["valor"]}}

            </li>

        % end

    </ul>

    <br>

    <a href="/dashboard">
        Voltar
    </a>

</body>

</html>