import pandas as pd

from charts import grafico_bloxpot

def preprocessing(df_limpo):
    """
    Função para realizar o pré-processamento de dados
    """
    
    # ----- 1. Limpeza e pré-processamento de dados -----
    print("\n ----- Corrigindo os tipos de dados: ----- \n")

    #errors = 'coerce' faz com que valores inválidos sejam convertidos para NaN
    df_limpo['Preco_Unitario'] = pd.to_numeric(df_limpo['Preco_Unitario'], errors = 'coerce')

    df_limpo['Cliente_ID'] = pd.to_numeric(df_limpo['Cliente_ID'], errors = 'coerce').astype('Int64')

    # ------ 2. Tratando Valores Ausentes (NaN) -----
    print("\n ----- Tratando valores ausentes: ----- \n")

    media_qtd = df_limpo['Quantidade'].median()# Prence com o valor mediano da coluna Quantidade
    df_limpo.fillna({'Quantidade': media_qtd}, inplace = True)

    moda_status = df_limpo['Status_Entrega'].mode()[0] #P renche com o valor mais frequente (moda)
    df_limpo['Status_Entrega'] = df_limpo['Status_Entrega'].fillna(moda_status)

    df_limpo.dropna(subset = ['Preco_Unitario', 'Cliente_ID'], inplace = True)

    # ------ 3. Removendo Duplicatas -----
    print("\n ----- Removendo duplicatas: ----- \n")
    df_limpo.drop_duplicates(inplace = True)

    # ----- 4. Tratando Outliers -----
    print("\n ----- Tratando outliers: ----- \n")

    grafico_bloxpot(df_limpo['Quantidade'], 'Boxplot da Quantidade de Produtos Vendidos (Antes de tratar outliers)')

    limite_superior = df_limpo['Quantidade'].mean() + 3 * df_limpo['Quantidade'].std() # Remover valores acima de 3 desvios padrão da média
    df_limpo = df_limpo[df_limpo['Quantidade'] <= limite_superior]

    grafico_bloxpot(df_limpo['Quantidade'], 'Boxplot da Quantidade de Produtos Vendidos (Após tratar outliers)')

    # ----- 5. Verificando o dataframe limpo -----
    print("\n ----- Verificando o dataframe limpo: ----- \n")
    df_limpo.info()

    print(f"\n ----- Verificando valores ausentes: ----- \n {df_limpo.isnull().sum()}")
    print(f"\n ----- Verificando a presença de registros duplicados: ----- \n {df_limpo.duplicated().sum()}")
    
    return df_limpo
