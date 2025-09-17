from fastapi import FastAPI
from app.routes import router as ncm_router

app = FastAPI(
    title="API Filtra NCM",
    description="API para gerenciamento fictício de NCM e produtos. Permite validar NCM, cadastrar produtos e simular categorias.",
    version="1.0.0",
)

# Rota raiz para teste da API
@app.get("/")
def root():
    """
    Rota raiz da API para teste.
    
    Retorna:
        dict: Mensagem informando que a API está online.
    """
    return {"message": "API Filtra NCM está rodando 🚀"}


# Inclui todas as rotas do módulo app.routes
app.include_router(ncm_router)
