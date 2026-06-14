<!DOCTYPE html>
<html>

<head>
    <title>Transações</title>
</head>

<body>

    <h1>Histórico de Transações</h1>

    <table border="1">

        <tr>
            <th>ID</th>
            <th>Tipo</th>
            <th>Descrição</th>
            <th>Valor</th>
            <th>Ações</th>
        </tr>

        % for i, t in enumerate(transacoes):

        <tr>

            <td>{{i}}</td>

            <td>{{t["tipo"]}}</td>

            <td>{{t["descricao"]}}</td>

            <td>R$ {{t["valor"]}}</td>

            <td>

                <a href="/editar_transacao/{{i}}">
                    Editar
                </a>

                |

                <a href="/excluir_transacao/{{i}}">
                    Excluir
                </a>

            </td>

        </tr>

        % end

    </table>

    <br>

    <a href="/dashboard">
        Voltar
    </a>

</body>

</html>