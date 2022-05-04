import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator
import numpy as np

y = [92.6, 87.8, 82.6, 73.0, 70.4]
y2 = [87.2, 93.3, 85, 77.9, 80]
x = [1, 2, 3, 4, 5]

plt.rcParams["font.family"] = "Times New Roman"

fig, axes = plt.subplots(1, 1, figsize=(8, 4))
# 折线图
axes.plot(x, y, linestyle='-', color='#DE6B58', marker='x', linewidth=1.5)
axes.plot(x, y2, linestyle='-', color='#E1A084', marker='x', linewidth=1.5)
# 设置最小刻度间隔
axes.yaxis.set_minor_locator(MultipleLocator(2.5))
axes.xaxis.set_minor_locator(MultipleLocator(0.5))
# 画网格线
axes.grid(which='minor', c='lightgrey')
# 设置x、y轴标签
axes.set_ylabel("Generation Consistency")
axes.set_xlabel("KB Row Number")
# 设置y轴的刻度
axes.set_yticks([70, 75, 80, 85, 90, 95])
# 对每个数据点加标注
for x_, y_ in zip(x, y):
    axes.text(x_, y_, y_, ha='left', va='bottom')
for x_, y_ in zip(x, y2):
    axes.text(x_, y_, y_, ha='left', va='bottom')
# 展示图片
plt.show()
fig.savefig("折线图.png", dpi=800)
