from bottle import template

class Application():

    def __init__(self):
        # O dicionário mapeia o nome da página (string) para o método da classe
        self.pages = {
            'helper': self.helper,
            'pagina': self.pagina_customizada  # Chave usada na rota /projeto
        }

    def render(self, page):
        """
        Busca o método no dicionário 'pages'. 
        Se não encontrar a chave, carrega o 'helper' por padrão.
        """
        content = self.pages.get(page, self.helper)
        return content()

    def helper(self):
        """Renderiza o template de ajuda (exemplo da sala de aula)."""
        return template('app/views/html/helper')

    def pagina_customizada(self):
        """
        Renderiza a sua página personalizada para o nível BMVC I.
        Certifique-se de que o arquivo 'pagina.tpl' existe em app/views/html/
        """
        return template('app/views/html/pagina')