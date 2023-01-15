from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, decomposition
from sklearn.cluster import KMeans
pca = decomposition.PCA(n_components=2)

digits = datasets.load_digits()
X = digits.data
y = digits.target

#Свернём признаковое описание в матрицу цветов 8x8 и изобразим эти рукописные цифры см. рис. 2.5
plt.figure(figsize=(16, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X[i,:].reshape([8,8]));
#Уменьшим размерность пространства с 64 координат до 2
pca = decomposition.PCA(n_components=2)
X_reduced = pca.fit_transform(X)
#Отобразим элементы датасета в новом 2-х мерном пространстве, раскрасив их в соответствии со значением y (см. рис. 2.6)
plt.figure(figsize=(12,10))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, edgecolor='none', alpha=0.7, s=40, cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.colorbar()
pca = decomposition.PCA().fit(X)
plt.figure(figsize=(10,7))
plt.plot(np.cumsum(pca.explained_variance_ratio_), color='k', lw=2)
plt.xlabel('Number of components')
plt.ylabel('Total explained variance')
plt.xlim(0, 63)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.axvline(21, c='b')
plt.axhline(0.9, c='r')
plt.show()