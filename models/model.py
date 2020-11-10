import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataframe=pd.read_csv('StudentMarks.csv')
X=dataframe.iloc[:,1:-1]
y=dataframe.iloc[:,-1]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/4, random_state = 0)


regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

y_compare=np.vstack((y_pred,y_test)).T

print(y_compare)

print(r2_score(y_test,y_pred))
