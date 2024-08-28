import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.metrics import r2_score
import pickle

df_set=pd.read_csv("Algerian_forest_fires_cleaned_dataset.csv")
df_set.drop(columns=['day','month','year'],axis=1,inplace=True)
df_set['Classes']=np.where(df_set['Classes'].str.contains('not fire'),0,1)
x2=df_set.drop('FWI', axis=1)
y2=df_set["FWI"]

x2_train,x2_test,y2_train,y2_test=train_test_split(x2,y2, train_size=0.75,random_state=42)

def drops(dataset,threshhold):
    any=set()
    correlation=dataset.corr()
    for i in range(len(correlation.columns)):
        for j in range(i):
            if abs(correlation.iloc[i,j]) > threshhold:
                column=correlation.columns[i]
                any.add(column)
    return any            

col=drops(x2,0.85)
x2_train.drop(col, axis=1,inplace=True)
x2_test.drop(col, axis=1,inplace=True)

scaling=StandardScaler()
x2_train=scaling.fit_transform(x2_train)
x2_test=scaling.transform(x2_test)
ridge=Ridge()
ridge.fit(x2_train,y2_train)
y2_pred=ridge.predict(x2_test)
plt.scatter(y2_test,y2_pred)
score=r2_score(y2_test,y2_pred)
print(score)

pickle.dump(scaling, open('scaler.pkl', 'wb'))
pickle.dump(ridge, open('ridge.pkl', 'wb'))

