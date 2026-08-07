import seaborn as sns
import matplotlib.pyplot as plt

from config import FIGURE_SIZE, TITLE_SIZE, ESTILO_GRAFICO, LABEL_SIZE, LINESTYLE, MARKER, DPI, PATH

plt.rcParams['figure.figsize'] = FIGURE_SIZE

def configurar_estilo():
    """
    Configurar o estilo do padrão de gráfico
    """   
    sns.set_style(ESTILO_GRAFICO)
    
def grafico_bloxpot(x, titulo):
    """
    Função para criar um gráfico de boxplot
    """
    configurar_estilo()
        
    sns.boxplot(x = x)
    plt.title(titulo)
    
    plt.tight_layout()
    plt.savefig(PATH + titulo, dpi=DPI, bbox_inches='tight')
    plt.show()
    
def grafico_bar(
    dados,
    titulo,
    yLabel,
    xLabel,
    xTicks = 0):
    """
    Função para criar um gráfico de barras
    """
    
    dados.plot(kind = 'bar', color = 'skyblue')
    
    plt.title(titulo, fontsize = TITLE_SIZE)
    plt.ylabel(yLabel, fontsize = LABEL_SIZE)
    plt.xlabel(xLabel, fontsize = LABEL_SIZE)
    plt.xticks(rotation = xTicks)
    
    plt.tight_layout()
    plt.savefig(PATH + titulo, dpi=DPI, bbox_inches='tight')
    plt.show()
   
def grafico_barh(
    dados,
    titulo,
    yLabel,
    xLabel,
    inverterY = True
    ):
    """
    Função para criar um gráfico de barras horizontal
    """
    
    dados.plot(kind = 'barh', color = 'salmon')
    plt.title(titulo, fontsize = TITLE_SIZE)
    plt.ylabel(yLabel, fontsize = LABEL_SIZE)
    plt.xlabel(xLabel, fontsize = LABEL_SIZE)
    
    if inverterY:
        plt.gca().invert_yaxis()  # Inverter o eixo y para que o produto mais vendido apareça no topo  
    
    plt.tight_layout()
    plt.savefig(PATH + titulo, dpi=DPI, bbox_inches='tight')
    plt.show()
    
def grafico_line(
    dados,
    titulo,
    yLabel,
    xLabel,
    grid = True):
    """
    Função para criar um gráfico de linha
    """
    
    dados.plot(kind = 'line', marker = MARKER, linestyle = LINESTYLE)
    plt.title(titulo, fontsize = TITLE_SIZE)
    plt.ylabel(yLabel, fontsize = LABEL_SIZE)
    plt.xlabel(xLabel, fontsize = LABEL_SIZE)
    plt.grid(grid)
    
    plt.tight_layout()
    plt.savefig(PATH + titulo, dpi=DPI, bbox_inches='tight')
    plt.show()
    
def grafico_pie(dados):
    """
    Função para criar um gráfico de pizza
    """

    plt.pie(
        dados,
        labels = dados.index,
        autopct = '%1.1f%%',
        startangle = 180,
        colors = ['lightgreen',
                'orange',
                'lightcoral'],
        )
    plt.title('Distribuição do Status de Entrega')
    
    plt.tight_layout()
    plt.savefig(PATH + 'Distribuição do Status de Entrega', dpi=DPI, bbox_inches='tight')
    plt.show()   