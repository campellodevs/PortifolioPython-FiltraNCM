"""
crud.py
-------
Funções CRUD (Create, Read) para manipulação de produtos no banco SQLite.
"""

from app.database import get_connection
from app.utils import gerar_codigo_seguranca, definir_categoria

def adicionar_produto(ncm: str, nome: str, marca: str, modelo: str):
    """
    Adiciona um novo produto ao banco. Retorna True se inserido, False se já existir.
    """
    codigo = gerar_codigo_seguranca(ncm)
    categoria = definir_categoria(ncm)

    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO produtos (ncm, codigo_seguranca, categoria, nome, marca, modelo)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (ncm, codigo, categoria, nome, marca, modelo))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

def listar_produtos():
    """
    Retorna todos os produtos cadastrados no banco.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos
