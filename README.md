# API de Rastreamento de Encomendas

## Descrição

### O que faz:
Uma API RESTful construída com FastAPI que permite gerenciar o rastreamento de encomendas. Possui funcionalidades para registrar uma encomenda e consultar seu status, com estrutura de banco de dados relacional integrada via SQLAlchemy.

### Com o que foi construída:
FastAPI para criação da API.

SQLAlchemy como ORM.

SQLite como banco de dados local (pode ser trocado por PostgreSQL facilmente).

Uvicorn como servidor ASGI.

Pydantic para validação de dados.

Requests para integração com API de rastreamento real.

### Por quê?
Empresas e desenvolvedores frequentemente precisam de APIs que centralizem o rastreamento de encomendas de diferentes transportadoras. Este projeto simula esse tipo de integração, sendo útil tanto como ferramenta prática quanto como prova de conceito em processos seletivos ou no portfólio.

### Instruções de Instalação

### Clone o repositório:
git clone https://github.com/seu-usuario/api-rastreamento-encomendas.git
cd api-rastreamento-encomendas

### Crie e ative um ambiente virtual (opcional, mas recomendado):

- python -m venv venv
- Ativação no Windows:
- venv\Scripts\activate
- Ativação no Linux/Mac:
- source venv/bin/activate

### Instale as dependências:
pip install -r requirements.txt

### Pré-requisitos
Python 3.10 ou superior

Git (para clonar o repositório)

Internet (caso deseje usar a API real de rastreamento)

### Instruções de Uso
Execute a aplicação:

bash
Copiar
Editar
uvicorn app.main:app --reload
Acesse a documentação interativa no navegador:

Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

Principais funcionalidades:

POST /encomendas/: Criar uma nova encomenda

GET /encomendas/{codigo_rastreamento}: Obter os dados de uma encomenda com base no código de rastreio

(Opcional) Integração com APIs de rastreamento reais (ex: Correios)
