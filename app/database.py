"""
database.py
----------
Responsável pela conexão com o banco SQLite e criação das tabelas.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "database" / "database.db"

def get_connection():
    """
    Cria e retorna uma conexão com o banco SQLite.
    """
    return sqlite3.connect(DB_PATH)

def create_tables():
    """
    Cria as tabelas necessárias para o projeto Filtra NCM.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ncm TEXT NOT NULL,
        codigo_seguranca TEXT NOT NULL,
        categoria TEXT NOT NULL,
        nome TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        UNIQUE(ncm, nome, marca, modelo)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tabelas criadas com sucesso!")
