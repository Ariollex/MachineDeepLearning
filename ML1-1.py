import pandas as pd

df = pd.read_csv(filepath_or_buffer='Dataset/titanic.csv')

print(df.head()) # Первые 5 строк
print(df.shape) # Размер данных
print(df.columns) # Названия столбцов
print(df.info()) # Общая информация
print(df.describe()) # Основные статистические характеристики данных по каждому числовому признаку
print(df.describe(include=['object', 'int64']))
print(df['Survived'].value_counts())
print(df['Embarked'].value_counts(normalize=True)) #Распределение пользователей по переменной Embarked. normalize=True, чтобы посмотреть не абсолютные частоты, а относительные
print(df.sort_values(by='PassengerId',
        ascending=False).head()) # ascending=False для сортировки по убыванию
print(df.sort_values(by=['PassengerId', 'Survived'], # Сортировка по группам столбцов
        ascending=[True, False]).head())
print(df['Survived'].mean())
print(df[:1]) # Первая строка
print(pd.crosstab(df['Survived'], df['Pclass'], margins=True)) # Как кол-во выживших связано с классом