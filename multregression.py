import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error ,mean_squared_error,root_mean_squared_error,r2_score


df1=pd.read_csv("economic_index.csv") #the data

df1.drop(columns=["Unnamed: 0","year","month"],axis=1, inplace=True)#dropping unnecessary column
x1=df1[["interest_rate", "unemployment_rate"]]#setting data to x and y variable
y1=df1['index_price']

x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,train_size=0.75,random_state=42)#splitting the data in test/train

scaler=StandardScaler()
x1_train=scaler.fit_transform(x1_train) #standardizing the data
x1_test=scaler.transform(x1_test)

mulregression=LinearRegression(n_jobs=-1)
mulregression.fit(x1_train,y1_train)      #feeding the data
y1_pred=mulregression.predict(x1_test)    #predicting the test data
'''mse=mean_squared_error(y1_test,y1_pred)
mae=mean_absolute_error(y1_test,y1_pred)
rmse=np.sqrt(mse)
print(mse,mae,rmse)          #accuracy checking
r=r2_score(y1_test,y1_pred)
print(r)
validation=cross_val_score(mulregression,x1_train,y1_train,scoring="neg_mean_squared_error",cv=5)
print(np.mean(validation))'''

print(mulregression.predict(scaler.transform([[2.34,5.2]])))      #prediction