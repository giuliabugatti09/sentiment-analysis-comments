"""
Treinamento e Avaliação do Modelo de Análise de Sentimento.

Este arquivo contém a função 'train_and_evaluate_model', que treina um modelo de Naive Bayes utilizando as características extraídas no processo de pré-processamento, e avalia seu desempenho utilizando métricas de classificação.
"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def train_and_evaluate_model(X, y):
    """
    Função para treinar o modelo e avaliar seu desempenho.
    """
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar modelo
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    # Prever
    y_pred = model.predict(X_test)
    
    # Avaliação
    return classification_report(y_test, y_pred)
