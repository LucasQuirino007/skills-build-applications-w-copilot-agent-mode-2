## Etapa 3: Inicializar e criar o banco de dados MongoDB octofit_db, projeto/app Django, atualizar arquivos do projeto/app Django e popular o banco de dados MongoDB

Nesta etapa, realizaremos o seguinte:

- Configurar a estrutura do banco de dados MongoDB octofit_db.
- Atualizar os arquivos da app octofit-tracker/backend/octofit_tracker:
  - arquivos settings, models, serializers, urls, views, tests e admin.
- Popular o banco de dados octofit_db com dados de teste.
- Verificar se os dados de teste foram populados no banco de dados octofit_db.

Copie e cole o(s) seguinte(s) prompt(s) no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.

> [!NOTE]
> - Tenha em mente que o modo agent do Copilot é conversacional, então ele pode fazer perguntas para você e você pode fazer perguntas para ele também.
> - Aguarde um momento para o Copilot responder e pressione o botão `Continue` para executar comandos apresentados pelo modo agent do Copilot.
> - Mantenha os arquivos criados e atualizados pelo modo agent do Copilot até que ele termine.
> - O modo agent tem a habilidade de avaliar sua base de código e executar comandos e adicionar/refatorar/deletar partes da sua base de código e se auto-curar automaticamente se ele ou você comete um erro no processo.

**Abra uma nova sessão do Copilot Chat clicando no ícone de mais `+` no painel do Copilot Chat.**

### :keyboard: Atividade: Configurar o projeto/app Python Django

Nesta atividade aproveitaremos um recurso no VS Code chamado arquivos de prompt. Um arquivo de prompt que foi criado pelo departamento de TI para nós criarmos nossa aplicação do projeto Django. Copie/cole o seguinte prompt no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.

O que são arquivos de prompt?

Arquivos de prompt permitem que você defina prompts reusáveis para tarefas de desenvolvimento comuns e repetíveis em um arquivo Markdown.
Arquivos de prompt são prompts independentes que você pode executar diretamente no chat. Você pode incluir contexto específico da tarefa e diretrizes sobre como a tarefa deve ser realizada.
Combine arquivos de prompt com instruções personalizadas para garantir execução consistente de tarefas complexas.

See the [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/customization/overview#_prompt-files) page for more information.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> /create-django-project
>```

> [!NOTE]
> - Aguarde um momento para o Copilot responder e pressione o botão `Continue` para executar cada comando apresentado pelo modo agent do Copilot.
> - Mantenha os arquivos criados e atualizados até que o modo agent do Copilot termine.

> [!IMPORTANT]
> - Não inicie a app Python Django da maneira que o modo agent do GitHub Copilot sugere, clique **cancel** quando você ver esta imagem.

<img src="https://github.com/user-attachments/assets/02a875c1-19a4-417b-ab03-aefbbe2186d4" width=50% height=50%>

### :keyboard: Atividade: Inicializar, criar e popular o banco de dados MongoDB octofit_db

Vamos continuar aproveitando um arquivo de prompt que foi criado pelo departamento de TI para nós inicializarmos e criarmos o banco de dados MongoDB octofit_db. Copie/cole o seguinte prompt no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
>
> /init-populate-octofit_db
> ```

### :keyboard: Atividade: Vamos criar um arquivo de prompt que atualizará os arquivos do projeto/app Python Django

Agora vamos criar um arquivo de prompt nosso que podemos compartilhar com outros funcionários para desenvolver e construir a app octofit-tracker. Copie/cole o seguinte prompt no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos adicionar o seguinte a um arquivo de prompt chamado `update-octofit-tracker-app.prompt.md` no diretório `.github/prompts` e adicionar mode: 'agent' e model: GPT-4.1 ao arquivo de prompt.
>
> # Atualizações da App Django
>
> - Todos os arquivos do projeto Django estão no diretório `octofit-tracker/backend/octofit_tracker`.
>
> 1. Atualize `settings.py` para conexão MongoDB e CORS.
> 2. Atualize `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` e `admin.py` para suportar coleções de usuários, equipes, atividades, placar de líderes e treinos.
> 3. Certifique-se de que `/` aponta para a api e `api_root` está presente em `urls.py`.
> ```

> [!TIP]
> Use arquivos de prompt para definir tarefas e fluxos de trabalho repetíveis.
>
> Ao escrever prompts, foque no **QUE** precisa ser feito. Você pode referenciar instruções para o **COMO**.

See the [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/customization/overview#_prompt-files) page for more information.

### :keyboard: Atividade: Vamos usar o arquivo de prompt para atualizar os arquivos do projeto/app Python Django

Copie/cole o seguinte prompt no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> /update-octofit-tracker-app
> ```
>

> [!IMPORTANT]
> - Não inicie a app Python Django da maneira que o modo agent do GitHub Copilot sugere, clique **cancel** quando você ver esta imagem.

<img src="https://github.com/user-attachments/assets/02a875c1-19a4-417b-ab03-aefbbe2186d4" width=50% height=50%>

1. Agora que criamos a estrutura do banco de dados, atualizamos nossos arquivos do projeto Django e populamos o banco de dados, vamos verificar nossas mudanças na nossa branch `build-octofit-app`.

1. Com nossas novas mudanças completas, por favor **commit** e **push** as mudanças para o GitHub.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para que possamos continuar trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para os seguintes arquivos na branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py`
- Se Mona encontrou um erro, simplesmente faça uma correção e envie suas mudanças novamente. Mona verificará seu trabalho quantas vezes for necessário.

</details>
