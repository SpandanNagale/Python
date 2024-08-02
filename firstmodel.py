import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error ,mean_squared_error,root_mean_squared_error,r2_score


df=pd.read_csv("wieght-height.csv")

df.drop(columns=["Gender"],axis=1,inplace=True)
#print(df.head())
#plt.scatter(df["Height"],df["Weight"])
#print(df.corr())
x=df[["Weight"]]
y=df["Height"]

x_train,x_test,y_train,y_test=train_test_split(x,y, train_size=0.75, random_state=42)

scalar=StandardScaler()
x_train=scalar.fit_transform(x_train)
x_test=scalar.transform(x_test)

regression=LinearRegression(n_jobs=-1)
regression.fit(x_train,y_train)
#print(regression.coef_,regression.intercept_)
#plt.scatter(x_train,y_train)
#plt.plot(x_train,regression.predict(x_train))
y_pred=regression.predict(x_test)
#print(y_pred)
'''mse=mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
rmse=np.sqrt(mse)
r=r2_score(y_test,y_pred)
print(r)

print(mse,mae,rmse)'''
print(regression.predict(scalar.transform([[70]])))
