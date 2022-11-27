import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

df = pd.read_csv('Dataset/video_games_sales.csv')
df = df.dropna()
df['User_Score'] = df.User_Score.astype('float64')
df['Year_of_Release'] = df.Year_of_Release.astype('int64')
df['User_Count'] = df.User_Count.astype('int64')
df['Critic_Count'] = df.Critic_Count.astype('int64')

useful_cols = ['Name', 'Platform', 'Year_of_Release', 'Genre',
               'Global_Sales', 'Critic_Score', 'Critic_Count',
               'User_Score', 'User_Count', 'Rating'
              ]
# defining all 3 axes
z = df.User_Score
x = df.Year_of_Release
y = df.User_Count

# plotting
ax.plot3D(x, y, z)

sales_df = df[[x for x in df.columns if 'Sales' in x] + ['Year_of_Release']]
sales_df.groupby('Year_of_Release').sum().plot(kind='bar', rot=45)
plt.show()
cols = ['Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
sns_plot = sns.pairplot(df[cols])
plt.show()
sns.displot(df.Critic_Score)
plt.show()
top_platforms = df.Platform.value_counts().sort_values(ascending = False).head(5).index.values
sns.boxplot(y="Platform", x="Critic_Score", data=df[df.Platform.isin(top_platforms)], orient="h")
plt.show()
