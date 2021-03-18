# Meiliuz - API

#### Desenvolvido por:  Marcelo Battistini - mabattistini@gmail.com

programming language: Python

**Instruções de instalação:**

1. Clonar o respositório

`git clone https://github.com/mabattistini/meliuz-api-py.git`

2. Executar o shell script install.sh

`./install.sh`

3. Para Instanciar o serviço

`venv/bin/python /desenv/meliuz/meliuz-api-py/main.py`

**observações**

- Persisti os dados do json em um banco sqlite
Usei para acesso o SqlAlchemy, tive problemas 
coma a versão mais atual, não criava o arquivo,
resolvi instalando uma versão anterior.

- A configuração do app está no arquivo config.py

- Agrupei os fontes em pastas distintas como models, controllers e views 
para facilitar a manutenção  posterior.

- O Shell-script install.sh cria o ambiente virtual, realiza o migrate dos models
e popula as tabelas como fonte o json dos pokemons.

- Queria usar o marshmallow para serializar os dados, mas também
encontrei algumas dificuldades com a versão, então devido ao tempo
acabei fazendo a serialização na mão.



