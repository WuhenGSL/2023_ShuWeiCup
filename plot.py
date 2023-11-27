import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件导入数据
df = pd.read_csv('./data/DFA_LG_Gas_Yield.csv')

# 提取数据
mixing_ratio = df['mixing ratio']
H2 = df['H2']
CO = df['CO']
CO2 = df['CO2']
CH4 = df['CH4']
C2H6 = df['C2H6']
""" C3H8 = df['C3H8']
C3H6 = df['C3H6']
C2H4 = df['C2H4']
C4H10 = df['C4H10'] """

# 绘制折线图
plt.plot(mixing_ratio, H2, label='H2')
plt.plot(mixing_ratio, CO, label='CO')
plt.plot(mixing_ratio, CO2, label='CO2')
plt.plot(mixing_ratio, CH4, label='CH4')
plt.plot(mixing_ratio, C2H6, label='C2H6')
""" plt.plot(mixing_ratio, C3H8, label='C3H8')
plt.plot(mixing_ratio, C3H6, label='C3H6')
plt.plot(mixing_ratio, C2H4, label='C2H4')
plt.plot(mixing_ratio, C4H10, label='C4H10') """

# 添加标签和标题
plt.xlabel('Mixing Ratio')
plt.ylabel('Gas Yield(mL/g,daf)')
plt.title('DFA/LG Gas Yield')

yticks = [i for i in range(0, 60, 10)]  # 从 0 到 60，每隔 5 设置一个刻度
plt.yticks(yticks)

plt.legend()

plt.savefig('./figure/DFA_LG_Gas_Yield.png')

plt.show()
