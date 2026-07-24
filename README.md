# organizador-arquivos

Script em Python que organiza automaticamente os arquivos de uma pasta, separando-os em subpastas por tipo (imagens, documentos, planilhas, PDFs, etc), gera um relatório do que foi movido e envia esse relatório por e-mail.

Fiz esse projeto pra treinar automação de tarefas repetitivas com Python, aplicando conceitos usados em RPA — automatizar um processo manual, registrar o resultado e distribuir essa informação sem intervenção humana.

## O que ele faz

1. Lê todos os arquivos da pasta informada
2. Identifica a extensão de cada um
3. Move cada arquivo pra uma subpasta correspondente (`Imagens`, `Documentos`, `Apresentacoes`, `Compactados`, `Instaladores`)
4. Gera um relatório (`relatorio.txt`) listando o que foi movido e o que ficou sem categoria
5. Envia esse relatório por e-mail automaticamente (opcional — o programa pergunta antes)

## Tecnologias

- Python 3
- `os` e `shutil` — leitura e movimentação de arquivos
- `smtplib` — envio de e-mail
- `python-dotenv` — leitura segura de credenciais

## Configuração do ambiente

### Pré-requisitos

- Python 3 instalado
- Git instalado

### Instalação

```bash
git clone https://github.com/brunofaomoura-max/automacao-organizador-arquivos.git
cd automacao-organizador-arquivos
python -m venv venv
```

Ativar o ambiente virtual:

```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Git Bash) / Linux / Mac
source venv/Scripts/activate
```

Instalar as dependências:

```bash
pip install -r requirements.txt
```

### Configurar o envio de e-mail (opcional)

O envio por e-mail é opcional — o programa pergunta antes de tentar enviar. Para usar essa função, copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Preencha o `.env` com suas credenciais:
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA=sua_senha_de_app_do_gmail
EMAIL_DESTINATARIO=email_que_vai_receber@gmail.com
A senha deve ser uma "senha de app" gerada em [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords), já que o Gmail não aceita mais a senha padrão da conta para esse tipo de acesso.

### Execução

```bash
python organizador.py
```

O script vai pedir o caminho da pasta que você quer organizar e, em seguida, se deseja enviar o relatório por e-mail.

### Erros comuns

| Erro | Causa | Solução |
|---|---|---|
| `can't open file 'organizador.py': No such file or directory` | Terminal fora da pasta do projeto | Use `cd` para navegar até a pasta correta |
| `Import "dotenv" could not be resolved` | Dependências não instaladas nesse ambiente | Rode `pip install -r requirements.txt` |
| `Author identity unknown` ao commitar | Git sem nome/e-mail configurado na máquina | `git config --global user.name "Seu Nome"` e `git config --global user.email "seu@email.com"` |

## Possíveis melhorias futuras

- Tratamento de erros (arquivos em uso, permissões, etc)
- Log com data e hora de cada execução
- Agendamento automático (rodar todo dia, por exemplo)
- Interface gráfica simples
