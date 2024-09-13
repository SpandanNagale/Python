import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

df=pd.read_csv("cardekho_imputated.csv")

df.drop(columns=['car_name','brand','Unnamed: 0'], axis=1,inplace=True)
df.head()
x=df.drop(columns=['selling_price'],axis=1)
y=df['selling_price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=23)

le=LabelEncoder()
x_train['model']=le.fit_transform(x_train['model'])
x_test['model']=le.fit_transform(x_test['model'])

num_feature=x.select_dtypes(exclude='object').columns
cat_feature=['fuel_type','seller_type','transmission_type']
scale=StandardScaler()
one_hot=OneHotEncoder(drop='first')

preprocessor=ColumnTransformer(
      [  ('StandardScaler',scale,num_feature),
        ('OneHotEncoder',one_hot,cat_feature)
      ],remainder='passthrough'

)
x_train=preprocessor.fit_transform(x_train)
x_test=preprocessor.transform(x_test)

models={
     
     'randomforest':RandomForestRegressor(),
     'kneighbour':KNeighborsRegressor(),
     'tree':DecisionTreeRegressor()

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
