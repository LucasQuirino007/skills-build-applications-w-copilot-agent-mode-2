## Etapa 5: Configurar o framework React do frontend, atualizar os componentes e iniciar a app OctoFit Tracker

Nesta etapa, realizaremos o seguinte:

- Configurar o framework React do frontend octofit-tracker.
- Atualizar os seguintes componentes para incluir o framework React:
  - src/App.js
  - src/index.js
  - src/components/Activities.js
  - src/components/Leaderboard.js
  - src/components/Teams.js
  - src/components/Users.js
  - src/components/Workouts.js
- Iniciar o app React e verificar a saída.

Copie e cole o(s) seguinte(s) prompt(s) no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.

> [!NOTE]
> - Tenha em mente que o modo agent do Copilot é conversacional, então ele pode fazer perguntas para você e você pode fazer perguntas para ele também.
> - Aguarde um momento para o Copilot responder e pressione o botão continue para executar comandos apresentados pelo modo agent do Copilot.
> - Mantenha os arquivos criados e atualizados pelo modo agent do Copilot até que ele termine.
> - O modo agent tem a habilidade de avaliar sua base de código e executar comandos e adicionar/refatorar/deletar partes da sua base de código e se auto-curar automaticamente se ele ou você comete um erro no processo.

**Abra uma nova sessão do Copilot Chat clicando no ícone de mais `+` no painel do Copilot Chat.**

### :keyboard: Atividade: Instalar o framework React do frontend octofit-tracker

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos configurar o framework React do frontend octofit-tracker e
> garantir que tudo seja criado no diretório `octofit-tracker/frontend` usando `--prefix`
>
> 1. Certifique-se de que o diretório octofit-tracker/frontend existe.
> 2. crie o app react
> 3. Instale react, bootstrap e react-router-dom
> 4. Importe o CSS do bootstrap no arquivo src/index.js.
> 5. Não altere o arquivo .gitignore
>```

### :keyboard: Atividade: Atualizar os componentes React do frontend octofit-tracker

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos atualizar os componentes React do frontend octofit-tracker.
>
> - Atualize os seguintes componentes para incluir o framework React para apontar para a REST API do backend:
>   - src/App.js
>   - src/index.js
>   - src/components/Activities.js
>   - src/components/Leaderboard.js
>   - src/components/Teams.js
>   - src/components/Users.js
>   - src/components/Workouts.js
> - Em cada componente, substitua a URL de fetch pela URL do codespace
>   https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/[component]/
>   para o backend do framework Django rest.
>   certifique-se de que todos os componentes estão obtendo dados do endpoint da REST API
>   para exibição no frontend REACT
> - Certifique-se de usar a porta e protocolo corretos http ou https.
> - Atualize src/App.js para incluir a navegação principal para todos os componentes.
> - Certifique-se de que react-router-dom seja usado para o menu de navegação.
> - O app react deve mostrar o menu de navegação e os componentes.
> - Atualize todos os componentes para registrar os dados obtidos e torná-los compatíveis com respostas paginadas (.results) e arrays simples.
> - Adicione instruções console.log a cada componente para registrar os dados obtidos e os endpoints da REST API.
> ```

### :keyboard: Atividade: Iniciar o app react e verificar a saída

Agora, vamos tentar executar a aplicação react! Na barra lateral esquerda, selecione a aba `Run and Debug` e então pressione o ícone **Start Debugging**.

<img alt="Run React Frontend" src="https://github.com/user-attachments/assets/b76a8e82-8435-4cbd-9540-8143756d1c60"  width=30% height=30%>

Vá para a URL do Frontend React em execução que aparece para a porta 3000, que se parece com o seguinte:

<img alt="react-frontend-port" src="https://github.com/user-attachments/assets/a0c8b213-ee5f-46dd-8675-686a7ba0818f" width=30% height=30%>

Quando você abrir no seu navegador da web, você receberá um aviso como o seguinte:

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/cb52d137-e78d-440b-8e9c-c322d7c49b48" width=30% height=30%>

Quando você clicar em `Continue`, deve parecer semelhante ao seguinte:

<img alt="react-frontend-app" src="https://github.com/user-attachments/assets/f7f1a076-c259-49f6-8aa5-9ebcd5f0698d" width=50% height=50%>

### :keyboard: Atividade: Vamos adicionar formatação, estruturação e estilo ao app octofit tracker

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos estilizar isso como App.css e fazer com que pareça bonito.
>
> - Vamos fazer o App.js e todos os arquivos javascript de componentes no app serem consistentes com o seguinte:
>   - Use tabelas bootstrap para os dados em todos os componentes javascript.
>   - Use botões bootstrap para os botões.
>   - Use títulos bootstrap para os títulos.
>   - Use links bootstrap para os links.
>   - Use navegação bootstrap para o menu de navegação.
>   - Use formulários bootstrap para os formulários.
>   - Use cartões bootstrap para os cartões.
>   - Use modais bootstrap para os modais.
>   - Layouts de tabela consistentes para dados de todos os componentes.
>```

### :keyboard: Atividade Opcional: Vamos fazer o app octofit tracker parecer bonito, atraente e adicionar algumas cores

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos estilizar isso como App.css e fazer com que pareça bonito.
> 
> -  Edite o arquivo App.css para fazer o seguinte:
>   - Adicione algumas cores ao fundo.
>   - Adicione algumas cores ao texto.
>   - Adicione algumas cores às tabelas.
>   - Adicione algumas cores aos botões.
>   - Adicione algumas cores aos títulos.
>   - Adicione algumas cores aos links.
>   - Adicione algumas cores ao menu de navegação.
> - Adicione o logo octofitapp-small justificado à esquerda no app e faça com que pareça bonito.
> - Adicione um favicon ao app e faça com que pareça bonito.
>```

### :keyboard: Atividade Opcional: Iterar na aparência e tentar modelos diferentes

> [!TIP]
> - Tente criar seus próprios prompts para alterar a aparência da aplicação, adicionar recursos e tentar modelos diferentes.

1. Agora que criamos o frontend React para todos os componentes da aplicação, vamos fazer check-in das nossas mudanças no nosso branch `build-octofit-app`.

1. Com nossas novas mudanças completas, por favor **commit** e **push** as mudanças para o branch `build-octofit-app`.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para que possamos continuar trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não recebeu feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para os seguintes arquivos no branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/frontend/src/components/Activities.js` e contém `-8000.app.github.dev/api/activities/`
  - `octofit-tracker/frontend/src/components/Leaderboard.js` e contém `-8000.app.github.dev/api/leaderboard/`
  - `octofit-tracker/frontend/src/components/Teams.js` e contém `-8000.app.github.dev/api/teams/`
  - `octofit-tracker/frontend/src/components/Users.js` e contém `-8000.app.github.dev/api/users/`
  - `octofit-tracker/frontend/src/components/Workouts.js` e contém `-8000.app.github.dev/api/workouts/`
- Se Mona encontrou um erro, simplesmente faça uma correção e envie suas mudanças novamente. Mona vai verificar seu trabalho quantas vezes for necessário.

</details>
