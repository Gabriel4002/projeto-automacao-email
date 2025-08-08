# 🤖 Projeto de Automação de E-mails com Python

Este projeto tem como objetivo automatizar o envio de e-mails personalizados para diferentes destinatários com base em dados extraídos de uma planilha Excel. Foi desenvolvido como parte do meu aprendizado em automação com Python.

---

## 📌 Funcionalidades

- 📊 Geração de planilha com notas por aluno usando `openpyxl`
- 🧠 Cálculo automático da média por aluno
- ✉️ Envio de e-mails personalizados com `smtplib` e `email.message`
- 🔐 Proteção de dados sensíveis com `.env` e `python-dotenv`
- 🗂️ Organização modular do código e Registro completo dos envios em um arquivo `logs/envios_log.txt`
- ✅ Inclusão dos scripts usados durante o processo de aprendizagem

---

## 🧪 Tecnologias utilizadas

- Python 3.13.5
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- smtplib / email.message (bibliotecas padrão)

---

## 📁 Estrutura do projeto

```bash
projeto-automacao-email/
├── codigo_email.py               # Script principal: cria planilha e envia e-mails
├── codigo_envio_email.py          # Função para envio de e-mails via SMTP
├── planilha/
│   └── notas_alunos.xlsx          # Planilha gerada automaticamente
├── exemplos_aprendizado/          # Scripts e testes durante o estudo
│   ├── base.py
│   ├── ex01.py
│   ├── ex02.py
│   ├── ex03.py
│   └── final_ex.py
├── logs/
│   └── envios_log.txt             # Registro dos envios
├── .env                           # Variáveis de ambiente (NÃO subir no GitHub)
├── .gitignore
└── README.md
```

---

## 🚀 Como executar este projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/Gabriel4002/projeto-automacao-email.git
cd projeto-automacao-email
```

### 2️⃣ Criar e ativar um ambiente virtual (recomendado)
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar as variáveis de ambiente
- Copie o arquivo `.env.example` para `.env` (caso exista) ou crie um novo `.env`.
- Preencha com seu e‑mail e senha de aplicativo (ou outra conta SMTP válida):

```env
EMAIL=seuemail@gmail.com
SENHA=sua_senha_de_app
```
> ⚠️ Importante: use senha de aplicativo no Gmail ou configuração equivalente em outros provedores.

### 5️⃣ Executar o script principal
```bash
python codigo_email.py
```

Os e-mails serão enviados e o log ficará registrado no arquivo `logs/envios_log.txt`.

---

📌 **Observações**
- Certifique-se de que a planilha `planilha/notas_alunos.xlsx` existe ou será gerada antes do envio.
- Caso use Gmail, ative a autenticação em dois fatores e gere uma senha de app.

