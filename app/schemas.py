from pydantic import BaseModel
from datetime import datetime


class EncomendaBase(BaseModel):
    codigo_rastreamento: str
    transportadora: str


class EncomendaCreate(EncomendaBase):
    pass


class Encomenda(EncomendaBase):
    id: int
    status: str
    ultima_atualizacao: datetime

    class Config:
        orm_mode = True
