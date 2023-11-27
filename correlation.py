import pandas as pd
from scipy.stats import kendalltau
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv('./data/DFA_LG_data.csv')

# 提取数据
mixing_ratio = data['mixing ratio']
tar_yield = data['Tar yield']
water_yield = data['Water yield']
char_yield = data['Char yield']
syngas_yield = data['Syngas yield']

# 换成kendalltau
spearman_tar, p_value_tar = kendalltau(mixing_ratio, tar_yield)
spearman_water, p_value_water = kendalltau(mixing_ratio, water_yield)
spearman_char, p_value_char = kendalltau(mixing_ratio, char_yield)
spearman_syngas, p_value_syngas = kendalltau(mixing_ratio, syngas_yield)

# 打印结果
print(f'Spearman correlation for Tar yield: {spearman_tar}, p-value: {p_value_tar}')
print(f'Spearman correlation for Water yield: {spearman_water}, p-value: {p_value_water}')
print(f'Spearman correlation for Char yield: {spearman_char}, p-value: {p_value_char}')
print(f'Spearman correlation for Syngas yield: {spearman_syngas}, p-value: {p_value_syngas}')

spearman = [spearman_tar, spearman_water, spearman_char, spearman_syngas]
p_values = [p_value_tar, p_value_water, p_value_char, p_value_syngas]

plt.figure(figsize=(12, 8))

plt.bar(['Tar yield', 'Water yield', 'Char yield', 'Syngas yield'], spearman, color=['purple', 'red', 'blue', 'green'])
plt.ylabel('Kenalltau correlation coefficient')
plt.title('Kenalltau correlation coefficient of DFA/LG yields')

plt.savefig('./figure/Kenalltau_DFA_LG.png')

plt.show()

plt.figure(figsize=(12, 8))

plt.bar(['Tar yield', 'Water yield', 'Char yield', 'Syngas yield'], p_values, color=['purple', 'red', 'blue', 'green'])
plt.ylabel('p-value')
plt.title('p-value coefficient of DFA/LG yields')

plt.savefig('./figure/p_value_DFA_LG.png')

plt.show()


