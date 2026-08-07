def feature_engineering(df_limpo):
    
    print(df_limpo.head())

    df_limpo['Total_Venda'] = df_limpo['Quantidade'] * df_limpo['Preco_Unitario']

    print(df_limpo.head())

    # ----- 1. Receita total -----
    receita_total = df_limpo['Total_Venda'].sum()
    print(f"\nReceita total: {receita_total:,.2f}")

    # ----- 2. Total de receita, por categoria -----
    receita_por_categoria = df_limpo.groupby('Categoria')['Total_Venda'].sum().sort_values(ascending = False)
    print(f"\nReceita por categoria:\n{receita_por_categoria}")

    # ----- 3. Total de receita -----
    produto_mais_vendido = df_limpo.groupby('Produto')['Quantidade'].sum().sort_values(ascending = False)
    print(f"\nProduto mais vendido:\n{produto_mais_vendido}")

    # ---- 4. Análise de vendas ao longo do tempo -----
    vendas_por_dia = df_limpo.set_index('Data_Compra').resample('D')['Total_Venda'].sum()
    print(f"\nVendas por dia (Primeiros 5 dias):\n{vendas_por_dia.head()}")
    
    return receita_por_categoria, produto_mais_vendido, vendas_por_dia