---
mode: 'agent'
model: GPT-4.1
description: 'Configurar, configurar e popular o banco de dados octofit_db com dados de teste para a app Django Octofit Tracker.'
---

# Configuração do Ambiente
- Use o ambiente virtual Python existente em `octofit-tracker/backend/venv`.
- Não crie um novo ambiente virtual Python.
- Ative com: `source octofit-tracker/backend/venv/bin/activate`
- `mongodb-org-shell` já está instalado; use `mongosh` para interagir com MongoDB.
- O projeto Django está em `octofit-tracker/backend/octofit_tracker`.

# Inicialização e População do Banco de Dados
1. Certifique-se de que o serviço MongoDB está executando.
2. Configure o Django em `settings.py` para conectar ao banco de dados `octofit_db` usando Djongo, sem autenticação ou senha necessária.
3. Certifique-se de que `octofit_tracker`, `rest_framework` e `djongo` estão em `INSTALLED_APPS`.
4. Habilite CORS em `settings.py` para permitir todas as origens, métodos e cabeçalhos. Permitir todos os hosts `*`.
5. Instale e configure os componentes de middleware CORS.
6. Execute `makemigrations` e `migrate` no ambiente virtual Python.
7. Inicialize o banco de dados `octofit_db` e crie coleções para usuários, equipes, atividades, placar de líderes e treinos.
8. Certifique-se de que há um índice único no campo `email` para a coleção de usuários (ex: `db.users.createIndex({ "email": 1 }, { unique: true })`).
9. Popule o banco de dados com dados de teste para todas as coleções usando o comando de gerenciamento Django em `octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py` 
  a. mensagem de ajuda: 'Popular o banco de dados octofit_db com dados de teste'.
  b. ORM do Django para deleção e inserção de dados
  c. Faça os dados de exemplo serem super heróis e use equipe marvel e equipe dc.
10. Verifique se o banco de dados e coleções foram criados e populados com sucesso usando `mongosh`.
11. Liste as coleções no banco de dados `octofit_db` e mostre documentos de exemplo de cada.

# Verificação
- Após a população, verifique com `mongosh` que o banco de dados `octofit_db` contém as coleções corretas e dados de teste.
- Confirme que os endpoints da API REST Django estão disponíveis para todas as coleções.
