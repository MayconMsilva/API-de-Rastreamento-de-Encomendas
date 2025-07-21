from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


# Criar uma nova encomenda
def criar_encomenda(db: Session, encomenda: schemas.EncomendaCreate):
    db_encomenda = models.Encomenda(
        codigo_rastreamento=encomenda.codigo_rastreamento,
        transportadora=encomenda.transportadora
    )

    db.add(db_encomenda)
    db.commit()
    db.refresh(db_encomenda)
    return db_encomenda


# Buscar todas as encomendas
def listar_encomendas(db: Session):
    return db.query(models.Encomenda).all()

# Buscar encomenda por ID


def buscar_encomenda(db: Session, encomenda_id: int):
    return db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()

# Atualiza status de uma encomenda


def atualizar_status(db: Session, encomenda_id: int, novo_status: str):
    encomenda = buscar_encomenda(db, encomenda_id)
    if encomenda:
        encomenda.status = novo_status
        encomenda.ultima_atualizacao = datetime.utcnow()
        db.commint()
        db.refresh(encomenda)
    return encomenda


# Deletar encomenda
def deletar_encomenda(db: Session, encomenda_id: int):
    encomenda = buscar_encomenda(db, encomenda_id)
    if encomenda:
        db.delete(encomenda)
        db.commit()
    return encomenda
