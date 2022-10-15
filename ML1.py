import pandas
data = pandas.read_csv(filepath_or_buffer='Dataset/titanic.csv')

# №1: Сколько мужчин было на корабле?
male = data.Sex.value_counts()['male']
print(male)

# №2: Какая доля пассажиров (в %) выжила?
All = data.Survived.value_counts()[1] + data.Survived.value_counts()[0]
Survived = data.Survived.value_counts()[1]
SurvivedPercent = int((Survived / All) * 100)
print(SurvivedPercent, '%', sep='')

# №3: Какая доля пассажиров (в %) от общего количества путешествовала во 2-ом классе?
class2 = data.Pclass.value_counts()[2]
class2Percent = int((class2 / All) * 100)
print(class2Percent, '%', sep='')

# №4: Посчитайте среднее и медиану возраста всех людей на корабле.
meanAge = data.Age.mean()
medianAge = data.Age.median()
print(meanAge)
print(medianAge)

# №5: Коррелируют ли число братьев/сестер с числом родителей/детей?
corr = data['SibSp'].corr(data['Parch'])
print(corr)
