# lol-summoner-match-manager

O "lol-summoner-match-manager" é um aplicativo da web simples desenvolvido com o FastAPI e MongoDB para gerenciar o histórico de partidas de jogadores do jogo League of Legends (LoL). Ele permite que os jogadores procurem e visualizem o histórico de suas partidas, favoritem partidas específicas e excluam partidas favoritadas.

## Pré-requisitos

Antes de executar o projeto, você precisa ter as seguintes ferramentas instaladas em seu ambiente:

- Python (versão 3.7 ou superior)
- [Poetry](https://python-poetry.org/)
- MongoDB (certifique-se de que o MongoDB esteja em execução)

## Instalação

Siga estas etapas para configurar e executar o projeto em seu ambiente local:

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/seu-usuario/lol-summoner-match-manager.git
   cd lol-summoner-match-manager

2. Instale as dependências do projeto com Poetry:
   ```bash
   poetry install

3. Configure as variáveis de ambiente
    ```bash
    RIOT_API_KEY=SUA_CHAVE_DA_API_DA_RIOT
    CLUSTER_URI=SUA_URI_DO_MONGODB

4. Execute o aplicativo com:
    ```bash
    python main.py

5. Acesse o aplicativo em seu navegador:
    http://0.0.0.0:8000/

## Funcionalidades:

O aplicativo oferece as seguintes funcionalidades:

    - Pesquisa de histórico de partidas por nome de invocador.
    - Visualização de detalhes de partidas, incluindo mapa, campeão jogado, resultado e estatísticas.
    - Favoritar e desfavoritar partidas.
    - Visualização de partidas favoritadas.
    - Exclusão de partidas favoritadas.