"""
routes.py
---------
Define os endpoints da API com FastAPI.
"""

from fastapi import APIRouter, HTTPException
from app.schemas import ProdutoCreate, ProdutoOut
from app.crud import adicionar_produto, listar_produtos
from app.utils import definir_categoria
from app.utils import gerar_codigo_seguranca

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API Filtra NCM funcionando!"}

@router.post("/produtos", response_model=ProdutoOut)
def criar_produto(produto: ProdutoCreate):
    sucesso = adicionar_produto(produto.ncm, produto.nome, produto.marca, produto.modelo)
    if not sucesso:
        raise HTTPException(status_code=400, detail="Produto já existe no banco")
    # Retorna o produto cadastrado (fictício, sem pegar ID real)
    return {
        "id": 1,
        "ncm": produto.ncm,
        "codigo_seguranca": gerar_codigo_seguranca(produto.ncm),
        "categoria": definir_categoria(produto.ncm),
        "nome": produto.nome,
        "marca": produto.marca,
        "modelo": produto.modelo
    }

@router.get("/produtos")
def obter_produtos():
    produtos = listar_produtos()
    return {"produtos": produtos}
