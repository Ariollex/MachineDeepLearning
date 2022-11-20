import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
datasets.load_iris()

iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df['target'] = iris.target
df['name'] = df.target.apply(lambda x : iris.target_names[x])
sns_plot = sns.pairplot(df[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','name']], hue='name')
plt.show()

df["sepal length (cm)"].plot()
df["sepal width (cm)"].plot()
df["petal length (cm)"].plot()
df["petal width (cm)"].plot()
plt.show()