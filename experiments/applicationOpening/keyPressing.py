import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.externals import joblib


#Read the voice dataset
mydata = pd.read_csv("voice/voice.csv")

#Preview voice dataset
mydata.head()
print(mydata.shape)



#Prepare data for modeling
mydata.loc[:,'label'][mydata['label']=="male"] = 0
mydata.loc[:,'label'][mydata['label']=="female"] = 1
mydata_train, mydata_test = train_test_split(mydata, random_state=0, test_size=.2)
scaler = StandardScaler()
scaler.fit(mydata_train.ix[:,0:3])
X_train = scaler.transform(mydata_train.ix[:,0:3])
X_test = scaler.transform(mydata_test.ix[:,0:3])
y_train = list(mydata_train['label'].values)
y_test = list(mydata_test['label'].values)

print(mydata_train.ix[:,0:3])

#train the data
svm = SVC().fit(X_train, y_train)
print("Support Vector Machine")
print("Accuracy on training set: {:.3f}".format(svm.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(svm.score(X_test, y_test)))

#save the data into a file
joblib.dump(svm, 'svm.pkl') 
joblib.dump(scaler, 'scaler.pkl')

print("We done")