import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pandas as pd

# Baixar o dataset do IMDb via NLTK
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews

# Preparar os dados: criar um DataFrame com as reviews e seus sentimentos
data = pd.DataFrame({
    'comentario': [' '.join(movie_reviews.words(fileid)) for fileid in movie_reviews.fileids()],
    'sentimento': [fileid.split('/')[0] for fileid in movie_reviews.fileids()]
})

# Mostrar as primeiras linhas do dataset
print(data.head())

# Pré-processamento: converter os comentários em uma matriz de contagem de palavras
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['comentario'])
y = data['sentimento']

# Dividir os dados em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Prever os sentimentos no conjunto de teste
y_pred = model.predict(X_test)

# Avaliação do modelo
print(classification_report(y_test, y_pred))
