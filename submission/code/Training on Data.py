
# coding: utf-8

# In[1]:

# Imports

# pandas
import pandas as pd
from pandas import Series,DataFrame

# numpy, matplotlib, seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


# In[2]:

# get test & test csv files as a DataFrame

def get_data(learn_percent):
    train_df = pd.read_csv("../data/PasswordData.csv")
    sep=int(learn_percent*400)
    rows=len(train_df)
    train_data=DataFrame()
    test_data=DataFrame()

    for i in range(0,rows,400):
        train_data=train_data.append(train_df[i:i+sep])
        test_data=test_data.append(train_df[i+sep:i+400])
    
    return train_data,test_data



def feature_eng(X,Y,l):
    X_featured=X
    Y_featured=Y
    for power in l:
        X_power=X.abs()**power
        Y_power=Y.abs()**power
        X_featured=pd.concat([X_featured, X_power], axis=1)
        Y_featured=pd.concat([Y_featured, Y_power], axis=1)
    return X_featured,Y_featured
    


# In[3]:

train_data,test_data=get_data(0.7)


Y_train=train_data["subject"]
X_train=train_data.drop("subject",axis=1)

Y_test=test_data["subject"]
X_test=test_data.drop("subject",axis=1)


# In[11]:

# Y_pred = random_forest.predict(X_test)


#----------- Logistic Regression------------------
# logreg.coef_[0] #to get the coeff of the data
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
print("Logistic Regression : "+ str(logreg.score(X_test, Y_test)))



#----------- Support Vector Machines------------------
svc = SVC()
svc.fit(X_train, Y_train)
print("Support Vector Machines : "+str(svc.score(X_test, Y_test)))



#-----------  Random Forests------------------
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
print("Random Forests : "+str(random_forest.score(X_test, Y_test)))



#----------- K NN Classification------------------
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))


#-----------  Gaussian Naive Bayes------------------
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
print("Gaussian Naive Bayes : "+str(gaussian.score(X_test, Y_test)))





# In[5]:
#trigraph : Uncomment to enable
'''
cols=list(X_train)
print(len(list(X_train)))
temp=DataFrame()
for i in range(2,len(cols)-8,3):
    X_train[str("DD"+str(i))]=X_train[cols [i] ] + X_train[cols[i+2]  ] + X_train[cols[i+3] ]+ X_train[cols[i+4] ]
    X_train[str("UD"+str(i))]=X_train[cols[i+2] ] + X_train[cols[i+3] ]+X_train[cols[i+4] ]+ X_train[cols[i+5] ]
    
print(len(list(X_train)))

cols=list(X_test)
print(len(list(X_test)))
temp=DataFrame()
for i in range(2,len(cols)-8,3):
    X_test[str("DD"+str(i))]=X_test[cols [i] ] + X_test[cols[i+2] ]  + X_test[cols[i+3]  ]+X_test[cols[i+4]  ]
    X_test[str("UD"+str(i))]=X_test[cols[i+2]  ]+ X_test[cols[i+3]  ]+X_test[cols[i+4]  ]+X_test[cols[i+5] ]
    
print(len(list(X_test)))
'''

# In[35]:

# Y_pred = random_forest.predict(X_test)


#----------- Logistic Regression------------------
# logreg.coef_[0] #to get the coeff of the data
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
print("Logistic Regression : "+ str(logreg.score(X_test, Y_test)))



#----------- Support Vector Machines------------------
svc = SVC()
svc.fit(X_train, Y_train)
print("Support Vector Machines : "+str(svc.score(X_test, Y_test)))



#-----------  Random Forests------------------
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
print("Random Forests : "+str(random_forest.score(X_test, Y_test)))



#----------- K NN Classification------------------
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))


#-----------  Gaussian Naive Bayes------------------
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
print("Gaussian Naive Bayes : "+str(gaussian.score(X_test, Y_test)))



# In[6]:

# Y_pred = random_forest.predict(X_test)


#----------- Logistic Regression------------------
# logreg.coef_[0] #to get the coeff of the data
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
print("Logistic Regression : "+ str(logreg.score(X_test, Y_test)))



#----------- Support Vector Machines------------------
svc = SVC()
svc.fit(X_train, Y_train)
print("Support Vector Machines : "+str(svc.score(X_test, Y_test)))



#-----------  Random Forests------------------
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
print("Random Forests : "+str(random_forest.score(X_test, Y_test)))



#----------- K NN Classification------------------
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))


#-----------  Gaussian Naive Bayes------------------
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
print("Gaussian Naive Bayes : "+str(gaussian.score(X_test, Y_test)))





# In[5]:

from sklearn.neural_network import MLPClassifier

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))

knn = KNeighborsClassifier(n_neighbors = 4)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))

knn = KNeighborsClassifier(n_neighbors = 10)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))

knn = KNeighborsClassifier(n_neighbors = 51)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))

gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
print("Gaussian Naive Bayes : "+str(gaussian.score(X_test, Y_test)))

nn = MLPClassifier(activation='relu', hidden_layer_sizes=(1200,50))
nn.fit(X_train, Y_train)
print("MLP : "+str(nn.score(X_test, Y_test)))

nn = MLPClassifier(activation='identity', hidden_layer_sizes=(12000,500))
nn.fit(X_train, Y_train)
print("MLP : "+str(nn.score(X_test, Y_test)))


nn = MLPClassifier(activation='logistic', hidden_layer_sizes=(51,5))
nn.fit(X_train, Y_train)
print("MLP : "+str(nn.score(X_test, Y_test)))


nn = MLPClassifier(activation='tanh', hidden_layer_sizes=(51,5))
nn.fit(X_train, Y_train)
print("MLP : "+str(nn.score(X_test, Y_test)))


# In[6]:

#feature engineering
Y_train=train_data["subject"]
X_train=train_data.drop("subject",axis=1)

Y_test=test_data["subject"]
X_test=test_data.drop("subject",axis=1)

# X_train.info()
powers=[0.5,2]
X_train,X_test_featured=feature_eng(X_train,X_test,powers)
# X_train.info()
#X_test.info()


# # Without  Normalization
# 
# ## Without Feature Engineering 
# Logistic Regression : 0.702777777778<br />
# Support Vector Machines : 0.0970588235294<br />
# Random Forests : 0.873366013072<br />
# K NN Classification : 0.157679738562<br />
# Gaussian Naive Bayes : 0.57091503268<br />
# 
# 
# ## Feature Engineering:
# ### powers=[0.5]
# Logistic Regression : 0.76339869281<br />
# Support Vector Machines : 0.180882352941<br />
# Random Forests : 0.859967320261<br />
# K NN Classification : 0.172549019608<br />
# Gaussian Naive Bayes : 0.646895424837<br />
# 
# 
# ### powers=[2]
# Logistic Regression : 0.504248366013<br />
# Support Vector Machines : 0.0196078431373<br />
# Random Forests : 0.85637254902<br />
# K NN Classification : 0.146405228758<br />
# Gaussian Naive Bayes : 0.205555555556<br />
# 
# 
# ### powers=[0.5,2]
# Logistic Regression : 0.776307189542<br />
# Support Vector Machines : 0.0197712418301<br />
# Random Forests : 0.854738562092<br />
# K NN Classification : 0.15637254902<br />
# Gaussian Naive Bayes : 0.37385620915<br />
# 
# 
# 
# 
# Need to try
# http://sebastianraschka.com/Articles/2014_about_feature_scaling.html

# In[7]:

# Y_pred = random_forest.predict(X_test)


#----------- Logistic Regression------------------
Y_test=test_data["subject"]
X_test=X_test_featured
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
print("Logistic Regression : "+ str(logreg.score(X_test, Y_test)))



#----------- Support Vector Machines------------------
Y_test=test_data["subject"]
X_test=X_test_featured
svc = SVC()
svc.fit(X_train, Y_train)
print("Support Vector Machines : "+str(svc.score(X_test, Y_test)))



#-----------  Random Forests------------------
Y_test=test_data["subject"]
X_test=X_test_featured
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
print("Random Forests : "+str(random_forest.score(X_test, Y_test)))



#----------- K NN Classification------------------
Y_test=test_data["subject"]
X_test=X_test_featured
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
print("K NN Classification : "+str(knn.score(X_test, Y_test)))


#-----------  Gaussian Naive Bayes------------------
Y_test=test_data["subject"]
X_test=X_test_featured
gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
print("Gaussian Naive Bayes : "+str(gaussian.score(X_test, Y_test)))


# With 3 <br />
# Logistic Regression : 0.718954248366 <br />
# Support Vector Machines : 0.174019607843 <br />
# Random Forests : 0.853921568627 <br />
# K NN Classification : 0.170424836601 <br />
# Gaussian Naive Bayes : 0.475490196078 <br /> <br /> <br />
# 
#  <br />
# Without 3 <br />
# Logistic Regression : 0.76862745098 <br />
# Support Vector Machines : 0.0197712418301 <br />
# Random Forests : 0.855882352941 <br />
# K NN Classification : 0.15637254902 <br />
# Gaussian Naive Bayes : 0.37385620915 <br />

# In[ ]:



