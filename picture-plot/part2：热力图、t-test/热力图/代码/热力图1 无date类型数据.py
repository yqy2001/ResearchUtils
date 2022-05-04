import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

IO = 'Sales1.xlsx'
sales = pd.read_excel(io = IO)

summary = pd.pivot_table(data = sales,
                         index = 'year',
                         columns = 'month',
                         values = 'sales')

sns.heatmap(data = summary,
            annot = False,
            square = True,
            cmap = 'BuGn_r')
plt.title('sales')
plt.show()