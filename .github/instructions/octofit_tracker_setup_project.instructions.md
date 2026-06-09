---
applyTo: "**"
---
# Diretrizes de Configuração e Estrutura da App de Fitness Octofit-tracker

## Explicar os objetivos e etapas da App Octofit Tracker

Eu quero construir uma app Octofit Tracker que incluirá o seguinte:

* Autenticação de usuário e perfis
* Registro e rastreamento de atividades
* Criação e gerenciamento de equipes
* Placar de líderes competitivo
* Sugestões de treino personalizadas

## Nunca mude diretórios quando o modo agent estiver executando comandos

- Nunca mude diretórios
- Em vez disso, aponte para o diretório ao emitir comandos

## Portas encaminhadas

- 8000: pública
- 3000: pública
- 27017: privada

Não proponha outras portas para encaminhar ou tornar públicas

## Estrutura da App OctoFit Tracker

Esta seção define a estrutura da App OctoFit Tracker

```text
octofit-tracker/
├── backend/
│   ├── venv/
|   ├── octofit_tracker/
└── frontend/
```

## Criar o ambiente virtual Python do OctoFit Tracker

- Para criar o ambiente virtual, execute o seguinte comando:
  
  ```bash
  python3 -m venv octofit-tracker/backend/venv
  ```

## Pacotes Python obrigatórios do OctoFit Tracker

### Criar arquivo octofit-tracker/backend/requirements.txt

- adicione o seguinte ao octofit-tracker/backend/requirements.txt
- Instale os pacotes Python abaixo apenas para nosso projeto OctoFit Tracker

```text
Django==4.1.7
djangorestframework==3.14.0
django-allauth==0.51.0
django-cors-headers==4.5.0
dj-rest-auth==2.2.6
djongo==1.3.6
pymongo==3.12
sqlparse==0.2.4
stack-data==0.6.3
sympy==1.12
tenacity==9.0.0
terminado==0.18.1
threadpoolctl==3.5.0
tinycss2==1.3.0
tornado==6.4.1
traitlets==5.14.3
types-python-dateutil==2.9.0.20240906
typing_extensions==4.9.0
tzdata==2024.2
uri-template==1.3.0
urllib3==2.2.3
wcwidth==0.2.13
webcolors==24.8.0
webencodings==0.5.1
websocket-client==1.8.0
```

## Requisitos do ambiente virtual Python

Crie um requirements.txt com os seguintes pacotes Python obrigatórios:
Instale os requisitos que criamos em requirements.txt.

```bash
source octofit-tracker/backend/venv/bin/activate 
pip install -r octofit-tracker/backend/requirements.txt
```

## Serviço mongodb-org e criação de dados

- sempre use `ps aux | grep mongod` para verificar se o mongod está executando
- mongodb-org é o pacote oficial do MongoDB
- mongosh é a ferramenta cliente oficial
- Sempre use o ORM do Django, não scripts diretos do MongoDB para criar a estrutura e dados do banco
