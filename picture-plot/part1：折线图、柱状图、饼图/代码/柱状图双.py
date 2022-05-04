import numpy as np
import matplotlib.pyplot as plt
a2 = [180, 170, 178, 185, 180, 190]
a1 = [160, 168, 170, 175, 160, 180]

b1 = [0.4571, 0.4824]
b2 = [0.3226, 0.4519]

plt.rcParams["font.family"] = "Times New Roman"

fig, axes = plt.subplots(1, 1, figsize=(5, 3))

x = np.arange(6)
width = 0.3

axes.bar(x - width / 2, a1,  width=width, label='2015', color="#D2ACA3")
axes.bar(x + width / 2, a2, width=width, label='2020', color="#EBDFDF")
# axes.bar(x + width, a2, width=width, label='2025', color="#E1A084")

axes.legend(loc='best')
axes.set_xticks([0, 1, 2, 3, 4, 5])
axes.set_yticks([150, 155, 160, 165, 170, 175, 180, 185, 190])
axes.set_ylim((150, 190))
axes.set_xticklabels(['zhouyi', 'xuweijia', 'lurenchi', 'chenxiao', 'weiyu', 'guhaiyao'])
axes.set_title('NLP group height change')


axes.grid(linewidth=0.5, which="major", axis='y')

axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['bottom'].set_visible(False)
axes.spines['left'].set_visible(False)


#for a, b in zip(x, a1):
#    axes[0].text(a - width / 2, b, b, ha='center', va='bottom')
#for a, b in zip(x, a2):
#    axes[0].text(a + width / 2, b, b, ha='center', va='bottom')
#
#for a, b in zip(x, b1):
#    axes[1].text(a - width / 2, b, b, ha='center', va='bottom')
#for a, b in zip(x, b2):
#    axes[1].text(a + width / 2, b, b, ha='center', va='bottom')

try:
    axes.rc('axes', axisbelow=True)
except:
    pass


plt.tight_layout()
plt.show()
fig.savefig("柱状图双.png", dpi=800)
