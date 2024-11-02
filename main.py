import os

def organizar_arquivos(pasta_raiz):
    """Organiza arquivos em pastas com base em suas extensões.

    Args:
        pasta_raiz (str): Caminho da pasta a ser organizada.
    """

    extensoes = {
        ".pdf": "PDF",
        ".docx": "Documentos",
        ".xlsx": "Planilhas",
        ".jpg": "Imagens",
        ".png": "Imagens"
    }

    for raiz, diretorios, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            extensao = os.path.splitext(arquivo)[1]

            if extensao in extensoes:
                pasta_destino = os.path.join(raiz, extensoes[extensao])
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                os.rename(caminho_completo, os.path.join(pasta_destino, arquivo))
            else:
                print(f"Extensão não mapeada: {extensao}")

# Exemplo de uso:
pasta = "C:/Users/SeuNome/Downloads"  # Substitua pelo caminho da sua pasta
organizar_arquivos(pasta)