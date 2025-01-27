# Análise de Sentimentos com Naive Bayes

Este projeto tem como objetivo realizar a **análise de sentimentos** em resenhas de filmes utilizando o algoritmo **Naive Bayes**. O modelo foi treinado com o dataset **IMDb** disponibilizado pelo **NLTK**, e classifica as resenhas como **positivas** ou **negativas**.

---

## 📖 Descrição

Neste projeto, usamos o **Naive Bayes** para treinar um modelo de **classificação de texto** e prever o sentimento de resenhas de filmes. O dataset utilizado é composto por resenhas de filmes e seus respectivos sentimentos (**positivo** ou **negativo**).

---

## 📊 Resultados

O modelo foi treinado, testado e avaliado com as seguintes **métricas de performance**:

- **Acurácia**: 80%  
- **Precisão (Precision)**:
  - Para resenhas **negativas**: 77%  
  - Para resenhas **positivas**: 83%  
- **Revocação (Recall)**:
  - Para resenhas **negativas**: 85%  
  - Para resenhas **positivas**: 75%  
- **F1-Score**:
  - Para resenhas **negativas**: 0.81  
  - Para resenhas **positivas**: 0.79  

Essas métricas indicam que o modelo apresenta um bom equilíbrio entre **precisão** e **capacidade de identificar corretamente** as resenhas de cada classe.

---

## 🛠️ Instalação e Configuração

Para rodar este projeto, você precisará configurar o ambiente adequadamente. Abaixo, você encontrará as instruções passo a passo.

### 1. Requisitos do Sistema

- **Python** 3.9 ou superior
- **Sistema Operacional**: Windows, macOS ou Linux

### 2. Dependências

Este projeto usa as seguintes bibliotecas e frameworks:

- **NLTK**: Para o processamento de linguagem natural e carregamento do dataset IMDb.
- **Scikit-learn**: Para a implementação do modelo Naive Bayes.
- **Pandas**: Para manipulação de dados.
- **Matplotlib**: Para visualização de gráficos.
- **Seaborn**: Para visualizações mais avançadas.
- **Plotly**: Para gráficos interativos, como o fluxograma.

### 3. Instalação das Dependências

Antes de rodar o código, é necessário instalar todas as dependências do projeto. Para isso, siga os passos abaixo:

#### Passo 1: Clone o repositório

```bash
git clone https://github.com/seu-usuario/sentiment-analysis.git
cd sentiment-analysis
```

#### Passo 2: Crie um ambiente virtual (opcional, mas recomendado)

Se você deseja usar um ambiente virtual, pode criar e ativar um com os seguintes comandos:

- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### Passo 3: Instale as dependências

Com o ambiente ativado, instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

Esse comando vai instalar **NLTK**, **Scikit-learn**, **Pandas**, **Matplotlib**, **Seaborn** e **Plotly**.

### 4. Baixar o Dataset IMDb

O dataset IMDb será automaticamente baixado pelo NLTK ao rodar o código, mas caso você deseje baixá-lo manualmente, basta rodar o seguinte comando no Python:

```python
import nltk
nltk.download('movie_reviews')
```

### 5. Rodando o Código

Após configurar o ambiente e instalar as dependências, você pode rodar o código principal. Dependendo de sua preferência, você pode executar o código de uma das seguintes formas:

- **Notebook Jupyter/Colab**: Abra o arquivo `notebooks/sentiment_analysis.ipynb` no **Jupyter Notebook** ou **Google Colab** e execute as células.
  
- **Script Python**: Se preferir rodar o código como script, basta executar o arquivo `main_code.py`:

  ```bash
  python main_code.py
  ```

### 6. Executando o Modelo

Ao rodar o código, o modelo será treinado automaticamente com o dataset IMDb e, em seguida, avaliado com as métricas de desempenho: **Acurácia**, **Precisão**, **Recall** e **F1-Score**.

O código também gera gráficos interativos e visualizações, como:

- **Gráfico de Acurácia**: Mostra a evolução da acurácia do modelo durante o treinamento.
- **Matriz de Confusão**: Mostra a performance do modelo em cada classe (positiva e negativa).
- **Gráfico de Métricas**: Compara Precision, Recall e F1-Score para as classes positivas e negativas.
- **Fluxograma do Projeto**: Um Sankey Diagram mostrando o fluxo do projeto, desde o carregamento dos dados até a previsão.
- **Exemplo de Entrada e Saída**: Mostra um comentário analisado pelo modelo com a saída prevista.

## 📊 Resultados Visuais

1. **Gráfico de Acurácia**: Mostra a evolução da acurácia do modelo durante o treinamento.

<p align="center"> <img src="images/Gráfico de Acurácia .png" alt="Gráfico de Acurácia" width="70%"> </p>

**Visualizar Gráfico de Acurácia**

(https://colab.research.google.com/drive/1zwU09L2hXFuFZFcfILG_vPO_4EUMH7T8#scrollTo=dHgRkxCTBP3O&line=1&uniqifier=1))

2. **Matriz de Confusão**: Mostra a matriz de confusão normalizada, detalhando a performance do modelo em cada classe.

   **Visualizar Matriz de confusão**

   (https://colab.research.google.com/drive/1zwU09L2hXFuFZFcfILG_vPO_4EUMH7T8#scrollTo=dHgRkxCTBP3O&line=1&uniqifier=1))

<p align="center"> <img src="images/Matriz de confusão.png" alt="Matriz de Confusão" width="70%"> </p>

3. **Gráfico de Métricas**: Compara **Precision**, **Recall** e **F1-Score** para as classes **positiva** e **negativa**.

<p align="center"> <img src="images/Métricas de Desempenho.png" alt="Gráfico de Métricas" width="70%"> </p>

**Visualizar Gráfico de Métricas**

(https://colab.research.google.com/drive/1zwU09L2hXFuFZFcfILG_vPO_4EUMH7T8#scrollTo=dHgRkxCTBP3O&line=1&uniqifier=1))

4. **Fluxograma Interativo**: Um Sankey Diagram que ilustra o fluxo do projeto, desde o carregamento dos dados até a previsão. O fluxograma exibe de forma visual como os dados passam pelas diferentes etapas do processo, com cada uma representada em uma linha distinta:

  - Carregamento dos dados: O dataset IMDb é carregado através do NLTK.
  - Pré-processamento: As resenhas de filmes são limpas e transformadas para que possam ser analisadas pelo modelo.
  - Treinamento: O modelo Naive Bayes é treinado com as resenhas processadas.
  - Avaliação: O modelo é avaliado com as métricas de acurácia, precisão, recall e F1-score.
  - Previsão: O modelo realiza a classificação de novas resenhas como positivas ou negativas.

<p align="center"> <img src="images/Fluxograma do projeto.png" alt="Fluxo do projeto" width="70%"> </p>

**Visualizar Fluxograma Interativo**

(https://colab.research.google.com/drive/1zwU09L2hXFuFZFcfILG_vPO_4EUMH7T8#scrollTo=dHgRkxCTBP3O&line=1&uniqifier=1))

5. **Exemplo de Entrada e Saída**: Mostra um comentário analisado pelo modelo com a saída prevista (sentimento).

<p align="center"> <img src="images/Exemplo-entrada e saída.png" alt="Exemplo de Entrada e Saída" width="70%"> </p>

**Visualizar Exemplo de entrada e saída**

(https://colab.research.google.com/drive/1zwU09L2hXFuFZFcfILG_vPO_4EUMH7T8#scrollTo=dHgRkxCTBP3O&line=1&uniqifier=1))


---



### 7. Resultados

Após a execução, os resultados serão exibidos no console e os gráficos interativos serão gerados automaticamente.

---

## 🎉 Contribuições

Contribuições são **bem-vindas**! Se você tiver sugestões de melhorias ou quiser adicionar novos recursos, sinta-se à vontade para **fazer um fork** deste repositório e enviar um **pull request**.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo `LICENSE` para mais detalhes.

---

