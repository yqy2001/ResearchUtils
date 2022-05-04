import matplotlib.pyplot as plt

plt.rc('font', family='Times New Roman')

fig, axe = plt.subplots(1, 1, figsize=(8, 5))

font1 = {'family': 'Times New Roman', 'size': '15'}
# 饼状图各个部分的标签、值、颜色
labels = ['food', 'clothing', 'housing', 'transport']
values = [0.35, 0.15, 0.2, 0.3]
colors = ['#D2ACA3', '#EBDFDF', '#DE6B58', '#E1A084']
# 突出显示
explode = [0, 0.1, 0, 0]
# 标题
axe.set_title("daily cost", fontdict=font1)
# 画饼状图
wedge, texts, pcts = axe.pie(values, labels=labels, colors=colors, startangle=45, autopct='%3.1f%%'
                             , explode=explode)
axe.axis('equal')
# 图例
axe.legend(wedge, labels, fontsize=10, title='event', loc=2)
# 设置文本的属性

plt.setp(texts, size=12)
plt.setp(pcts, size=12)
plt.show()

fig.savefig("bingtu.png", dpi=800)
