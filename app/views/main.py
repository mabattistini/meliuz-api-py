from flask import Blueprint

main_view = Blueprint('main_view', __name__)


@main_view.route(rule='/', methods=['GET'])
def main():
    html = ''
    html += '<html>'
    html += '<body>'
    html += '<h1>Webservice</h1>'
    html += '<h3>Teste Meliuz</h3>'
    html += '<a href="https://github.com/mabattistini/meliuz-api-py/blob/master/README.md">Instruções</a>'
    html += '</body>'
    html += '</html>'

    return html
