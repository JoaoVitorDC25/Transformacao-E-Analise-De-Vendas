import seaborn as sns
import matplotlib.pyplot as plt

from config import FIGURE_SIZE
from config import ESTILO_GRAFICO

plt.rcParams['figure.figsize'] = FIGURE_SIZE

def configurar_estilo():
    """
    Configurar o estilo do padrão de gráfico
    """   
    sns.set_style(ESTILO_GRAFICO)
    
def grafico_bloxpot(x, title):
    """
    Função para criar um gráfico de boxplot
    """
    configurar_estilo()
    
    sns.boxplot(x = x)
    plt.title(title)
    plt.show()