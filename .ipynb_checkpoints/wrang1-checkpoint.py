import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")
print(df.isnull().sum())
print(df.describe())
print(df.info())
print(df.shape)

# Type Conversion
df['Salary'] = df['Salary'].astype(float)

# Z-Score Normalization
df['Age_Z'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()
df.boxplot(column=['Age_Z'])
plt.show()

# Categorical to Quantitative
df = pd.get_dummies(df, columns=['Gender'])