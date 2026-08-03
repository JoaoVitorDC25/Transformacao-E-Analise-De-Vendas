import seaborn as sns
import matplotlib.pyplot as plt

from config import FIGURE_SIZE, TITLE_SIZE, ESTILO_GRAFICO, LABEL_SIZE

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
    
def grafico_bar(
    dados,
    titulo,
    yLabel,
    xLabel,
    xTicks = 0
    ):

    dados.plot(kind = 'bar', color = 'skyblue')
    
    plt.title(titulo, fontsize = TITLE_SIZE)
    plt.ylabel(yLabel, fontsize = LABEL_SIZE)
    plt.xlabel(xLabel, fontsize = LABEL_SIZE)
    plt.xticks(rotation = xTicks)
    plt.show()
#plt.ylabel('Receita (R$)')
#plt.xlabel('Categoria')
#plt.xticks(rotation = 0)

   
#def grafico_barh():
    
#def grafico_line():
    
#def grafico_pie():
    