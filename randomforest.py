import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score,roc_auc_score
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("Travel.csv")

df.isnull().sum()
df['Gender']=df['Gender'].replace('Fe Male','Female')
df['MaritalStatus']=df['MaritalStatus'].replace('Single','Unmarried')


feature_with_na=[features for features in df.columns if df[features].isnull().sum()>=1]

#for feature in feature_with_na:
    #print(feature,np.round(df[feature].isnull().mean()*100,5))


df.Age.fillna(df.Age.median(),inplace=True)
df.TypeofContact.fillna(df.TypeofContact.mode()[0], inplace=True)
df.DurationOfPitch.fillna(df.DurationOfPitch.median(), inplace=True)
df.NumberOfFollowups.fillna(df.NumberOfFollowups.mode()[0], inplace=True)
df.PreferredPropertyStar.fillna(df.PreferredPropertyStar.mode()[0], inplace=True)
df.NumberOfTrips.fillna(df.NumberOfTrips.median(), inplace=True)
df.NumberOfChildrenVisiting.fillna(df.NumberOfChildrenVisiting.median(), inplace=True)
df.MonthlyIncome.fillna(df.MonthlyIncome.median(), inplace=True)


df.drop('CustomerID', inplace=True, axis=1)

df['TotalVisiting']=df['NumberOfPersonVisiting'] + df['NumberOfChildrenVisiting']
df.drop(columns=['NumberOfPersonVisiting','NumberOfChildrenVisiting'], inplace=True, axis=1)


x=df.drop(['ProdTaken'], axis=1)
y=df['ProdTaken']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=20)

categorial_f=x.select_dtypes(include='object').columns
numerical_f=x.select_dtypes(exclude='object').columns

scale=StandardScaler()
one_hot=OneHotEncoder(drop="first")

preprocessor=ColumnTransformer(
    [
        
        ("StandardScaler",scale,numerical_f),
        ("OneHotEncoder",one_hot,categorial_f)
    ]
    
)

x_train=preprocessor.fit_transform(x_train)
x_test=preprocessor.transform(x_test)
 

models={
    "random forest":RandomForestClassifier()
}

for i in range(len(list(models))):
    model=list(models.values())[i]
    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)
    


    score=accuracy_score(y_test,y_pred)
   
    classify=classification_report(y_test,y_pred)
    matrix=confusion_matrix(y_test,y_pred)
    roc_auc=roc_auc_score(y_test,y_pred)

    print(model,":")
    print("\naccuracy_score:",score)
    print("\nconfusion matrix:",matrix)
    print("\nclassification report:",classify)
    print("\nROC_AUC curve:",roc_auc)
