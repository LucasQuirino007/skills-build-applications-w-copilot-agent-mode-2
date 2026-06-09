# Construindo uma App de Fitness com o modo agent do GitHub Copilot para a Escola Secundária Mergington

## História da aplicação OctoFit Tracker para a Escola Secundária Mergington

Paul Octo é professor de educação física na Escola Secundária Mergington há mais de 8 anos. Apesar de seu entusiasmo e abordagem criativa para as aulas de ginástica, ele tem se preocupado cada vez mais com o declínio da atividade física dos estudantes quando saem do ambiente escolar. Muitos estudantes admitiram que raramente se exercitavam fora das aulas de EF obrigatórias.
Após participar de uma conferência de desenvolvimento profissional sobre "Integração de Tecnologia na Educação Física," Paul se inspirou a criar uma solução. Ele queria algo que:

1. Tornasse o rastreamento de fitness divertido e envolvente
2. Criasse pressão positiva dos colegas através de competição amigável
3. Permitisse que ele monitorasse o progresso dos estudantes remotamente
4. Fornecesse orientação personalizada baseada nos níveis individuais de fitness

## O Nascimento do OctoFit Tracker

Paul inicialmente esboçou sua ideia em um bloco de notas durante os intervalos do almoço. Ele imaginou uma app onde os estudantes poderiam registrar treinos, ganhar distintivos de conquista e competir em desafios mensais de fitness. No entanto, como um professor de EF com apenas conhecimento básico de programação, os aspectos técnicos pareciam assustadores.
Foi então que ele procurou Jessica Cat, chefe do departamento de TI da Escola Mergington. Jessica recomendou usar nossas instruções e prompts do repositório.

### Fase de Planejamento Técnico

Antes de iniciar o desenvolvimento, Paul e Jessica revisaram cuidadosamente as instruções e prompts do OctoFit Tracker. Isso forneceu uma base sólida para o OctoFit Tracker, garantindo conformidade com padrões técnicos e aproveitando padrões de design comprovados.
Juntos, Paul e a equipe de TI identificaram requisitos-chave para o OctoFit Tracker:

### Objetivos de Experiência do Usuário

- Interface simples e intuitiva projetada especificamente para adolescentes
- Registro rápido de atividades para minimizar o atrito
- Recursos sociais que respeitam a privacidade dos estudantes
- Elementos de gamificação para manter o envolvimento

## Status Atual do Desenvolvimento

Paul e Jessica configuraram um ambiente GitHub Codespace e estão fazendo progresso notável com o modo agent do GitHub Copilot. O protótipo do OctoFit Tracker incluirá:

- Um sistema funcional de registro de usuários
- Registro básico de atividades para corrida, caminhada e treinamento de força
- A estrutura inicial para competições em equipe
- Um painel simples mostrando o progresso dos estudantes

## Próximos Passos para Paul

Com a infraestrutura básica no lugar, Paul agora está focado em:

1. Desenvolver um sistema de pontos envolvente que compare de forma justa diferentes tipos de atividades
2. Criar desafios motivacionais que atraiam diferentes interesses dos estudantes
3. Construir um sistema de notificações que encoraje consistência sem ser intrusivo
4. Projetar relatórios que o ajudem a identificar estudantes que possam precisar de apoio ou motivação adicional

O departamento de TI ficou impressionado com como o modo agent do GitHub Copilot acelerou o desenvolvimento, permitindo que Paul se concentrasse nos aspectos educacionais enquanto a IA cuida de muito da implementação técnica. Jessica Cat ficou particularmente satisfeita com como o OctoFit Tracker aproveita as instruções personalizadas e arquivos de prompt.

### Visão Geral do Workshop

Neste workshop, você irá:

1. Configurar um ambiente de desenvolvimento usando **GitHub Codespaces**
2. Usar **GitHub Copilot** para acelerar o desenvolvimento em múltiplas tecnologias
3. Construir componentes-chave da app **OctoFit Tracker** com a ajuda do modo agent do Copilot
4. Aprender melhores práticas e técnicas de prompting para trabalhar com **modo agent do GitHub Copilot**

### Funcionalidades da Aplicação

**OctoFit Tracker** incluirá:

- Perfis de usuários
- Registro e rastreamento de atividades
- Criação e gerenciamento de equipes
- Um placar de líderes competitivo
- Sugestões de treino personalizadas

### GitHub Copilot Chat

- [Começando com GitHub Copilot Chat](https://docs.github.com/en/copilot/how-tos/use-chat/get-started-with-chat?tool=vscode)
- [Usar Chat na IDE](https://docs.github.com/en/copilot/how-tos/use-chat/use-chat-in-ide?tool=vscode)

#### Referências de modelos LLM

- [Modelos de IA suportados no GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models)
- [Comparação de modelos de IA](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)
- [Alterando o modelo de IA para GitHub Copilot Chat](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model?tool=vscode)
- [Alterando o modelo de IA para compleção de código do GitHub Copilot](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-completion-model?tool=vscode)

#### Engenharia de prompt

- [Engenharia de prompt para GitHub Copilot Chat](https://docs.github.com/en/copilot/concepts/prompt-engineering)
- [Como usar GitHub Copilot: Prompts, dicas e casos de uso](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Usando GitHub Copilot na sua IDE: Dicas, truques e melhores práticas](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)

### Stack tecnológico da aplicação de fitness OctoFit tracker

Estaremos usando um stack moderno de aplicação web:

- **Frontend**: React.js
- **Backend**: Python com Django REST API Framework
- **Banco de Dados**: MongoDB
- **Ambiente de Desenvolvimento**: GitHub Codespaces

### Estrutura do Workshop

1. **Introdução**
   - Visão geral do conceito da app OctoFit Tracker
   - Modelos do GitHub Copilot Chat

2. **Configuração de Pré-requisitos**
   - Configurando GitHub Codespaces
   - Garantir que as extensões GitHub Copilot e Copilot Chat estejam atualizadas

3. **Prototipagem Rápida com modo agent do GitHub Copilot**
   - Criando estrutura do projeto
   - Gerando código boilerplate
   - Implementando models, serializers, urls e views básicos

4. **Construindo Funcionalidades Principais**
   - Registro e rastreamento de atividades
   - Perfis de usuários
   - Gerenciamento de equipes
   - Funcionalidade de placar de líderes

5. **Desenvolvimento Frontend e Backend**
   - Configurando componentes React
   - Implementando UI responsiva
   - Conectando a APIs backend
   - Lógica de negócio Python Django
   - Camada de dados MongoDB
