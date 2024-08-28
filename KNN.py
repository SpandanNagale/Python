import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , classification_report

df=pd.read_csv('Algerian_forest_fires_cleaned_dataset.csv')
df.drop(columns=['day','month','year'],axis=1,inplace=True)
df['Classes']=np.where(df['Classes'].str.contains('not fire'),0,1)
x=df.drop('Classes',axis=1)
y=df['Classes']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=49)

def drops(dataset,threshhold):
    any=set()
    correlation=dataset.corr()
    for i in range(len(correlation.columns)):
        for j in range(i):
            if abs(correlation.iloc[i,j]) > threshhold:
                column=correlation.columns[i]
                any.add(column)
    return any            

col=drops(x,0.85)
x_train.drop(col, axis=1,inplace=True)
x_test.drop(col, axis=1,inplace=True)
KNN=KNeighborsClassifier()
KNN.fit(x_train,y_train)
y_pred=KNN.predict(x_test)
score=accuracy_score(y_test,y_pred)
classify=classification_report(y_test,y_pred)
print(score)
print(classify)