class Transacao:

    def __init__(
        self,
        tipo,
        descricao,
        valor
    ):
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor

    def to_dict(self):

        return {
            "tipo": self.tipo,
            "descricao": self.descricao,
            "valor": self.valor
        }

    def eh_entrada(self):
        return self.tipo == "entrada"

    def eh_saida(self):
        return self.tipo == "saida"