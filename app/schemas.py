"""
schemas.py
----------
Define os schemas Pydantic para entrada e saída de dados na API.
"""

from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    """
    Schema para criar um novo produto.
    """
    ncm: str = Field(..., min_length=8, max_length=8, description="NCM com 8 dígitos")
    nome: str
    marca: str
    modelo: str

class ProdutoOut(BaseModel):
    """
    Schema para retornar informações de produtos.
    """
    id: int
    ncm: str
    codigo_seguranca: str
    categoria: str
    nome: str
    marca: str
    modelo: str
