"""
utils.py
--------
Funções auxiliares do projeto, como validação de NCM, geração de código de segurança e categorização.
"""

def gerar_codigo_seguranca(ncm: str) -> str:
    """
    Gera um código de segurança fictício baseado na soma dos dígitos do NCM.
    
    Args:
        ncm (str): NCM do produto (8 dígitos).

    Returns:
        str: Código de segurança formatado como 'CSxxx'.
    """
    soma = sum(int(digito) for digito in ncm)
    return f"CS{soma:03d}"


def definir_categoria(ncm: str) -> str:
    """
    Define categoria fictícia do produto com base nos dois primeiros dígitos do NCM.
    
    Args:
        ncm (str): NCM do produto (8 dígitos).

    Returns:
        str: Nome da categoria correspondente.
    """
    categorias = {
        "10": "Eletrônicos - Computadores",
        "11": "Eletrônicos - Smartphones",
        "12": "Eletrônicos - Acessórios",
        "13": "Eletrônicos - Áudio e Vídeo",
        "14": "Eletrônicos - Gadgets",
        "20": "Consumíveis Líquidos - Bebidas",
        "21": "Consumíveis Líquidos - Produtos de Limpeza",
        "22": "Consumíveis Líquidos - Cosméticos",
        "23": "Consumíveis Líquidos - Medicamentos",
        "30": "Comida Perecível - Carnes",
        "31": "Comida Perecível - Laticínios",
        "32": "Comida Perecível - Hortifruti",
        "33": "Comida Perecível - Pães e Bolos",
        "40": "Eletrodomésticos - Cozinha",
        "41": "Eletrodomésticos - Lavanderia",
        "42": "Eletrodomésticos - Limpeza",
        "50": "Vestuário Masculino - Camisetas",
        "51": "Vestuário Masculino - Calças",
        "52": "Vestuário Masculino - Acessórios",
        "60": "Vestuário Feminino - Blusas",
        "61": "Vestuário Feminino - Saias e Vestidos",
        "62": "Vestuário Feminino - Acessórios",
        "70": "Vestuário Infantil - Roupas",
        "71": "Vestuário Infantil - Calçados",
        "72": "Vestuário Infantil - Brinquedos Educativos",
        "80": "Calçados - Masculino",
        "81": "Calçados - Feminino",
        "82": "Calçados - Infantil",
        "90": "Brinquedos - Diversão",
        "91": "Brinquedos - Educativos",
        "00": "Outros"
    }
    return categorias.get(ncm[:2], "Outros")
