import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_generator import data_generator
from src.visualization import visualization

df_vendas = data_generator()

# ----- EDA -----
# Informações do dataframe
print(f"\n ----- Informações do dataframe: ----- \n")
df_vendas.info()

print(f"\n ----- Verificando valores ausentes: ----- \n {df_vendas.isnull().sum()}")

print(f"\n ----- Verificando a presença de registros duplicados: ----- \n {df_vendas.duplicated().sum()}")

print(f"\n ----- Estatísticas descritivas para colunas numericas: ----- \n {df_vendas.describe()}")

print(f"\n ----- Estatísticas descritivas para colunas categóricas: ----- \n {df_vendas.describe(include = 'object')}")

print(f"\n ----- Verificando tipos de dados: ----- \n {df_vendas.dtypes}")

# ----- 1. Limpeza e pré-processamento de dados -----

df_limpo = df_vendas.copy()

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

# ----- ENGENHARIA DE ATRIBUTOS -----
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

# ----- VISUALIZAÇÃO DE DADOS -----
visualization(receita_por_categoria, produto_mais_vendido, vendas_por_dia, df_limpo)






