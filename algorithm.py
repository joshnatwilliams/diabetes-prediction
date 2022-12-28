import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score

# read data
df = pd.read_csv("/Users/joshuawilliams/Documents/diabetes-prediction/diabetes_data.csv")
questions = list(df.columns.values)
# split data
X_tr, X_te, Y_tr, Y_te = train_test_split(df.iloc[:,:-1],df.iloc[:,-1], train_size=0.3, test_size=.7,random_state=None) 

# Train model
svc = SVC()
svc.fit(X_tr,Y_tr)
