import os
import shutil
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

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

enviar_email = input("\nDeseja enviar o relatorio por e-mail? (s/n): ")

if enviar_email.lower() == "s":
    load_dotenv()

    email_remetente = os.getenv("EMAIL_REMETENTE")
    email_senha = os.getenv("EMAIL_SENHA")
    email_destinatario = os.getenv("EMAIL_DESTINATARIO")

    corpo_email = "\n".join(relatorio)

    mensagem = EmailMessage()
    mensagem["Subject"] = "Relatorio de organizacao de arquivos"
    mensagem["From"] = email_remetente
    mensagem["To"] = email_destinatario
    mensagem.set_content(f"Segue o relatorio da organizacao:\n\n{corpo_email}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_remetente, email_senha)
        smtp.send_message(mensagem)

    print("E-mail enviado com sucesso!")
else:
    print("Envio de e-mail ignorado.")