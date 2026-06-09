## Etapa 4: Configurar Django REST Framework, iniciar o servidor e testar a API

Nesta etapa, realizaremos o seguinte:

- Configurar o Django REST Framework.
- Iniciar o servidor.
- Testar a API usando curl.

Copie e cole o(s) seguinte(s) prompt(s) no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.

> [!TIP]
> - Tenha em mente que o modo agent do Copilot é conversacional, então ele pode fazer perguntas para você e você pode fazer perguntas para ele também.
> - Aguarde um momento para o Copilot responder e pressione o botão continue para executar comandos apresentados pelo modo agent do Copilot.
> - Mantenha os arquivos criados e atualizados pelo modo agent do Copilot até que ele termine.
> - O modo agent tem a habilidade de avaliar sua base de código e executar comandos e adicionar/refatorar/deletar partes da sua base de código e se auto-curar automaticamente se ele ou você comete um erro no processo.

**Abra uma nova sessão do Copilot Chat clicando no ícone de mais `+` no painel do Copilot Chat.**

### :keyboard: Atividade: Configurar Django REST Framework e testar os endpoints da REST API

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos configurar o codespace para a URL, iniciar o servidor via VS Code launch.json e testar a API.
> 
> - Todos os arquivos do projeto Django estão no diretório `octofit-tracker/backend/octofit_tracker`.
> - Apenas atualize urls em `settings.py` e `urls.py`
> - Formato do endpoint da REST api https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
> - exemplo de url completa: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
> - Não codifique diretamente o valor `$CODESPACE_NAME`, use a variável
> - Não atualize o `views.py`
>
> 1. Atualize `urls.py` para substituir o retorno dos endpoints da URL da REST API com a variável de ambiente $CODESPACE_NAME https://$CODESPACE_NAME-8000.app.github.dev para Django e evitar problemas de certificado HTTPS.
> 2. Certifique-se de que o backend Django funcione na sua URL do codespace e localhost (ou seja, o valor de `$CODESPACE_NAME`) atualizando `ALLOWED_HOSTS` em `settings.py`.
> 3. Teste os endpoints da API usando comando curl.
>```

> [!IMPORTANT]
> Não inicie a app Python Django da maneira que o modo agent do GitHub Copilot sugere, clique
> **cancel**. Siga a próxima atividade em vez disso.

### :keyboard: Atividade: Iniciar a app Python Django e verificar a saída

Agora, vamos tentar executar a aplicação Django! Na barra lateral esquerda, selecione a aba `Run and Debug` e então pressione o ícone **Start Debugging**.

<img alt="Run Django" src="https://github.com/user-attachments/assets/a6c32898-bbeb-41ed-a8c5-488c8a42d507" width=30% height=30%>

Vá para a URL da API REST Django em execução que aparece para a porta 8000, que se parece com o seguinte:

<img alt="django-rest-api-port" src="https://github.com/user-attachments/assets/627f3cbe-96ae-4a30-b38b-acd3cecf96ee" width=30% height=30%>

Quando você abrir no seu navegador da web, você receberá um aviso como o seguinte:

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/cb52d137-e78d-440b-8e9c-c322d7c49b48" width=30% height=30%>

Quando você clicar em `Continue`, deve parecer semelhante ao seguinte com o nome do seu codespace:

<img alt="django-rest-api" src="https://github.com/user-attachments/assets/45ac98ba-aa7b-4953-81d6-e38bba97ae35" width=50% height=50%>

1. Agora que atualizamos nosso produto Django para incluir o nome do nosso codespace para o endpoint da URL,
   vamos fazer check-in das nossas mudanças no branch `build-octofit-app`.

1. Com nossas novas mudanças completas, por favor **commit** e **push** as mudanças para o branch `build-octofit-app`.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para que possamos continuar trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não recebeu feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para os seguintes arquivos no branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/views.py`
- Se Mona encontrou um erro, simplesmente faça uma correção e envie suas mudanças novamente. Mona vai verificar seu trabalho quantas vezes for necessário.

</details>
