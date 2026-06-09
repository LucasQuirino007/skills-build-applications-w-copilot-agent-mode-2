---
applyTo: "octofit-tracker/frontend/**"
---
# Diretrizes do Frontend React da App de Fitness Octofit-tracker

## Estrutura da App Frontend REACT

Certifique-se de que em todos os comandos apontamos para o diretório `octofit-tracker/frontend`

```bash
npx create-react-app octofit-tracker/frontend --template cra-template --use-npm

npm install bootstrap --prefix octofit-tracker/frontend

# Add the Bootstrap CSS import at the very top of src/index.js:
sed -i "1iimport 'bootstrap/dist/css/bootstrap.min.css';" octofit-tracker/frontend/src/index.js

npm install react-router-dom --prefix octofit-tracker/frontend

```

## Imagens para a App OctoFit Tracker

A imagem para usar na app está na raiz deste repositório docs/octofitapp-small.png
