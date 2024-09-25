import pandas as pd 
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,roc_auc_score



df=load_breast_cancer()

x=pd.DataFrame(df.data,columns=df.feature_names)
y=pd.DataFrame(df.target)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=34)

scale=StandardScaler()

x_train=scale.fit_transform(x_train)
x_test=scale.transform(x_test)

models={
        'random forest':RandomForestClassifier(),
        'gradient boosting':GradientBoostingClassifier(),
        'adaboost':AdaBoostClassifier()


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
