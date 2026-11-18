# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API simples para gerenciar itens de um catálogo usando FastAPI. Você vai praticar rotas HTTP, parâmetros de caminho, validação de dados com Pydantic e códigos de status. A API guardará os dados em memória; eles serão reiniciados quando o servidor parar.

## 📝 Tarefas

### 🛠️ Criar a aplicação e listar itens

#### Descrição

Configure a aplicação FastAPI e crie rotas para confirmar que a API está funcionando e para consultar todos os itens do catálogo.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI chamada `app`.
- Implementar `GET /` com uma mensagem de boas-vindas em JSON.
- Implementar `GET /items` para retornar a lista inicial de itens em JSON.

### 🛠️ Consultar um item

#### Descrição

Adicione uma rota que permita buscar um item específico pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Implementar `GET /items/{item_id}` usando um parâmetro de caminho inteiro.
- Retornar o item correspondente quando ele existir.
- Retornar uma resposta HTTP `404` quando não houver item com esse identificador.

### 🛠️ Cadastrar um item

#### Descrição

Permita que clientes enviem dados em JSON para adicionar um novo item ao catálogo.

#### Requisitos

O programa concluído deve:

- Definir um modelo Pydantic com os campos `name` e `description`, ambos textos.
- Implementar `POST /items` para receber e validar os dados do novo item.
- Atribuir ao item um identificador único e adicioná-lo à lista em memória.
- Retornar o item criado com o código de status HTTP `201`.

Instale as dependências listadas em `requirements.txt` e inicie o servidor com `uvicorn starter-code:app --reload`. Use `http://127.0.0.1:8000/docs` para testar as rotas pela documentação interativa do FastAPI.
