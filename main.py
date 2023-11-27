import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

df = pd.read_csv('./data/DFA_CE_data.csv')

X = sm.add_constant(df[['mixing ratio', 'Water yield', 'Char yield', 'Syngas yield']])

model_tar = sm.OLS(df['Tar yield'], X)
results_tar = model_tar.fit()
model_water = sm.OLS(df['Water yield'], X)
results_water = model_water.fit()
model_char = sm.OLS(df['Char yield'], X)
results_char = model_char.fit()
model_syngas = sm.OLS(df['Syngas yield'], X)
results_syngas = model_syngas.fit()

print(results_syngas.params)
plt.figure(figsize=(12, 8))

# CE 和 LG 不用输出 mixing ratio = 0 的数据
"""plt.scatter([0], [19.46], marker='o', s=200, color='purple', label='Reference (mixing ratio=0, Tar Yield)')
plt.scatter([0], [26.84], marker='o', s=200, color='red', label='Reference (mixing ratio=0, Water Yield)')
plt.scatter([0], [29.21], marker='o', s=200, color='blue', label='Reference (mixing ratio=0, Char Yield)')
plt.scatter([0], [24.49], marker='o', s=200, color='green', label='Reference (mixing ratio=0, Syngas Yield)')"""

plt.plot(df['mixing ratio'], results_tar.predict(), marker='o', markersize=8, label='Tar Yield', color='purple')
plt.plot(df['mixing ratio'], results_water.predict(), marker='o', markersize=8, label='Water Yield', color='red')
plt.plot(df['mixing ratio'], results_char.predict(), marker='o', markersize=8, label='Char Yield', color='blue')
plt.plot(df['mixing ratio'], results_syngas.predict(), marker='o', markersize=8, label='Syngas Yield', color='green')


plt.title('DFA/CE')
plt.xlabel('Mixing Ratio')
plt.ylabel('wt.%(daf)')
plt.legend()
plt.grid(True)
plt.savefig('./figure/linear_regression_DFA_CE.png')
plt.show()
