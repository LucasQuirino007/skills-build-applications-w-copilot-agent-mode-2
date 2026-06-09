## Etapa 6: Usando GitHub Copilot dentro de um pull request

Parabéns! Você terminou de codificar para este exercício (e VS Code). Agora é hora de fazer merge do nosso trabalho. :tada: Para finalizar, vamos aprender sobre dois recursos de acesso limitado do Copilot que podem acelerar nossos pull requests!

#### Sumários de Pull Request do Copilot

Tipicamente, você revisaria suas anotações e mensagens de commit e então as resumiria para a descrição do seu pull request. Isso pode levar algum tempo, especialmente se as mensagens de commit são inconsistentes ou o código não está bem documentado. Felizmente, o Copilot pode considerar todas as mudanças no pull request e fornecer os destaques importantes, e com referências também!

> [!NOTE]  
> Isso não está disponível com o tier **Copilot Free**. [[docs]](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/using-github-copilot-for-pull-requests/creating-a-pull-request-summary-with-github-copilot)

#### Revisão de código do Copilot

Mais olhos no nosso trabalho sempre é útil, então vamos pedir ao Copilot para fazer uma primeira análise antes de fazermos um processo normal de revisão por pares. O Copilot é ótimo para detectar erros comuns que podem ser corrigidos com ajustes simples, mas lembre-se de usá-lo de forma responsável.

### :keyboard: Atividade: Resumir e revisar um PR com Copilot

1. Em um navegador da web, abra outra aba e navegue até seu repositório de exercício.

1. Você pode notar um **banner de notificação** sugerindo criar um novo pull request. Clique nele ou use a aba **Pull Requests** no topo para criar um novo pull request. Use os seguintes detalhes:

   - **base:** `main`
   - **compare:** `build-octofit-app`
   - **title:** `Add registration validation and more activities`

1. (Opcional) Na área **Add a description**, entre no modo de edição se necessário, depois clique no ícone **Copilot actions** e na ação **Summary**. Após um momento, o Copilot adicionará uma descrição. :memo:

   <img alt="Copilot summarize button " width="300px" src="https://github.com/user-attachments/assets/3fc5fab4-db03-4ab8-8a16-cdd71ec2ded0">

1. (Opcional) No painel de informações do lado direito no topo, localize a seção **Reviewers** e clique no botão **Request** ao lado do **ícone do Copilot**. Aguarde um momento para o Copilot adicionar um comentário de revisão ao seu pull request!

   <img alt="Copilot review button" width="300px" src="https://github.com/user-attachments/assets/39b15002-a235-4c25-b09d-6a8097e27b62">

   > 🪧 **Nota:** Observe uma entrada de log que o Copilot foi solicitado para uma revisão.

1. Na parte inferior, pressione o botão **Merge pull request**. Bom trabalho! Você terminou tudo! :tada:

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e postar uma revisão final desta lição!
