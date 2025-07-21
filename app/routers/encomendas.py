from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
from app.services.rastreamento import consultar_status_encomenda


router = APIRouter(prefix="/encomendas", tags=["Encomendas"])

# DependÊncia para a injeção do banco


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Criar encomenda
@router.post("/", response_model=schemas.Encomenda)
def criar(encomenda: schemas.EncomendaCreate, db: Session = Depends(get_db)):
    return crud.criar_encomenda(db, encomenda)


# Listar todas as encomendas
@router.get("/", response_model=list[schemas.Encomenda])
def listar(db: Session = Depends(get_db)):
    return crud.listar_encomendas(db)


# Buscar uma encomenda por ID
@router.get("/{encomenda_id}", response_model=schemas.Encomenda)
def buscar(encomenda_id: int, db: Session = Depends(get_db)):
    encomenda = crud.buscar_encomenda(db, encomenda_id)
    if not encomenda:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return encomenda

# Atualiza status manualmente(por enquanto)


@router.put("/{encomenda_id}/status")
def atualizar_status(encomenda_id: int, status: str, db: Session = Depends(get_db)):
    encomenda = crud.atualizar_status(db, encomenda_id, status)
    if not encomenda:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return {"mensagem": "Status atualizado com sucesso"}


# Deletar encomenda
@router.delete("/{encomenda_id}")
def deletar(encomenda_id: int, db: Session = Depends(get_db)):
    encomenda = crud.deletar_encomenda(db, encomenda_id)
    if not encomenda:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return {"mensagem": "Encomenda deletada"}


@router.post("/{encomenda_id}/atualizar")
def atualizar_por_rastreamento(encomenda_id: int, db: Session = Depends(get_db)):
    encomenda = crud.buscar_encomenda(db, encomenda_id)
    if not encomenda:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")

    resultado = consultar_status_encomenda(encomenda.codigo_rastreamento)

    crud.atualizar_status(db, encomenda_id, resultado["status"])

    return {
        "mensagem": "Status atualizado com sucesso",
        "novo_status": resultado["status"],
        "atualizado_em": resultado["atualizado_em"]
    }
