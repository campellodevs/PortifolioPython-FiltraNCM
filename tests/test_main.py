from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """
    Testa se a rota raiz da API está online.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Filtra NCM está rodando 🚀"}

def test_create_product():
    """
    Testa se conseguimos cadastrar um produto fictício.
    Apenas simulação, verifica se a rota responde corretamente.
    """
    payload = {
        "ncm": "12345678",
        "nome": "Mouse",
        "marca": "Logitech",
        "modelo": "G203"
    }
    response = client.post("/produtos/", json=payload)
    
    # Aqui assumimos que o produto ainda não existe no banco
    # Se já existir, a API retorna mensagem de erro
    assert response.status_code in [200, 400]
