"""
models.py
----------
Define os modelos de dados do projeto, mapeando as tabelas do SQLite.
"""

from pydantic import BaseModel

class Produto(BaseModel):
    """
    Modelo de Produto para validação de dados.
    """
    ncm: str
    codigo_seguranca: str
    categoria: str
    nome: str
    marca: str
    modelo: str
