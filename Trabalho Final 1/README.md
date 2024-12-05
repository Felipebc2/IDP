# Trabalho 1 ML - Extra Trees Classifier

**Alunos**: Felipe Barroso e Arthur Torquato

---

## 1. Introdução

### Introdução ao Algoritmo
O **ExtraTreesClassifier** foi utilizado para classificar o conjunto de dados de vinhos, separando as instâncias em vinhos de boa e má qualidade. Esse modelo, parte da família de métodos de árvores, seleciona divisões de maneira aleatória, o que o torna menos propenso ao sobreajuste e mais robusto em comparação a métodos tradicionais de Árvores de Decisão. O algoritmo é eficiente tanto para tarefas de classificação quanto de regressão.

**Principais Hiperparâmetros:**
- `n_estimators`: Número de árvores a serem treinadas no modelo.
- `max_depth`: Define a profundidade máxima da árvore para controlar o ajuste excessivo.
- `min_samples_split`: Determina o número mínimo de amostras exigido para dividir um nó.
- `min_samples_leaf`: Número mínimo de amostras exigido para formar uma folha.
- `max_features`: Define o número de características a serem consideradas para cada divisão.

---

## 2. Metodologia

### Técnicas de Otimização Utilizadas
1. **Randomized Search**:
   - Busca aleatória conduzida para explorar amplamente o espaço de hiperparâmetros.
   - Identificou rapidamente as regiões mais promissoras.
2. **Grid Search**:
   - Busca exaustiva focada nos hiperparâmetros mais relevantes identificados anteriormente.
3. **Bayes Search**:
   - Otimização Bayesiana para explorar de forma eficiente os melhores hiperparâmetros, utilizando uma abordagem probabilística.

### Hiperparâmetros Testados
- **`n_estimators`**: Valores testados entre 100 e 1000 para equilibrar o número de árvores e o tempo de treinamento.
- **`max_depth`**: Variou de `None` a profundidades de 10, 20 e 30, buscando balancear a capacidade de ajuste e evitar sobreajuste.
- **`min_samples_split`** e **`min_samples_leaf`**: Ajustados para controlar o tamanho das divisões e folhas, garantindo previsões estáveis.

### Métricas
- **Acurácia**: Proporção de predições corretas no conjunto de dados.
- **F1-score**: Combina precisão e recall, ideal para conjuntos desbalanceados.
- **Curva ROC e AUC**: Avaliação do desempenho do modelo na separação entre classes.

---

## 3. Resultados

### Resultados para Cada Técnica de Otimização

1. **Randomized Search**:
   - Acurácia: **82%**
   - Melhores hiperparâmetros:
     - `n_estimators`: 200
     - `min_samples_split`: 2
     - `min_samples_leaf`: 1
     - `max_features`: `'log2'`
     - `max_depth`: `None`

2. **Grid Search**:
   - Acurácia: **83%**
   - Melhores hiperparâmetros:
     - `bootstrap`: False
     - `max_depth`: `None`
     - `max_features`: `'log2'`
     - `min_samples_leaf`: 1
     - `min_samples_split`: 2
     - `n_estimators`: 200

3. **Bayes Search**:
   - Acurácia: **89%**
   - Melhores hiperparâmetros:
     - `max_depth`: `None`
     - `max_features`: `'log2'`
     - `min_samples_leaf`: 1
     - `min_samples_split`: 2
     - `n_estimators`: 200

### Resultados Adicionais
- **Curva ROC**:
  - AUC: **0.94**, indicando excelente desempenho na separação das classes.
- **Matriz de Confusão**:
  ```
  [[ 131 122 ]
   [  22 1025 ]]
  ```
  - **Verdadeiros Negativos (VN)**: 131
  - **Falsos Positivos (FP)**: 122
  - **Falsos Negativos (FN)**: 22
  - **Verdadeiros Positivos (VP)**: 1025

- **Relatório de Classificação**:
  | Classe | Precision | Recall | F1-Score | Support |
  |--------|-----------|--------|----------|---------|
  | 0      | 0.86      | 0.52   | 0.65     | 253     |
  | 1      | 0.89      | 0.98   | 0.93     | 1047    |
  | **Accuracy** | **0.89** | | | 1300 |
  | **Macro Avg** | 0.87 | 0.75 | 0.79 | 1300 |
  | **Weighted Avg** | 0.89 | 0.89 | 0.88 | 1300 |

---

## 4. Discussão

### Melhoria no Processo de Otimização
O uso sequencial de Randomized Search, Grid Search e Bayes Search provou ser eficiente na otimização do modelo. Entretanto, melhorias podem ser feitas, como o uso de **Early Stopping** para economizar tempo computacional em treinos desnecessários.

### Impacto dos Hiperparâmetros no Desempenho
- **`max_depth`**: Manter profundidade ilimitada ajudou a evitar o sobreajuste sem sacrificar a performance.
- **`min_samples_split`** e **`min_samples_leaf`**: Valores maiores resultaram em predições mais estáveis e menos suscetíveis a ruídos nos dados.
