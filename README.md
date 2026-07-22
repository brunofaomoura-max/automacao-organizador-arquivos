# organizador-arquivos

Script em Python que organiza automaticamente os arquivos de uma pasta, separando-os em subpastas por tipo (imagens, documentos, planilhas, PDFs, etc), gera um relatório do que foi movido e envia esse relatório por e-mail.

Fiz esse projeto pra treinar automação de tarefas repetitivas com Python, aplicando conceitos usados em RPA — automatizar um processo manual, registrar o resultado e distribuir essa informação sem intervenção humana.

## Como rodar

```bash
git clone https://github.com/brunofaomoura-max/automacao-organizador-arquivos.git
cd automacao-organizador-arquivos
pip install -r requirements.txt
python organizador.py
```

O script vai pedir:
- O caminho da pasta que você quer organizar
- O e-mail de destino do relatório

## O que ele faz

1. Lê todos os arquivos da pasta informada
2. Identifica a extensão de cada um
3. Move cada arquivo pra uma subpasta correspondente (`Imagens`, `Documentos`, `Planilhas`, `Outros`)
4. Gera um relatório (`relatorio.txt`) listando o que foi movido e para onde
5. Envia esse relatório por e-mail automaticamente

## Tecnologias

- Python 3
- `os` e `shutil` — leitura e movimentação de arquivos
- `smtplib` — envio de e-mail

## Possíveis melhorias futuras

- Interface gráfica simples
- Agendamento automático (rodar todo dia, por exemplo)
- Log mais detalhado, com data e hora de cada execução
