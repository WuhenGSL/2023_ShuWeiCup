"""tar，char数据不满足正态性"""
import pandas as pd
from scipy.stats import shapiro, levene

data1 = pd.read_csv('./data/DFA_CE_data.csv')
data2 = pd.read_csv('./data/DFA_LG_data.csv')

CE_tar_yield = data1['Tar yield']
LG_tar_yield = data2['Tar yield']
CE_water_yield = data1['Water yield']
LG_water_yield = data2['Water yield']
CE_char_yield = data1['Char yield']
LG_char_yield = data2['Char yield']
CE_syngas_yield = data1['Syngas yield']
LG_syngas_yield = data2['Syngas yield']

ce_yield_data = [CE_tar_yield, CE_water_yield, CE_char_yield, CE_syngas_yield]
lg_yield_data = [LG_tar_yield, LG_water_yield, LG_char_yield, LG_syngas_yield]

# 定义一个函数进行正态性检验
def normality_test(data, label):
    stat, p_value = shapiro(data)
    print(f"Shapiro-Wilk 正态性检验结果 ({label}):")
    print(f"统计值 (W): {stat}")
    print(f"P-value: {p_value}")

# 定义一个函数进行方差齐性检验
def homogeneity_of_variance_test(data1, data2, label1, label2):
    stat, p_value = levene(data1, data2)
    print(f"Levene's 方差齐性检验结果 ({label1} vs {label2}):")
    print(f"统计值 (W): {stat}")
    print(f"P-value: {p_value}")

# 对CE的各个yield进行正态性检验
for i, ce_yield in enumerate(ce_yield_data):
    normality_test(ce_yield, f'CE_{i+1}_yield')

# 对LG的各个yield进行正态性检验
for i, lg_yield in enumerate(lg_yield_data):
    normality_test(lg_yield, f'LG_{i+1}_yield')

# 对各个yield进行方差齐性检验
for i in range(len(ce_yield_data)):
    homogeneity_of_variance_test(ce_yield_data[i], lg_yield_data[i], f'CE_{i+1}_yield', f'LG_{i+1}_yield')

data1 = pd.read_csv('./data/DFA_CE_Gas_Yield.csv')
data2 = pd.read_csv('./data/DFA_LG_Gas_Yield.csv')

CE_H2 = data1['H2']
LG_H2 = data2['H2']
CE_CO = data1['CO']
LG_CO = data2['CO']
CE_CO2 = data1['CO2']
LG_CO2 = data2['CO2']
CE_CH4 = data1['CH4']
LG_CH4 = data2['CH4']
CE_C2H6 = data1['C2H6']
LG_C2H6 = data2['C2H6']

ce_gas_data = [CE_H2, CE_CO, CE_CO2, CE_CH4, CE_C2H6]
lg_gas_data = [LG_H2, LG_CO, LG_CO2, LG_CH4, LG_C2H6]

# 对CE的各个yield进行正态性检验
for i, ce_gas in enumerate(ce_gas_data):
    normality_test(ce_gas, f'CE_{i+1}_gas')

# 对LG的各个yield进行正态性检验
for i, lg_gas in enumerate(lg_gas_data):
    normality_test(lg_gas, f'LG_{i+1}_gas')

# 对各个yield进行方差齐性检验
for i in range(len(ce_gas_data)):
    homogeneity_of_variance_test(ce_gas_data[i], lg_gas_data[i], f'CE_{i+1}_gas', f'LG_{i+1}_gas')

