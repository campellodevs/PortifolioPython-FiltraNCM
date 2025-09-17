# Filtra NCM 🚀

**Filtra NCM** é um sistema desenvolvido em **Python** com **FastAPI** e **SQLite**, pensado para resolver um problema real do dia a dia: validar NCMs e gerenciar produtos em comércios e varejos. Ele transforma tarefas repetitivas em processos rápidos, confiáveis e intuitivos, mesmo para quem não tem conhecimento técnico.

---

## 🌟 Funcionalidades Atuais

- Validação de **NCM com 8 dígitos obrigatórios**  
- Geração automática de **código de segurança fictício**  
- Classificação de produtos em **30 categorias**  
- Cadastro único de produtos no banco (sem duplicidade)  
- CRUD completo (Create, Read, Update, Delete)  
- Testes unitários com **pytest**  
- Documentação interativa da API via **Swagger**  
- Banco de dados **SQLite** integrado  

---

## 🔮 Funcionalidades Futuras

- **Dashboard interativo** mostrando:  
  - Quantidade de produtos por categoria  
  - Produtos mais cadastrados  
  - Relatórios de entradas e saídas  
- **Filtros de busca avançados** para localizar produtos por:  
  - NCM  
  - Categoria  
  - Marca ou modelo  
- **Integração com Front-End** para visualização mais amigável  
- **Gráficos comparativos** e estatísticas sobre o inventário  

---

## 🛠 Tecnologias

- **Python 3.13**  
- **FastAPI**  
- **SQLite3**  
- **Pydantic** (validação de dados)  
- **Uvicorn** (servidor ASGI)  
- **pytest** (testes automatizados)  
- **Postman** (teste das rotas da API)  

---

## 📁 Estrutura do Projeto

```text
filtra_ncm/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── utils.py
├── database/
│   └── database.db
├── tests/
│   └── test_main.py
├── venv/
├── README.md
└── requirements.txt
