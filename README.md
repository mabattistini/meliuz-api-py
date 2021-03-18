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


**Documentação**

- Obter uma lista geral dos pokemons

    `http://0.0.0.0:5000/pokemon`

- Obter uma lista filtrada pelo nome
   
    `http://0.0.0.0:5000/pokemon/filter?name=bulbasaur,venusaur`
  
- Obter uma lista filtrada pelo tipo
    
    `http://0.0.0.0:5000/pokemon/filter?type=fire,flying`


- Criar um time 

  `curl --request POST \
    --url http://localhost:5000/team \
    --header 'content-type: application/json' \
    --data '{
      "name": "time1",
      "coach": "treinador"
  }'`

- Alterar um time
  
  `curl --request PUT \
    --url 'http://localhost:5000/team?id=1' \
    --header 'content-type: application/json' \
    --data '{
      "name": "time1",
      "coach": "treinador"
  }'`
  
- Excluir um time
  
  `curl --request DELETE \
    --url 'http://localhost:5000/team?id=1' \
    --header 'content-type: application/json'`



- Incluir um pokemon em um time

  `curl --request POST \
    --url http://localhost:5000/team/pokemon \
    --header 'content-type: application/json' \
    --data '{
      "team_id": 1,
      "pokemon_id": 8
  }'`
  

- Trocar o pokemon em um time

  `curl --request PUT \
    --url 'http://localhost:5000/team/pokemon?id=1' \
    --header 'content-type: application/json' \
    --data '{
      "pokemon_id": 100
  }'`
  
- Excluir um pokemon de um time

  `curl --request DELETE \
    --url 'http://localhost:5000/team/pokemon?id=8' \
    --header 'content-type: application/json'`
  
- Listar todos times e seus pokemons

  `curl --request GET \
    --url http://localhost:5000/team/pokemon`
  
- Listar os pokemons de um time
  
  `curl --request GET \
    --url 'http://localhost:5000/team/pokemon?team_id=1'`
  

**Evidência de testes**


 ![]('testes/pokemons/Captura de tela de 2021-03-18 15-37-50.png')
