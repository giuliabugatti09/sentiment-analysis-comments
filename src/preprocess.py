"""
Pré-processamento de dados para análise de sentimento.

Este arquivo contém funções para limpar e transformar os dados de texto em um formato numérico utilizável pelo modelo de machine learning. A principal função é a 'preprocess_data', que aplica uma limpeza no texto e o transforma em uma matriz de características.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import string

def clean_text(text):
    """
    Função para limpar o texto: converte para minúsculas e remove pontuação.
    """
    text = text.lower()  # Converter para minúsculas
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remover pontuação
    return text

def preprocess_data(data):
    """
    Função para processar os dados: limpeza do texto e conversão para uma matriz numérica.
    """
    # Limpar o texto
    data['comentario'] = data['comentario'].apply(clean_text)
    
    # Vectorização (transforma o texto em uma matriz numérica)
    vectorizer = CountVectorizer(stop_words='english')  # Remove stop words automaticamente
    X = vectorizer.fit_transform(data['comentario'])  # X é a matriz de características
    y = data['sentimento']  # y são as labels
    
    return X, y
