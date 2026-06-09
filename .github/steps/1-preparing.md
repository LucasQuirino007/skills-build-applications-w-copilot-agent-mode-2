## Etapa 1: Olá modo agent do GitHub Copilot

Bem-vindo ao seu exercício **"Construa aplicações com o modo agent do GitHub Copilot"**! :robot:

Neste exercício, você usará o modo agent do GitHub Copilot para construir uma aplicação que rastreia suas metas e progresso de fitness. 🏋️‍♂️🏃‍♀️💪

### O que é o modo agent do GitHub Copilot?

O modo agent do Copilot pode criar aplicações do zero, refatorar em múltiplos arquivos, escrever e executar testes, e migrar código legado para frameworks modernos. Ele pode gerar documentação automaticamente, integrar novas bibliotecas, ou ajudar a responder questões sobre uma base de código complexa. O modo agent do Copilot ajuda você a ser super-produtivo tendo um colaborador de IA que entende o workspace. Ele pode orquestrar seu fluxo de desenvolvimento interno mantendo você no controle.

O modo agent do Copilot opera de forma mais autônoma e dinâmica para alcançar o resultado desejado. Para processar uma solicitação, o Copilot executa os seguintes passos em loop e itera múltiplas vezes conforme necessário:

Determina o contexto relevante e arquivos para editar de forma autônoma.
Oferece tanto mudanças de código quanto comandos de terminal para completar a tarefa. Por exemplo, o Copilot pode compilar código, instalar pacotes, executar testes e muito mais.
Monitora a correção das edições de código e saída dos comandos de terminal e itera para remediar problemas.

> [!NOTE]
> Você pode aprender mais sobre o modo agent do GitHub Copilot na [documentação Use agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode).

### :keyboard: Atividade: Conhecendo seu ambiente de desenvolvimento do modo agent do GitHub Copilot

1. Clique com o botão direito no botão abaixo para abrir a página **Create Codespace** em uma nova aba.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

   - O nível gratuito dos Codespaces que vem com todas as contas GitHub está bem, assumindo que você ainda tem minutos disponíveis.
   - As configurações padrão do Codespace estão adequadas.

1. Confirme que o campo **Repository** é sua cópia do exercício, não o original, então clique no botão verde **Create Codespace**.

   - ✅ Sua cópia: `/{{full_repo_name}}`
   - ❌ Original: `/skills/build-applications-w-copilot-agent-mode`

1. Aguarde um momento para o Visual Studio Code carregar.

1. Antes de continuarmos, vamos dedicar um momento para nos familiarizar com a pasta do projeto.

   - A barra de navegação à esquerda é onde você pode acessar o explorador de arquivos, debugger e pesquisa.
   - O painel inferior (Ctrl+J) mostra a saída do debugger, permite executar comandos de terminal e permite configurar as portas do serviço web.
   - Nossa pasta docs contém outro repositório de aplicação de exemplo que dará contexto ao modo agent do Copilot para construir sua aplicação. Mais sobre isso nos próximos passos!

1. No topo do VS Code, localize e clique no ícone do Copilot para abrir um painel do Copilot Chat.

   <img width="150" alt="image" src="https://github.com/user-attachments/assets/5e64db46-95cb-415d-badc-b6b8677f10c1" />

1. Se esta é sua primeira vez usando o GitHub Copilot, você terá que aceitar os termos de uso para continuar.
    - Clique no botão **Accept** para continuar.

### :keyboard: Atividade: Use o modo agent do Copilot para criar uma branch e publicá-la. 🙋

Ótimo trabalho! Vamos pedir ajuda ao copilot para iniciar uma branch para que possamos fazer algumas personalizações.

> [!NOTE]
> - Tenha em mente que o modo agent do Copilot é conversacional, então ele pode fazer perguntas para você e você pode fazer perguntas para ele também.
> - Aguarde um momento para o Copilot responder e pressione o botão **Continue** para executar comandos apresentados pelo modo agent do Copilot.

1. Se não estiver lá, retorne ao VS Code.
1. Abra a janela do GitHub Copilot Chat se não estiver aberta.
1. Copie e cole o seguinte prompt no GitHub Copilot Chat e selecione **Agent** ao invés de **Ask** ou **Edit** no menu suspenso onde você está inserindo o prompt.

   <img src="https://github.com/user-attachments/assets/b9e291be-d835-4de0-ac1c-35a6ec3ea72d" width=30% height=30%>

1. Vamos pedir ao modo agent do Copilot para nos ajudar a lembrar do comando e criar a branch `build-octofit-app` e publicá-la

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
   >
   > ```prompt
   > Por favor, crie e publique uma nova branch do Git chamada build-octofit-app
   > ```

   O modo agent do Copilot responderá e pedirá para você **continuar** para executar o comando.<br/>

   <img src=https://github.com/user-attachments/assets/d1652fc1-78e5-49c6-9303-b455815eea8f width=40% height=40%>

1. Agora que estamos satisfeitos com o comando, pressione o botão `Continue` para deixar o modo agent do Copilot executá-lo para nós. Não precisa copiar e colar!

1. Após um momento, olhe na barra de status inferior do VS Code, à esquerda, para ver a branch ativa. Agora deve dizer `build-octofit-app`. Se sim, você terminou esta etapa!

1. Agora que sua branch foi enviada para o GitHub, Mona já deve estar ocupada verificando seu trabalho. Dê um momento para ela e fique de olho nos comentários. Você verá ela responder com informações de progresso e a próxima lição.

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que criou a branch com o nome exato `build-octofit-app`. Sem prefixos ou sufixos.
- Certifique-se de que a branch foi realmente publicada no seu repositório.

</details>
