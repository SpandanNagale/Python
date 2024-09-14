import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge,Lasso,ElasticNet
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.datasets import load_diabetes
from sklearn.svm import SVR

df=load_diabetes()
x=pd.DataFrame(df.data,columns=df.feature_names)
y=pd.DataFrame(df.target)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=23)
scale=StandardScaler()
x_train=scale.fit_transform(x_train)
x_test=scale.transform(x_test)

models={
     
     'randomforest':RandomForestRegressor(),
     'kneighbour':KNeighborsRegressor(),
     'tree':DecisionTreeRegressor(),
     'ridge':Ridge(),
     'lasso':Lasso(),
     'elasticnet':ElasticNet(),
     'supportvector':SVR(),
     'adaboost':AdaBoostRegressor()


}

for i in range(len(list(models))):
    model=list(models.values())[i]
    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)


    
    score=r2_score(y_test,y_pred)
    mae=mean_absolute_error(y_test,y_pred)
    mse=mean_squared_error(y_test,y_pred)
    print(model,":")
    print('mean absolute error',mae)
    print('mean squared error',mse)
    print('r2score',score)
