# Relatório de Análise de Clusters em Dados de Academia

**Alunos**: Lucas Narita, Felipe Barroso, Arthur Torquato

---

## Objetivo
O presente trabalho tem como objetivo identificar padrões em dados de usuários de uma academia, agrupando-os em clusters para personalizar recomendações de treino. A motivação está na crescente demanda por soluções baseadas em dados para melhorar os treinos e os resultados de praticantes de musculação, oferecendo treinos mais adequados às suas características e objetivos.

---

## Metodologia

### Dados Utilizados
- **Dataset**: Dados de 973 usuários com 14 atributos, incluindo:
  - Idade
  - Peso
  - Altura
  - Frequência semanal de treino
  - Calorias queimadas, entre outros.

### Técnicas Aplicadas
1. **Análise Exploratória**:
   - Histogramas e matriz de correlação para identificar padrões e relações entre variáveis.
2. **Clusterização (K-Means)**:
   - Método do cotovelo indicou 4 clusters ideais.
3. **Redução de Dimensionalidade (PCA)**:
   - Aplicada para visualização dos clusters em 2 dimensões.
4. **Ferramentas**:
   - Python (bibliotecas: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`).

---

## Resultados

### Clusters Identificados:
1. **Cluster 0**: Usuários jovens, alta frequência semanal e baixo percentual de gordura.
2. **Cluster 1**: Alta duração de treinos, menor frequência semanal.
3. **Cluster 2**: Usuários mais velhos com menor intensidade de treino.
4. **Cluster 3**: Usuários com maior peso e percentual de gordura.

### Gráficos Relevantes:
- **Distribuição de Gênero por Cluster**:
  - Maior proporção de mulheres nos Clusters 0 e 1.
- **Tipos de Treino**:
  - Yoga e Cardio predominam nos Clusters 0 e 1.
  - Treino de força predominante no Cluster 3.
- **Visualização PCA**:
  - Clusters bem separados em duas dimensões.

---

## Conclusão
O modelo de clusterização mostrou-se eficaz ao identificar padrões claros no comportamento dos usuários. Os resultados podem ser aplicados para personalizar recomendações, melhorando a experiência dos clientes.

### Limitações e Melhorias:
- **Limitações**:
  - A análise não considera aspectos qualitativos, como preferências pessoais ou lesões.
- **Melhorias**:
  - Incluir mais variáveis (e.g., alimentação, histórico médico).
  - Testar outros algoritmos de clusterização (e.g., DBSCAN, GMM).
