from src.charts import grafico_bloxpot, grafico_bar, grafico_barh, grafico_line, grafico_pie


def visualization(receita_por_categoria, 
                  produto_mais_vendido, 
                  vendas_por_dia, 
                  df_limpo):
    """
    Função para criar visualizações de dados
    """
    # ----- 1. Receita por categoria -----
    grafico_bar(dados = receita_por_categoria,titulo='Receita por Categoria',yLabel='Receita (R$)',xLabel='Categoria',)

    # ---- 2. Quantidade Vendida por Produtor -----
    grafico_barh(dados = produto_mais_vendido, titulo = 'Quantidade Vendida por Produto', yLabel = 'Produto', xLabel = 'Quantidade Vendida', inverterY = True)

    # ----- 3. Tendencia de Vendas ao longo do tempo -----
    grafico_line(dados = vendas_por_dia, titulo = 'Tendência de Vendas Diárias', yLabel = 'Receita (R$)', xLabel = 'Data de Compra', grid = True)

    # ----- 4. Distribuição do Status de Entrega -----
    status_entrega_counts = df_limpo['Status_Entrega'].value_counts()

    grafico_pie(dados = status_entrega_counts)
    