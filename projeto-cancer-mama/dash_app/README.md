
# FIAP - Pós Tech -- Curso IA para Devs 2025/2026

## Tech Challenge -- Fase 1 - Welcome to IA para Devs

## Sistema Inteligente de Apoio ao Diagnóstico - Câncer de Mama

Este projeto foi desenvolvido como parte do Tech Challenge (Fase 1) da Pós-Tech FIAP. O objetivo é auxiliar médicos de um hospital universitário na análise inicial de exames de câncer de mama, utilizando Machine Learning para triagem e suporte à decisão baseada em diferentes contextos clínicos.

## Demonstração

[Acesse a aplicação online: Hugging Face Spaces - Saúde da Mulher ML](https://huggingface.co/spaces/leonardoleojosants/fiap-tech-challenge-fase-1-saude-mulher-ml)

## Funcionalidades

- Análise Preditiva:
  - Identificação de indícios de tumores malignos ou benignos com base no dataset Breast Cancer Wisconsin.

- Contextos Clínicos Adaptáveis:
  - Permite ajustar o limiar (threshold) de decisão de acordo com o cenário de uso (Triagem, Ambulatório, Exames Invasivos ou Confirmação).

- Visualização de Dados:
  - Gráficos comparativos entre o risco estimado do paciente e os protocolos clínicos estabelecidos.

- Persistência Local:
  - Armazenamento automático da última análise realizada no navegador do usuário.

## Tecnologias Utilizadas

- O projeto utiliza o ecossistema Python focado em ciência de dados e aplicações web:
  - Interface:
    - Dash & Plotly (Visualização interativa)
  
  - Machine Learning:
    - Scikit-learn (Modelo RandomForest e Pipelines)
  
  - Processamento de Dados:
    - Pandas & NumPy
  
  - Deploy:
    - [Hugging Face Spaces](https://huggingface.co/spaces)

## O Modelo de Machine Learning

- O sistema utiliza um RandomForestClassifier otimizado, integrado em um pipeline que inclui a padronização de escalas (StandardScaler).
  - Dataset:
    - Breast Cancer Wisconsin Diagnostic.
  
  - Acurácia:
    - O modelo foca no equilíbrio entre sensibilidade (para evitar falsos negativos em triagens) e precisão (para evitar procedimentos invasivos desnecessários).

## Estrutura do Projeto

```md
fiap-pos-tech-ia-para-devs-tech-challenge-fase-1/projeto-cancer-mama/
├── dash_app/
│   ├── app.py                  # Entrada principal da aplicação Dash
│   ├── requirements.txt        # Dependências do projeto
│   ├── assets/
│   │   └── styles.css          # Estilização customizada da interface
│   ├── data/
│   │   └── breast_cancer.csv   # Dataset utilizado
│   └── src/
│       ├── artifacts/
│       │   └── best_model.joblib # Modelo treinado persistido
│       ├── callbacks.py        # Lógica de interação e gráficos
│       ├── clinical_policy.py  # Definição de regras de negócio/limiares
│       ├── data_loader.py      # Carregamento e limpeza de dados
│       ├── layout.py           # Estrutura visual da aplicação
│       └── model.py            # Lógica de treino e predição
```

## Como Executar Localmente

- Requisitos
  - python versão: `3.12.0`
  - pip versão: `25.3`

- Clone o repositório:
  - ```git clone git@github.com:leojosants/fiap-pos-tech-ia-para-devs-tech-challenge-fase-1.git```
  - ```cd projeto-cancer-mama/dash_app```

- Crie um ambiente virtual e instale as dependências:
  - ```python -m venv venv```
  - ```source venv/bin/activate  # No Windows: venv\Scripts\activate```
  - ```pip install -r requirements.txt```

- Execute a aplicação:
  - ```python app.py```
  - ```Acesse no navegador: http://localhost:7860```

## Aviso Legal

- Esta ferramenta é um protótipo para fins educacionais e suporte à decisão. O diagnóstico final deve ser sempre realizado por um profissional médico qualificado.

## Autores

- Diego Pereira - RM369440
- Thiago Venceslau - RM369527
- Fernando Monin - RM369303
- Wellington José - RM369441
- Leonardo Oliveira - RM369985
