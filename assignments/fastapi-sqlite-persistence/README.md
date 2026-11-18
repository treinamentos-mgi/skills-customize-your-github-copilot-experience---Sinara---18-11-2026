# 📘 Atividade: Persistência de Dados com FastAPI e SQLite

## 🎯 Objetivo

Atualize uma API de catálogo para guardar seus itens em um banco SQLite, em vez de mantê-los apenas na memória. Você vai praticar operações básicas de banco de dados e conectar consultas SQL a rotas do FastAPI. O módulo `sqlite3` já faz parte do Python, então não precisa ser instalado separadamente.

## 📝 Tarefas

### 🛠️ Consultar itens salvos

#### Descrição

Use a tabela `items` criada no código inicial para implementar rotas que consultem o banco de dados.

#### Requisitos

O programa concluído deve:

- Implementar `GET /items` para retornar todos os itens armazenados no SQLite como JSON.
- Implementar `GET /items/{item_id}` para buscar um item pelo identificador.
- Retornar o código HTTP `404` quando o identificador não existir.
- Fechar as conexões com o banco após cada operação.

### 🛠️ Salvar novos itens

#### Descrição

Implemente a rota que recebe os dados de um item e os grava no banco, para que continuem disponíveis após reiniciar o servidor.

#### Requisitos

O programa concluído deve:

- Usar o modelo Pydantic `ItemCreate` para validar os campos `name` e `description`.
- Implementar `POST /items` e inserir os dados na tabela SQLite.
- Usar parâmetros na consulta SQL para enviar os valores, sem montar a consulta concatenando strings.
- Retornar o item criado, incluindo seu identificador, com o código HTTP `201`.
- Manter o item salvo após parar e iniciar novamente o servidor.

Instale as dependências de `requirements.txt` e inicie o servidor com `uvicorn starter-code:app --reload`. Teste as rotas em `http://127.0.0.1:8000/docs`. O arquivo `items.db` será criado na pasta da atividade.
