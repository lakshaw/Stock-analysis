import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv('transformed_data.csv')

#print(dataset)
#Create a Naive Bayes object
nb = GaussianNB()
#Create variable x and y.
X = dataset.iloc[:, :-1]

y = dataset.iloc[:, -1]
#Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0)
#Training the model
nb.fit(X_train, y_train)
#Predict testing set
y_pred = nb.predict(X_test)

#Check performance of model
print("\n accuracy\n",accuracy_score(y_test,y_pred))
print("\n Confusion matrix\n",confusion_matrix(y_test,y_pred))
print("\n Precision\n",precision_score(y_test,y_pred,average=None))
print("\n Recall\n",recall_score(y_test,y_pred,average=None))