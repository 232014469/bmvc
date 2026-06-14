import json
import os


class TransacaoManager:

    def __init__(self):

        self.caminho = (
            "app/controllers/database/transactions.json"
        )

    def carregar(self):

        if os.path.exists(self.caminho):

            with open(
                self.caminho,
                "r",
                encoding="utf-8"
            ) as arquivo:

                try:
                    return json.load(arquivo)

                except:
                    return []

        return []

    def salvar(self, dados):

        with open(
            self.caminho,
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    def adicionar(self, tipo, descricao, valor):

        transacoes = self.carregar()

        transacoes.append({
            "tipo": tipo,
            "descricao": descricao,
            "valor": valor
        })

        self.salvar(transacoes)

    def listar(self):

        return self.carregar()

    def excluir(self, indice):

        transacoes = self.carregar()

        if indice < len(transacoes):

            transacoes.pop(indice)

            self.salvar(transacoes)

    def atualizar(
        self,
        indice,
        descricao,
        valor
    ):

        transacoes = self.carregar()

        if indice < len(transacoes):

            transacoes[indice]["descricao"] = descricao

            transacoes[indice]["valor"] = valor

            self.salvar(transacoes)

    def calcular_saldo(self):

        saldo = 0

        for t in self.carregar():

            if t["tipo"] == "entrada":

                saldo += float(t["valor"])

            else:

                saldo -= float(t["valor"])

        return saldo

    def obter(self, indice):

        transacoes = self.carregar()

        if indice < len(transacoes):

            return transacoes[indice]

        return None