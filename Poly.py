import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 读取数据
df = pd.read_csv('./data/DFA_LG_data.csv')

# 提取输入特征和目标变量
X = df[['mixing ratio']]
y = df['Syngas yield']

# 创建多项式特征
degree = 3  # 多项式的次数
poly = PolynomialFeatures(degree=degree, include_bias=False)
X_poly = poly.fit_transform(X)

# 创建并拟合多项式回归模型
model = LinearRegression()
model.fit(X_poly, y)

# 输出模型参数
print("Intercept (截距):", model.intercept_)
print("Coefficients (系数):", model.coef_)

# 生成新数据点进行预测
new_mixing_ratios = np.linspace(min(df['mixing ratio']), max(df['mixing ratio']), 100)
new_data = pd.DataFrame({'mixing ratio': new_mixing_ratios})
new_data_poly = poly.transform(new_data)
predictions = model.predict(new_data_poly)

# 绘制拟合结果
plt.scatter(df['mixing ratio'], y, label='Actual Data')
plt.plot(new_data['mixing ratio'], predictions, label=f'Polynomial Regression (Degree={degree})', color='red')
plt.xlabel('Mixing Ratio')
plt.ylabel('Syngas Yield')
plt.legend()
plt.savefig('./figure/poly_regression_syngas.png')
plt.show()

import joblib

# 保存模型
model_filename = 'polynomial_regression_model.joblib'
joblib.dump(model, model_filename)
print(f'Model saved as {model_filename}')

# 加载模型
loaded_model = joblib.load(model_filename)

# 进行模型的灵敏度检验
sensitivity_data = pd.DataFrame({'mixing ratio': new_mixing_ratios})
sensitivity_data_poly = poly.transform(sensitivity_data)
sensitivity_predictions = loaded_model.predict(sensitivity_data_poly)

# 绘制灵敏度检验结果
plt.scatter(df['mixing ratio'], y, label='Actual Data')
plt.plot(new_data['mixing ratio'], predictions, label=f'Polynomial Regression (Degree={degree})', color='red')
plt.scatter(sensitivity_data['mixing ratio'], sensitivity_predictions, label='Sensitivity Test', marker='x', color='green')
plt.xlabel('Mixing Ratio')
plt.ylabel('Syngas Yield')
plt.legend()
plt.savefig('./figure/check_syngas.png')
plt.show()
