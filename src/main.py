import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import preprocessing
from data_generator import data_generator
from visualization import visualization
from charts import grafico_bloxpot

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

preprocessing(df_limpo)

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






