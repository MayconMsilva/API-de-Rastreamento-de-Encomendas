from fastapi import FastAPI
from app.routers import encomendas
from app.database import Base, engine
from app import models


app = FastAPI(title="API de Rastreamento de Encomendas")


# Inclui as rotas do módulo de encomendas
app.include_router(encomendas.router)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
