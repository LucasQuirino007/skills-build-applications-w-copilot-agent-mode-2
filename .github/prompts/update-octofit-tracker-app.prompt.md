---
mode: 'agent'
model: GPT-4.1
description: 'Atualizar app Django OctoFit Tracker com MongoDB, CORS e endpoints de domínio'
---

# Atualizações da App Django

- Todos os arquivos do projeto Django estão no diretório `octofit-tracker/backend/octofit_tracker`.

1. Atualize `settings.py` para conexão MongoDB e CORS.
2. Atualize `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` e `admin.py` para suportar coleções de usuários, equipes, atividades, placar de líderes e treinos.
3. Certifique-se de que `/` aponta para a api e `api_root` está presente em `urls.py`.
