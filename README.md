

# Análise de Sentimentos com Naive Bayes

Este projeto tem como objetivo realizar a **análise de sentimentos** em resenhas de filmes utilizando o algoritmo **Naive Bayes**. O modelo foi treinado com o **dataset IMDb** disponibilizado pelo **NLTK**, e classifica as resenhas como **positivas** ou **negativas**.

## Descrição

Neste projeto, usamos o **Naive Bayes** para treinar um modelo de classificação de texto e prever o sentimento de resenhas de filmes. O dataset utilizado é composto por resenhas de filmes e seus respectivos sentimentos (positivo ou negativo).

O modelo foi treinado, testado e avaliado com as seguintes métricas de performance:
- **Acurácia**: 80%
- **Precision** (Precisão): 77% para resenhas negativas, 83% para resenhas positivas.
- **Recall** (Revocação): 85% para resenhas negativas, 75% para resenhas positivas.
- **F1-Score**: 0.81 para resenhas negativas, 0.79 para resenhas positivas.

## Instalação

Para rodar este projeto, é necessário ter o Python instalado no seu computador. As bibliotecas que usamos são:

- **pandas**
- **scikit-learn**
- **nltk**

### Como instalar as dependências

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/sentiment-analysis.git
    cd sentiment-analysis
    ```

2. Instale as dependências com o `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. Baixe os dados do **NLTK**:

    No código Python, o **NLTK** irá automaticamente baixar o dataset de resenhas de filmes. Se você for rodar localmente, apenas execute:

    ```python
    import nltk
    nltk.download('movie_reviews')
    ```

## Como rodar o código

Após configurar o ambiente, você pode rodar o código principal para treinar e avaliar o modelo:

1. Abra o arquivo `main_code.py` ou o notebook `sentiment_analysis.ipynb`.
2. Execute o código para treinar o modelo e avaliar seu desempenho.

## Resultados

O modelo de **Naive Bayes** foi avaliado com as seguintes métricas:

#### **Acurácia**:
- **80% de acerto** no total, ou seja, o modelo acertou 80% das previsões.

#### **Precisão**:
- **Para resenhas negativas**: **77%** de precisão.
- **Para resenhas positivas**: **83%** de precisão.

#### **Revocação**:
- **Para resenhas negativas**: **85%** de recall.
- **Para resenhas positivas**: **75%** de recall.

#### **F1-Score**:
- **Para resenhas negativas**: **0.81**.
- **Para resenhas positivas**: **0.79**.

Com essas métricas, o modelo mostra um bom equilíbrio entre precisão e capacidade de identificar corretamente as resenhas de cada classe.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou quiser adicionar novos recursos, fique à vontade para fazer um **fork** deste repositório e enviar um **pull request**.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---


