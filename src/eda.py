def eda(df_vendas):
    # Informações do dataframe
    print(f"\n ----- Informações do dataframe: ----- \n")
    df_vendas.info()
    print(f"\n ----- Verificando valores ausentes: ----- \n {df_vendas.isnull().sum()}")
    print(f"\n ----- Verificando a presença de registros duplicados: ----- \n {df_vendas.duplicated().sum()}")
    print(f"\n ----- Estatísticas descritivas para colunas numericas: ----- \n {df_vendas.describe()}")
    print(f"\n ----- Estatísticas descritivas para colunas categóricas: ----- \n {df_vendas.describe(include = 'object')}")
    print(f"\n ----- Verificando tipos de dados: ----- \n {df_vendas.dtypes}")