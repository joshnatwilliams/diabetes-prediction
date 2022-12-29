import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

# Read data
df = pd.read_csv('/Users/joshuawilliams/Documents/diabetes-prediction/diabetes_data.csv')
questions = list(df.columns.values)
# split data
X_tr, X_te, Y_tr, Y_te = train_test_split(df.iloc[:,:-1],df.iloc[:,-1], train_size=0.3, test_size=.7,random_state=None) 

# Train model
svc = SVC(probability = True)
svc.fit(X_tr,Y_tr)

# Simplify model for visualization
pca = PCA(n_components=2)
tr_df = pd.DataFrame(pca.fit_transform(X_tr), columns= ['PC1', 'PC2'])
y_df = pd.DataFrame(Y_tr).reset_index()
pca_df = pd.concat([tr_df, y_df['Diabetes']],axis=1).head(n = 500)
