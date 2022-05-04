import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

IO = 'Sales2.xlsx'
sales = pd.read_excel(io = IO)

sales['year'] = sales['Date'].dt.year #提取年份
sales['month'] = sales['Date'].dt.month #提取月份

summary = pd.pivot_table(data = sales,
                         index = 'year',
                         columns = 'month',
                         values = 'Sales',
                         aggfunc = np.sum)

sns.heatmap(data = summary,
            annot = False,
            square = False,
            cmap = 'BuGn',
            mask = summary < 350000)

plt.title('数据')
plt.show()
