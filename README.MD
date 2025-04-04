# CharadAPI - Uma API Simples para Charadas

Esta é uma API RESTful construída com Python e Flask, utilizando o Firebase como banco de dados para armazenar charadas (perguntas e suas respectivas respostas). O objetivo principal é fornecer uma maneira fácil de acessar e gerenciar um conjunto de charadas através de requisições HTTP.

## Índice

* [Endpoints da API](#endpoints-da-api)
* [Observações adicionais](#observações-adicionais)
* [Repositório Frontend](#repositório-frontend)

## Primeiros Passos

Para começar a usar ou executar esta API, siga estas instruções:

1.  **Pré-requisitos:**
    * Certifique-rse de ter o Python 3 instalado em sua máquina.
    * O gerenciador de pacotes pip também é necessário.

2.  **Configuração do Projeto:**
    * **Arquivo `.env`:** Crie um arquivo chamado `.env` na raiz do projeto. Nele, você precisará configurar as informações de acesso ao seu projeto Firebase. Isso inclui o conteúdo da chave privada da sua conta de serviço do Firebase em formato JSON, atribuído à variável de ambiente `CONFIG_FIREBASE`.

        ```dotenv
        CONFIG_FIREBASE='{"type": "...", "project_id": "...", ...}'
        ```

    * **Dependências:** Instale as bibliotecas necessárias executando o seguinte comando no seu terminal:

        ```bash
        pip install -r requirements.txt
        ```

        Certifique-se de ter um arquivo `requirements.txt` com as seguintes linhas:

        ```
        Flask
        Flask-CORS
        firebase-admin
        python-dotenv
        ```

    * **Configuração do Firebase Firestore:**
        * No seu projeto Firebase, acesse o Firestore e crie uma coleção chamada `charadas`. Cada documento dentro desta coleção deve representar uma charada e conter os seguintes campos:
            * `id`: Um número inteiro único para identificar a charada.
            * `charada`: A pergunta da charada (texto).
            * `resposta`: A resposta da charada (texto).

        * Além disso, crie uma coleção chamada `controle_id` com um documento chamado `contador`. Este documento deve ter um campo `id` (um número inteiro) que será usado para gerar novos IDs para as charadas adicionadas através da API. Inicialize este `id` com o próximo valor sequencial desejado para suas charadas.

3.  **Execução da API:**
    Para iniciar o servidor da API, navegue até o diretório do projeto no seu terminal e execute o seguinte comando:

    ```bash
    python app.py
    ```

    A API estará rodando localmente no endereço `http://127.0.0.1:5000/`.

## Tecnologias utilizadas

* ![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![image](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
* ![image](https://img.shields.io/badge/firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=black)

## Endpoints da API

A API CharadAPI oferece os seguintes endpoints para interagir com as charadas:

* **`GET /`**:
    * Retorna uma mensagem simples indicando que a API está online.
    * Status Code: 200 OK
    * Exemplo de resposta: `"CharadAPI tá ON! Ria!"`

* **`GET /charadas`**:
    * Retorna uma charada aleatória da coleção `charadas` no Firestore.
    * Status Code: 200 OK
    * Exemplo de resposta:
        ```json
        {
            "id": 3,
            "charada": "O que tem pescoço comprido e cabeça pequena?",
            "resposta": "A garrafa"
        }
        ```
    * Status Code: 404 Not Found: Retornado se não houver nenhuma charada cadastrada.

* **`GET /charadas/<id>`**:
    * Retorna a charada com o `id` especificado na URL.
    * Status Code: 200 OK
    * Exemplo de resposta (para `/charadas/1`):
        ```json
        {
            "id": 1,
            "charada": "O que é, o que é? Sobe e desce, mas nunca se move.",
            "resposta": "A escada"
        }
        ```
    * Status Code: 404 Not Found: Retornado se a charada com o `id` fornecido não for encontrada.

* **`POST /charadas`**:
    * Adiciona uma nova charada à coleção.
    * Os dados da nova charada devem ser enviados no corpo da requisição como JSON, contendo os campos `charada` e `resposta`.
    * Status Code: 201 Created
    * Exemplo de corpo da requisição:
        ```json
        {
            "charada": "Qual o animal que anda com as patas?",
            "resposta": "Todos"
        }
        ```
    * Exemplo de resposta:
        ```json
        {
            "mensagem": "Charada cadastrada com sucesso!"
        }
        ```
    * Status Code: 400 Bad Request: Retornado se os campos `charada` ou `resposta` estiverem faltando no corpo da requisição.

* **`PUT /charadas/<id>`**:
    * Atualiza a charada existente com o `id` especificado na URL.
    * Os dados atualizados devem ser enviados no corpo da requisição como JSON, contendo os campos `charada` e `resposta`.
    * Status Code: 201 Created
    * Exemplo de corpo da requisição:
        ```json
        {
            "charada": "O que tem boca mas não fala, tem rio mas não bebe?",
            "resposta": "O mapa"
        }
        ```
    * Exemplo de resposta:
        ```json
        {
            "mensagem": "Charada atualizada com sucesso!"
        }
        ```
    * Status Code: (implícito) 200 OK em alguns casos de sucesso.
    * Status Code: (implícito) 404 Not Found: Retornado se a charada com o `id` fornecido não for encontrada.
    * Status Code: 400 Bad Request: Retornado se os campos `charada` ou `resposta` estiverem faltando no corpo da requisição.

* **`DELETE /charadas/<id>`**:
    * Exclui a charada com o `id` especificado na URL.
    * Status Code: 200 OK
    * Exemplo de resposta:
        ```json
        {
            "mensagem": "Charada excluída com sucesso"
        }
        ```
    * Status Code: 404 Not Found: Retornado se a charada com o `id` fornecido não for encontrada.

## Observações Adicionais

* Esta API depende de uma conexão ativa com o Firebase e de uma configuração correta das credenciais.
* Atualmente, a API não implementa nenhum tipo de autenticação ou autorização. Em um ambiente de produção, é altamente recomendável adicionar medidas de segurança para proteger seus dados.
* O sistema de geração de IDs para novas charadas utiliza um contador armazenado no Firestore. É importante garantir que esta configuração inicial esteja correta para o bom funcionamento da funcionalidade de adição de charadas.

## Repositório Frontend

- Venha conhecer também meu projeto Frontend das charadas: https://github.com/Pedrao345/charadas-frontend.git