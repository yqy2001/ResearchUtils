import numpy as np
import matplotlib.pyplot as plt

a1 = [180, 170, 178, 185, 180, 190]
x = np.arange(6)

plt.rcParams["font.family"] = "Times New Roman"

fig, axes = plt.subplots(1, 1, figsize=(5, 3))
# 画柱状图
axes.bar(x, a1,  width=0.4, label='height', color="#D2ACA3")
# 图例
axes.legend(loc='best')
# 设置坐标轴刻度、标签
axes.set_xticks([0, 1, 2, 3, 4, 5])
axes.set_yticks([160, 165, 170, 175, 180, 185, 190])
axes.set_ylim((160, 190))
axes.set_xticklabels(['zhouyi', 'xuweijia', 'lurenchi', 'chenxiao', 'weiyu', 'guhaiyao'])
# 设置title
axes.set_title('NLP group members heights')
# 网格线
axes.grid(linewidth=0.5, which="major", axis='y')
# 隐藏上、右边框
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

for i in range(6):
    axes.text(x[i], a1[i], a1[i], ha='center', va='bottom')

plt.tight_layout()
plt.show()
fig.savefig("普通柱状图.png", dpi=800)
