import os
import shutil

pasta = input("Digite o caminho da pasta que deseja organizar: ")
arquivos = os.listdir(pasta)

categorias = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".pptx": "Apresentacoes",
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".zip": "Compactados",
    ".exe": "Instaladores",
    ".msi": "Instaladores",
    ".msix": "Instaladores",
}

relatorio = []

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho_completo):
        continue

    nome, extensao = os.path.splitext(arquivo)
    if extensao in categorias:
        destino = categorias[extensao]
        pasta_destino = os.path.join(pasta, destino)

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        shutil.move(caminho_completo, pasta_destino)
        print(f"{arquivo} foi movido para a pasta {destino}")
        relatorio.append(f"{arquivo} -> {destino}")
    else:
        print(f"{arquivo} não tem categoria definida")
        relatorio.append(f"{arquivo} -> sem categoria (não movido)")

caminho_relatorio = os.path.join(pasta, "relatorio.txt")
with open(caminho_relatorio, "w", encoding="utf-8") as arquivo_relatorio:
    arquivo_relatorio.write("Relatorio de organizacao de arquivos\n")
    arquivo_relatorio.write("=" * 40 + "\n\n")
    for linha in relatorio:
        arquivo_relatorio.write(linha + "\n")

print(f"\nRelatorio salvo em: {caminho_relatorio}")