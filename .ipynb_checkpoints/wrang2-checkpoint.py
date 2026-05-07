import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("Academic_Performance.csv")

# Missing Values (Mean/Mode)
df['Score'] = df['Score'].fillna(df['Score'].mean())
df = df.fillna(df.mode().iloc[0])

# Outliers (Z-Score)
z = np.abs((df['Age'] - df['Age'].mean()) / df['Age'].std())
df = df[z < 3]

# Data Transformation (Binning)
df['Grade'] = pd.cut(df['Marks'], bins=[0, 40, 70, 100], labels=['Low', 'Avg', 'High'])

sns.boxplot(data=df)
plt.show()