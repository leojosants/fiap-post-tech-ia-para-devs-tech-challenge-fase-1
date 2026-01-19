
# FIAP - Pós Tech -- Curso IA para Devs

## Tech Challenge -- Fase 1 - Welcome to IA para Devs

### Sistema Inteligente de Suporte ao Diagnóstico em Saúde da Mulher

---

### 📝 Descrição do Projeto

Este projeto consiste em um **sistema de suporte ao diagnóstico em saúde da mulher** desenvolvido como parte do Tech Challenge – Fase 1.  

O objetivo principal é **auxiliar profissionais de saúde na identificação precoce de tumores mamários**, classificando-os como benignos ou malignos a partir de dados estruturados de exames médicos.  

⚠️ **Atenção:** Este sistema **não substitui avaliação médica**, sendo apenas uma ferramenta de apoio à decisão clínica. A responsabilidade final permanece com o profissional de saúde.

---

### 🚀 Funcionalidades

O sistema oferece:

1. **Seleção do contexto clínico e paciente** via interface interativa.
2. **Geração de análise clínica automatizada**, exibindo:
   - Resultado da classificação (benigno/maligno)
   - Probabilidade estimada
   - Indicadores visuais de risco
   - Comparação com limiar clínico
3. **Explicabilidade das decisões** do modelo via SHAP:
   - Summary Plot (visão global)
   - Waterfall Plot (visão individual por paciente)
4. **Armazenamento local dos resultados**, permitindo recuperar análises anteriores.
5. **Dashboard responsivo**, visualmente organizado em cards e gráficos interativos.

---

### 📊 Dataset Utilizado

- **Breast Cancer Wisconsin (Diagnostic)**  
  - Contém atributos extraídos de exames de tumores mamários.  
  - Classes: `B` (Benigno) e `M` (Maligno).  
  - Fonte acadêmica amplamente utilizada em ML para saúde.  

---

### 🛠 Requisitos do Sistema

- **Python 3.12**
- **Pip 25.3** ou superior

### Principais Bibliotecas

- pandas, numpy  
- plotly, dash  
- scikit-learn  
- shap  
- joblib  

### Instale as dependências com

```bash
pip install -r requirements.txt
```

### 📂 Estrutura de Arquivos

```bash
fiap-2025-tech-challenge-fase-/
│
├─ data/raw/breast_cancer.csv          # Dataset original
├─ models/                             # Modelos treinados (Random Forest, etc.)
├─ testes/notebooks/saude_mulher_ml.ipynb  # Notebook narrativo completo
├─ requirements.txt                     # Bibliotecas
└─ README.md                            # Este arquivo
```

### ⚡ Como Clonar e Executar

1 - Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

2 - Crie e ative um ambiente virtual:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

3 - Instale as dependências:

```bash
pip install -r requirements.txt
```

### 📚 Notebook de Demonstração

- O notebook tests/notebooks/saude_mulher_ml.ipynb contém:
  - Todo o passo a passo da análise de dados
  - Treinamento e avaliação dos modelos
  - Explicabilidade com SHAP
  - Relato narrativo para apresentação do projeto
  - Ele pode ser usado para documentação da apresentação da banca FIAP.

### ⚖️ Observações Importantes

- Sistema não substitui avaliação médica.
- Modelo treinado com dataset acadêmico limitado.
- Para aplicações clínicas reais, seria necessária validação externa e integração com sistemas hospitalares.

### Autores

- Diego Pereira - RM369440
- Thiago Venceslau - RM369527
- Fernando Monin - RM369303
- Wellington José - RM369441
- Leonardo Oliveira - RM369985
  