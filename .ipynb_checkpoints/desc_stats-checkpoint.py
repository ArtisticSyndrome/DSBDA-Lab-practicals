import pandas as pd

df = pd.read_csv("data.csv")

# Summary Stats
print(df[['age', 'salary']].mean())
print(df[['age', 'salary']].std())

# Grouping
grouped = df.groupby('AgeGroup')['income'].describe()
print(grouped)

# Job ID Count
print(df['JOB_ID'].value_counts())

df['salary'].hist()
plt.show()