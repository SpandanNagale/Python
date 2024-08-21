import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pickle

df=sns.load_dataset('tips')
x=df[['tip', 'sex', 'smoker', 'day', 'time', 'size']]
y=df['total_bill']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=45)

l1=LabelEncoder()
l2=LabelEncoder()
l3=LabelEncoder()

x_train['sex']=l1.fit_transform(x_train['sex'])
x_train['smoker']=l2.fit_transform(x_train['smoker'])
x_train['time']=l3.fit_transform(x_train['time'])

x_test['sex']=l1.transform(x_test['sex'])
x_test['smoker']=l2.transform(x_test['smoker'])
x_test['time']=l3.transform(x_test['time'])

ct=ColumnTransformer(transformers=[('onehot',OneHotEncoder(drop='first'),[3])],
                                   remainder='passthrough')
x_train=ct.fit_transform(x_train)
x_test=ct.transform(x_test)

param_grid = {'C': [0.1, 1, 10, 100, 1000],
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['rbf']}
grid=GridSearchCV(SVR(),param_grid,refit=True,verbose=3,n_jobs=-1)
grid.fit(x_train,y_train)

y_pred=grid.predict(x_test)

score=r2_score(y_test,y_pred)
print(score)