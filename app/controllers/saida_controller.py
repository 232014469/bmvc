from app.models.json_helper import (
    read_json,
    write_json
)

DATABASE = "app/controllers/database/transactions.json"


def add_saida(descricao, valor):

    dados = read_json(DATABASE)

    nova = {
        "id": len(dados) + 1,
        "tipo": "saida",
        "descricao": descricao,
        "valor": valor
    }

    dados.append(nova)

    write_json(DATABASE, dados)