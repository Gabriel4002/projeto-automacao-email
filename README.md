# 🤖 Projeto de Automação de E-mails com Python

Este projeto tem como objetivo automatizar o envio de e-mails personalizados para diferentes destinatários com base em dados extraídos de uma planilha Excel. Foi desenvolvido como parte do meu aprendizado em automação com Python.

---

## 📌 Funcionalidades

- 📊 Geração de planilha com notas por aluno usando `openpyxl`
- 🧠 Cálculo automático da média por aluno
- ✉️ Envio de e-mails personalizados com `smtplib` e `email.message`
- 🔐 Proteção de dados sensíveis com `.env` e `python-dotenv`
- 🗂️ Organização modular do código
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
│   └── notas_alunos.xlsx    # Planilha gerada automaticamente
├── exemplos_aprendizado/    # Scripts e testes durante o estudo
│   └── exemplo_openpyxl.py
├── .env                     # Variáveis de ambiente (NÃO subir no GitHub)
├── .gitignore
└── README.md
