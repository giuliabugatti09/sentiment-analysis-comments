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

📊 Resultados Visuais
1. Gráfico de Acurácia:
Mostra a evolução da acurácia do modelo durante o treinamento.
<p align="center"> <img src="images/gráfico de acurácia.png" alt="Gráfico de Acurácia" width="70%"> </p>

2. Matriz de Confusão:
Mostra a matriz de confusão normalizada, detalhando a performance do modelo em cada classe.
<p align="center"> <img src="images/Matriz de confusão.png" alt="Matriz de Confusão" width="70%"> </p>

3. Gráfico de Métricas:
Compara Precision, Recall e F1-Score para as classes positiva e negativa.
<p align="center"> <img src="images/Métricas de Desempenho.png" alt="Gráfico de Métricas" width="70%"> </p>

4. Fluxograma Interativo:
Um Sankey Diagram que ilustra o fluxo do projeto, desde o carregamento dos dados até a previsão.
<p align="center"> <img src="images/Fluxograma do projeto.png" alt="Fluxo do projeto" width="70%"> </p>

5. Exemplo de Entrada e Saída:
Mostra um comentário analisado pelo modelo com a saída prevista (sentimento).
<p align="center"> <img src="images/Exemplo-entrada e saída.png" alt="Exemplo de Entrada e Saída" width="70%"> </p>

---

## 🛠️ Instalação

Para rodar este projeto, é necessário ter o **Python 3.x** instalado no seu computador. As bibliotecas utilizadas são:

NLTK
Scikit-learn
Pandas
Matplotlib
Seaborn
Plotly

### Como instalar as dependências

Clone este repositório:

```
git clone https://github.com/seu-usuario/sentiment-analysis.git
cd sentiment-analysis
```

Instale as dependências com o **pip**:

```
pip install -r requirements.txt
```

Baixe os dados do **NLTK**:

No código Python, o **NLTK** irá automaticamente baixar o dataset de resenhas de filmes. Se você for rodar localmente, apenas execute:

```python
import nltk
nltk.download('movie_reviews')
```

---

## ▶️ Como Rodar o Código

Após configurar o ambiente, você pode rodar o código principal para **treinar** e **avaliar** o modelo:

1. Abra o arquivo `main_code.py` ou o notebook `sentiment_analysis.ipynb`.
2. Execute o código para **treinar o modelo** e avaliar seu desempenho.

---

## 🎉 Contribuições

Contribuições são **bem-vindas**! Se você tiver sugestões de melhorias ou quiser adicionar novos recursos, sinta-se à vontade para **fazer um fork** deste repositório e enviar um **pull request**.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo `LICENSE` para mais detalhes.
