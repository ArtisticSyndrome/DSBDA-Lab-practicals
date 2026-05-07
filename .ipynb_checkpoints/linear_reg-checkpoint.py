import pandas as pd
from sklearn.linear_model import LinearRegression

# For Salary CSV
df = pd.read_csv("salary.csv")
X = df[['Experience']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

# Predict for 15 years
print(model.predict([[15]]))