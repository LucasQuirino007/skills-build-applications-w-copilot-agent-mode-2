## Etapa 2: A configuração inicial da aplicação: Estrutura de diretórios, requisitos Python e MongoDB

Nesta etapa, iremos realizar o seguinte:

- Criar a estrutura de diretórios da aplicação octofit-tracker.
- Criar os diretórios octofit-tracker/backend e octofit-tracker/frontend.
- Criar o arquivo octofit-tracker/backend/requirements.txt.

> [!NOTE]
> Copie e cole o(s) seguinte(s) prompt(s) no GitHub Copilot Chat e selecione "Agent" ao invés de "Ask" ou "Edit" no menu suspenso onde você está inserindo o prompt.
> - Tenha em mente que o modo agent do Copilot é conversacional, então ele pode fazer perguntas para você e você pode fazer perguntas para ele também.
> - Aguarde um momento para o Copilot responder e pressione o botão `Continue` para executar comandos apresentados pelo modo agent do Copilot.
> - Mantenha os arquivos criados e atualizados pelo modo agent do Copilot até que ele termine.
> - O modo agent tem a habilidade de avaliar sua base de código e executar comandos e adicionar/refatorar/deletar partes da sua base de código e se auto-curar automaticamente se ele ou você comete um erro no processo.

**Abra uma nova sessão do Copilot Chat clicando no ícone de mais `+` no painel do Copilot Chat.**

### :keyboard: Atividade: Prompt para o GitHub Copilot no modo agent iniciar a criação da nossa aplicação

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos seguir os seguintes passos e executar os comandos.
> 
> Siga as instruções
>
> - Siga a estrutura da OctoFit Tracker App
> - Siga a criação do ambiente virtual Python
> - Crie o arquivo requirements.txt
> - Instale os requisitos Python do arquivo criado
>```

1. Agora que criamos a estrutura de diretórios da aplicação, configuramos um ambiente virtual Python, e o modo agent do Copilot ajudou a escrever um `requirements.txt` para instalar todas as dependências do projeto, vamos confirmar nossas mudanças na nossa branch `build-octofit-app`.

1. Com nossas novas mudanças completas, por favor **commit** e **push** as mudanças para a branch `build-octofit-app`.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para que possamos continuar trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para o seguinte arquivo na branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/backend/requirements.txt` e que contém o pacote `Django==4.1`
- Se Mona encontrou um erro, simplesmente faça uma correção e envie suas mudanças novamente. Mona verificará seu trabalho quantas vezes for necessário.

</details>
