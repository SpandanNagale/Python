import pandas as pd
import numpy  as np
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report

df=sns.load_dataset('tips')
x=df[['total_bill' ,'tip','sex','smoker', 'day','size']]
y=df['time']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=45)

l1=LabelEncoder()
l2=LabelEncoder()
l3=LabelEncoder()

x_train['sex']=l1.fit_transform(x_train['sex'])
x_train['smoker']=l2.fit_transform(x_train['smoker'])

x_test['sex']=l1.transform(x_test['sex'])
x_test['smoker']=l2.transform(x_test['smoker'])


ct=ColumnTransformer(transformers=[('onehot',OneHotEncoder(drop='first'),[4])],
                                   remainder='passthrough')
x_train=ct.fit_transform(x_train)
x_test=ct.transform(x_test)

gauss=GaussianNB()
gauss.fit(x_train,y_train)
y_pred=gauss.predict(x_test)
score=accuracy_score(y_test,y_pred)
classify=classification_report(y_test,y_pred)
print(score)
print(classify)
