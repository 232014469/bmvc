from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response

app = Bottle()
ctl = Application()

#-----------------------------------------------------------------------------
# Rotas de Arquivos Estáticos:
# Essencial para carregar seu CSS e JS da pasta app/static/

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

#-----------------------------------------------------------------------------
# Rotas de Navegação:

@app.route('/helper')
def helper():
    """Rota original para teste do sistema."""
    return ctl.render('helper')

@app.route('/')
@app.route('/projeto')
def projeto():
    """
    Sua rota personalizada para o nível BMVC I.
    Ela chama o método render do controller passando a chave 'pagina'.
    """
    return ctl.render('pagina')

#-----------------------------------------------------------------------------
# Execução do Servidor:

if __name__ == '__main__':
    # host='0.0.0.0' permite acesso externo (importante para Docker)
    # port=8080 é a porta padrão configurada
    # debug=True recarrega o servidor automaticamente ao salvar arquivos
    run(app, host='0.0.0.0', port=8080, debug=True)