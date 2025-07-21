from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Encomenda(Base):
    __tablename__ = "encomendas"

    id = Column(Integer, primary_key=True, index=True)
    codigo_rastreamento = Column(
        String, unique=True, index=True, nullable=False)
    transportadora = Column(String, nullable=False)
    status = Column(String, default="pendente")
    ultima_atualização = Column(DateTime, default=datetime.utcnow)
