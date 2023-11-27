"""请制作三线表"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, wilcoxon


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


t_stat_tar, p_value_tar = wilcoxon(CE_tar_yield, LG_tar_yield)
t_stat_water, p_value_water = ttest_ind(CE_water_yield, LG_water_yield)
t_stat_char, p_value_char = wilcoxon(CE_char_yield, LG_char_yield)
t_stat_syngas, p_value_syngas = ttest_ind(CE_syngas_yield, LG_syngas_yield)

# 打印结果
print(f'wilcoxon for Tar yield: t-statistic = {t_stat_tar}, p-value = {p_value_tar}')
print(f't-test for Water yield: t-statistic = {t_stat_water}, p-value = {p_value_water}')
print(f'wilcoxon for Char yield: t-statistic = {t_stat_char}, p-value = {p_value_char}')
print(f't-test for Syngas yield: t-statistic = {t_stat_syngas}, p-value = {p_value_syngas}')


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

t_stat_H2, p_value_H2 = ttest_ind(CE_H2, LG_H2)
t_stat_CO, p_value_CO = ttest_ind(CE_CO, LG_CO)
t_stat_CO2, p_value_CO2 = ttest_ind(CE_CO2, LG_CO2)
t_stat_CH4, p_value_CH4 = ttest_ind(CE_CH4, LG_CH4)
t_stat_C2H6, p_value_C2H6 = ttest_ind(CE_C2H6, LG_C2H6)

# 打印结果
print(f't-test for H2 yield: t-statistic = {t_stat_H2}, p-value = {p_value_H2}')
print(f't-test for CO yield: t-statistic = {t_stat_CO}, p-value = {p_value_CO}')
print(f't-test for CO2 yield: t-statistic = {t_stat_CO2}, p-value = {p_value_CO2}')
print(f't-test for CH4 yield: t-statistic = {t_stat_CH4}, p-value = {p_value_CH4}')
print(f't-test for C2H6 yield: t-statistic = {t_stat_C2H6}, p-value = {p_value_C2H6}')
