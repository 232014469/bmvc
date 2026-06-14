from bottle import template

class Application():

    def __init__(self):

        self.pages = {
            'helper': self.helper,
            'pagina': self.pagina_customizada,

            # Autenticação
            'login': self.login,
            'cadastro': self.cadastro,

            # Sistema
            'dashboard': self.dashboard,
            'entradas': self.entradas,
            'saidas': self.saidas,
            'transacoes': self.transacoes,

        }

    def render(self, page):

        content = self.pages.get(
            page,
            self.helper
        )

        return content()


    def helper(self):
        return template('app/views/html/helper')


    def pagina_customizada(self):
        return template('app/views/html/pagina')


    def login(self):
        return template('app/views/html/login')

    def cadastro(self):
        return template('app/views/html/cadastro')

    def dashboard(self, saldo=0, transacoes=[]):

        return template(
        'app/views/html/dashboard',
        saldo=saldo,
        transacoes=transacoes
    )

    def entradas(self):
        return template('app/views/html/entradas')

    def saidas(self):
        return template('app/views/html/saidas')


    def transacoes(self):
        return template('app/views/html/transacoes')
