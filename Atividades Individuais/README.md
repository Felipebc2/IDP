
---

## 🖥 Atividades Individuais

**Air Quality Dataset:**
https://github.com/klaytoncastro/idp-machinelearning/tree/main/airquality

**Bank Dataset:**
https://github.com/klaytoncastro/idp-machinelearning/tree/main/bank

**California Dataset:**
https://github.com/klaytoncastro/idp-machinelearning/tree/main/california

**Mall Customers Dataset:**
https://github.com/klaytoncastro/idp-machinelearning/tree/main/clustering

**Iris Dataset:**
https://github.com/klaytoncastro/idp-machinelearning/tree/main/iris

**Sentiment Analysis**
https://github.com/klaytoncastro/idp-machinelearning/tree/main/nlp

---

## 🌪️ Air Quality Dataset

<details>

# Análise do Air Quality Dataset

Este repositório contém um notebook em Python com a análise exploratória de dados e aplicação de técnicas de Machine Learning no **Air Quality Dataset**, como parte das atividades práticas de aprendizado.

## Estrutura do Repositório

- **`Airquality_Felipe_Barroso.ipynb`**: Notebook principal contendo todas as etapas do projeto.
- **`AirQualityUCI.csv`**: Arquivo com os dados originais utilizados no projeto.

## Objetivo

O objetivo principal deste projeto foi analisar a qualidade do ar com base em medições de gases e variáveis climáticas, além de criar modelos preditivos para estimar concentrações de CO no ar.

## Etapas Realizadas

1. **Carregamento e Limpeza de Dados**
   - Importação do dataset em formato CSV.
   - Tratamento de valores ausentes preenchendo com a mediana.
   - Remoção de colunas irrelevantes ou não numéricas.

2. **Análise Exploratória de Dados (EDA)**
   - Geração de estatísticas descritivas.
   - Visualizações gráficas das distribuições das variáveis.
   - Matriz de correlação para identificar relações entre variáveis.

3. **Pré-processamento**
   - Seleção de variáveis independentes (features) e dependente (target).
   - Divisão do dataset em conjuntos de treino e teste.

4. **Modelagem de Machine Learning**
   - Treinamento de um modelo de Random Forest para prever concentrações de CO.
   - Avaliação do modelo com métricas:
     - Mean Squared Error (MSE)
     - R-squared (R²)

5. **Resultados**
   - Comparação entre os valores reais e previstos para avaliar a eficácia do modelo.

6. **Conclusões**
   - O modelo conseguiu capturar padrões relevantes no dataset, apresentando um desempenho satisfatório para predição de CO.

## Ferramentas Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

## Observações

- Certifique-se de que o arquivo `AirQualityUCI.csv` esteja no mesmo diretório do notebook ao executá-lo.

</details>

---

## 🏦 Bank Dataset

<details>

# Análise do Bank Dataset

Este repositório contém um notebook em Python com a análise exploratória de dados e aplicação de técnicas de Machine Learning no **Bank Dataset**, parte das atividades práticas do curso de Machine Learning.

## Estrutura do Repositório

- **`Bank_Dataset_Felipe_Barroso.ipynb`**: Notebook principal contendo todas as etapas do projeto.
- **`Bank_Data.csv`**: Arquivo com os dados originais utilizados no projeto.

## Objetivo

O objetivo principal deste projeto foi analisar os dados de uma campanha de marketing de uma instituição bancária e criar modelos preditivos para estimar a probabilidade de um cliente aceitar um produto bancário (como um depósito a prazo fixo).

## Etapas Realizadas

1. **Carregamento dos Dados**
   - Importação do arquivo `Bank_Data.csv` para o ambiente de trabalho.
   - Inspeção inicial dos dados para compreender suas variáveis e estrutura.

2. **Análise Exploratória de Dados (EDA)**
   - Estatísticas descritivas das variáveis.
   - Visualizações gráficas para identificar padrões e relações entre os dados.
   - Tratamento de dados ausentes e outliers.

3. **Pré-processamento**
   - Conversão de variáveis categóricas para representações numéricas.
   - Normalização de variáveis para uso em modelos de aprendizado de máquina.
   - Divisão dos dados em conjuntos de treinamento e teste.

4. **Modelagem**
   - Treinamento de diferentes algoritmos de classificação:
     - Regressão Logística
     - Árvore de Decisão
     - Random Forest
   - Avaliação de desempenho dos modelos utilizando métricas como:
     - Acurácia
     - Precisão
     - Recall
     - F1-score

5. **Resultados**
   - Comparação entre os modelos com base nas métricas de avaliação.
   - Identificação do melhor modelo para o problema proposto.

6. **Conclusões**
   - Insights gerados a partir dos dados.
   - Discussão sobre a aplicabilidade do modelo no mundo real.

## Ferramentas Utilizadas

- Python (bibliotecas: pandas, numpy, matplotlib, seaborn, scikit-learn)
- Jupyter Notebook

## Observações

- Certifique-se de que o arquivo `Bank_Data.csv` esteja no mesmo diretório do notebook.

</details>

---

## ⛱️ California Dataset

<details>

# Análise do California Housing Dataset

Este repositório contém um notebook em Python com a análise exploratória, pré-processamento e aplicação de modelos de machine learning no **California Housing Dataset**.

## Estrutura do Repositório

- **`california_housing_analysis.ipynb`**: Notebook contendo a análise completa e modelagem dos dados.
- **`california_housing.csv`**: Arquivo com os dados originais utilizados no projeto.

## Objetivo

O objetivo principal deste projeto foi prever o valor médio de casas em diferentes regiões da Califórnia, utilizando variáveis como idade média das casas, número médio de quartos, ocupação média, latitude, longitude, entre outras.

## Etapas do Projeto

### 1. Análise Exploratória de Dados (EDA)
- **Distribuição das Variáveis**: Analisamos as distribuições das variáveis para identificar outliers e entender características gerais do conjunto de dados.
- **Correlação**: Exploramos as correlações entre as variáveis preditoras e a variável alvo (`MedHouseVal`).
- **Gráficos**:
  - Histogramas para distribuição de variáveis.
  - Matriz de correlação para identificar relações entre as variáveis.

### 2. Pré-processamento de Dados
- **Tratamento de Valores Ausentes**: Identificação e tratamento de valores ausentes (se aplicável).
- **Normalização**: Variáveis foram normalizadas com `StandardScaler` para garantir que todas as variáveis estivessem na mesma escala.
- **Divisão dos Dados**: O dataset foi dividido em conjuntos de treino (80%) e teste (20%) para validação dos modelos.

### 3. Modelagem
Foram aplicados e avaliados diferentes algoritmos de regressão para prever o valor médio das casas:
- **Regressão Linear**: Modelo básico para estabelecer uma linha de base.
- **Árvore de Decisão**: Modelo não linear para capturar interações complexas.
- **Random Forest**: Modelo de ensemble para melhorar a performance e reduzir overfitting.
- **SVR (Support Vector Regressor)**: Modelo de regressão baseado no algoritmo SVM.
- **Gradient Boosting Machines**: Implementação com `GradientBoostingRegressor`.

### 4. Avaliação e Interpretação
- **Métricas de Avaliação**:
  - **MAE (Mean Absolute Error)**: Erro médio absoluto.
  - **MSE (Mean Squared Error)**: Erro quadrático médio.
  - **R² (Coeficiente de Determinação)**: Mede a proporção da variância explicada pelo modelo.
- **Gráficos de Valores Reais x Preditos**:
  - Para cada modelo, geramos gráficos de dispersão comparando os valores reais e os previstos.

## Ferramentas Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

## Resultados

- **Modelos Avaliados**:
  - Regressão Linear apresentou bom desempenho como modelo inicial.
  - Random Forest e Gradient Boosting Machines se destacaram pelo melhor equilíbrio entre bias e variância.
- **Insights**:
  - Variáveis como `MedInc` (Renda Média) mostraram forte correlação com o valor médio das casas.
  - Modelos ensemble como Random Forest e Gradient Boosting são mais adequados para capturar padrões complexos.

</details>

---

## 🏢 Mall Customers Dataset

<details>


</details>

---

## 👁️ Iris Dataset

<details>


</details>

---

## 💕 Sentiment Analysis

<details>


</details>

---
