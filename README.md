Documentação Completa do Código Organizador de Arquivos
Descrição Geral
Este script Python tem como objetivo automatizar a organização de arquivos em uma pasta e suas subpastas, classificando-os de acordo com suas extensões. Ele cria novas pastas para cada tipo de extensão definido e move os arquivos correspondentes para as respectivas pastas.

Funcionalidades Principais
Leitura de uma pasta: Percorre recursivamente uma pasta e todas as suas subpastas.
Identificação de extensões: Extrai a extensão de cada arquivo.
Criação de pastas: Cria novas pastas para cada tipo de extensão definido.
Movimentação de arquivos: Move os arquivos para as pastas correspondentes às suas extensões.
Tratamento de extensões desconhecidas: Imprime uma mensagem informativa para extensões não mapeadas.
Parâmetros da Função organizar_arquivos
pasta_raiz (str): Caminho absoluto da pasta raiz onde a organização será iniciada.
Código Detalhado
Python
import os

def organizar_arquivos(pasta_raiz):
    """Organiza arquivos em pastas com base em suas extensões.

    Args:
        pasta_raiz (str): Caminho da pasta a ser organizada.

    Este método percorre recursivamente a pasta raiz e suas subpastas,
    identificando arquivos com extensões conhecidas. Para cada extensão,
    é criada uma pasta (se não existir) e os arquivos correspondentes
    são movidos para essa pasta. 

    Extensões não mapeadas são impressas no console.
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


Como Usar
Substituir o caminho da pasta: Altere o valor da variável pasta para o caminho da pasta que você deseja organizar.
Executar o script: Execute o script Python.
Personalizar:
Adicionar novas extensões: Adicione novas entradas ao dicionário extensoes.
Modificar nomes das pastas: Altere os valores das strings no dicionário extensoes.
Implementar lógica mais complexa: Para necessidades mais específicas, você pode adicionar lógica condicional ou utilizar bibliotecas externas.
Considerações
Cuidado ao executar: Antes de executar o script em uma pasta importante, faça um backup dos seus arquivos, pois a organização de arquivos pode resultar em alterações permanentes.
Tratamento de erros: Para aumentar a robustez do script, você pode adicionar blocos try-except para lidar com possíveis exceções, como permissões de arquivo ou erros de I/O.
Personalização: O script pode ser personalizado para atender a necessidades específicas, como organizar arquivos por data de criação ou por tamanho.
