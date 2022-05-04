import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

digits = datasets.load_digits(n_class=6)
X, y = digits.data, digits.target 
# 为了使得可视化更加直观，同一数据使用同一种颜色，所以我们需要额外记录每一组数据的信息，这里的y起到的就是记录信息的作用

n_samples, n_features = X.shape


'''为了方面演示构造了一组数据，用的是一个手写数字数据集'''
n = 20  # 每行20个数字，每列20个数字
img = np.zeros((10 * n, 10 * n))
for i in range(n):
    ix = 10 * i + 1
    for j in range(n):
        iy = 10 * j + 1
        img[ix:ix + 8, iy:iy + 8] = X[i * n + j].reshape((8, 8))

"""
plt.figure(figsize=(8, 8))   # figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
plt.imshow(img, cmap=plt.cm.binary)
plt.xticks([])
plt.yticks([])
plt.show()
"""


'''上面的这一部分主要是为了获取X，这个X必须为numpy.array数据类型，不只是上述的数据，无论任何数据都可以在转化成numpy.array类型后用T-sne可视化'''
'''获取X后，接下来的步骤都是类似的'''
'''接下来的这部分代码，只要保证X是array数据即可'''
'''t-SNE'''
tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
X_tsne = tsne.fit_transform(X) # 这里的X必须为array数据


'''嵌入空间可视化'''
x_min, x_max = X_tsne.min(0), X_tsne.max(0)
X_norm = (X_tsne - x_min) / (x_max - x_min)  # 归一化，主要是为了方便观察，实际上不使用也可以

fig=plt.figure(figsize=(8, 8))
plt.grid()

for i in range(X_norm.shape[0]):
    plt.text(X_norm[i, 0], X_norm[i, 1], str('.'), color=plt.cm.Set1(y[i]),   
            fontdict={'weight': 'bold', 'size': 9})   # plt.text(x, y, s, fontsize, verticalalignment,horizontalalignment,rotation , **kwargs)
# 这里使用了之前用来记录信息的y，在其他的使用情况中，每一大类数据应当使用同一种标号。
# 假设有m个数据，那么y即为一个长度为m，内容为区分对应的数据的特征的值

x = [0.2, 0.4, 0.6, 0.8]
labels = ['0.2', '0.4', '0.6', '0.8']
plt.xticks(x,labels,rotation=0)
plt.yticks(x,labels,rotation=0)

plt.show()