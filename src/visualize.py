"""
Funções de Visualização para Análise de Sentimento.

Este arquivo contém funções para gerar gráficos e relatórios visuais a partir das métricas de classificação do modelo. A função principal é 'plot_classification_report', que gera um gráfico do relatório de classificação.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report

def plot_classification_report(report):
    """
    Função para visualizar o relatório de classificação em um gráfico.
    """
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    df_report = pd.DataFrame(report_dict).transpose()

    # Plotar o gráfico
    plt.figure(figsize=(8, 6))
    sns.heatmap(df_report.drop('accuracy', axis=1).iloc[:-1, :], annot=True, cmap="Blues", fmt='.2f')
    plt.title("Classification Report Heatmap")
    plt.show()
