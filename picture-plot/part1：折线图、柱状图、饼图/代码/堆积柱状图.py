#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

y2 = [20, 2, 8, 10, 20, 10]
y1 = [160, 168, 170, 175, 160, 180]
x = np.arange(6)

plt.rcParams["font.family"] = "Times New Roman"

fig, axes = plt.subplots(1, 1, figsize=(5, 3))

axes.bar(x, y1,  width=0.4, label='height', color='#D2ACA3')
axes.bar(x, y2, width=0.4, bottom=y1, color="#EBDFDF", label='increse')

axes.legend()
axes.set_xticks([0, 1, 2, 3, 4, 5])
axes.set_yticks([150, 155, 160, 165, 170, 175, 180, 185, 190])
axes.set_ylim((150, 190))
axes.set_xticklabels(['zhouyi', 'xuweijia', 'lurenchi', 'chenxiao', 'weiyu', 'guhaiyao'])
axes.set_title('NLP group members height')

plt.tight_layout()
plt.show()

fig.savefig("柱状图堆积.png", dpi=800)
