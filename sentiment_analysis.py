import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Carregar dados
data = pd.read_csv('data/comments.csv')
print(data.head())

# Pré-processamento
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['comentario'])
y = data['sentimento']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Prever
y_pred = model.predict(X_test)

# Avaliação
print(classification_report(y_test, y_pred))
