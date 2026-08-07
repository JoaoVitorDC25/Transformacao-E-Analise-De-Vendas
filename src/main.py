import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from eda import eda
from preprocessing import preprocessing
from data_generator import data_generator
from feature_engineering import feature_engineering
from visualization import visualization

# ----- GERADOR DE DADOS -----
df_vendas = data_generator()

# ----- EDA -----
eda(df_vendas)

# ----- 1. LIMPEZA E PRÉ-PROCESSAMENTO DE DADOS -----
df_limpo = preprocessing(df_vendas.copy())

# ----- 2. ENGENHARIA DE ATRIBUTOS -----
data_feature_engineering = feature_engineering(df_limpo)

# ----- 4. VISUALIZAÇÃO DE DADOS -----
visualization(*data_feature_engineering, df_limpo)
