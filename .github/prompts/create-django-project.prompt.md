---
mode: 'agent'
model: GPT-4.1
description: 'Criar um projeto Django, inicializá-lo e executá-lo'
---

Sua tarefa é criar o projeto Django no diretório octofit-tracker/backend/octofit_tracker usando o
ambiente virtual Python que já criamos no diretório octofit-tracker/backend/venv que contém todos os pré-requisitos.


Para criar o projeto Django siga estes passos.
1. Certifique-se de que estamos no diretório raiz e não mude de diretórios
2. source octofit-tracker/backend/venv/bin/activate
3. django-admin startproject octofit_tracker no diretório octofit-tracker/backend
4. python manage.py migrate
5. Instrua o usuário para executar a app django a partir da configuração .vscode/launch.json que está no repositório
