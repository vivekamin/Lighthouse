import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import sys
sys.stdout = open('output.txt','wt')

def classifier(row):
    if(row['TotalCitation'] >=0 and row['TotalCitation'] < 100):
        return 0
    elif(row['TotalCitation'] >=100 and row['TotalCitation'] < 250):
        return 1
    elif(row['TotalCitation'] >=250 and row['TotalCitation'] < 500):
        return 2
    elif(row['TotalCitation'] >=500 and row['TotalCitation'] < 1000):
        return 3
    elif(row['TotalCitation'] >=1000 and row['TotalCitation'] < 2000):
        return 4
    elif(row['TotalCitation'] >=2000 and row['TotalCitation'] < 4000):
        return 5
    elif(row['TotalCitation'] >=4000 and row['TotalCitation'] < 8000):
        return 6
    elif(row['TotalCitation'] >=8000 and row['TotalCitation'] < 16000):
        return 7
    elif(row['TotalCitation'] >=16000):
        return 8

Author_data = pd.DataFrame(pd.read_csv('final_dataset.csv'))
Author_data["Class"] = Author_data.apply(classifier, axis=1)
Author_data_test = pd.DataFrame(pd.read_csv('test5kdata.csv'))
Author_data_test["Class"] = Author_data_test.apply(classifier, axis=1)
Author_data_test.head()

temp = Author_data.drop('AuthorName',axis = 1)
temp = temp.drop(['TotalCitation','CitationsPerYear'], axis = 1)


temp_test = Author_data_test.drop('AuthorName',axis = 1)
temp_test = temp_test.drop(['TotalCitation'], axis = 1)

Y = temp.Class
X = temp.drop('Class',axis = 1)
Y_test1 = temp_test.Class
X_test1 = temp_test.drop('Class', axis = 1)


X_test1.shape

train_samples = 40000

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, train_size=train_samples, test_size=5000)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_test1 =  scaler.transform(X_test1)

#Here we can use our Class Assignment programmed model(knn) for fitting purpose.
#However we have used sklearn package for this purpose

DataSet_Size = []
Accuracy = []
Accuracy1 = []
for x in range(1000,46000,4000):
    knn1 = KNeighborsClassifier(n_neighbors=5)
    clf = LogisticRegression(C=410./ 40000,
                         multi_class='multinomial',
                         penalty='l1', solver='saga', tol=0.1)
    train_samples1 = x
    print("Training dataset size:",round(((train_samples1/45000)*100)),'%')
    X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=train_samples1, test_size = 45000 - train_samples1)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    knn1.fit(X_train, y_train)
    pred = knn1.predict(X_test1)
    clf.fit(X_train, y_train)
    print('Multinomial Logistic Regression accuracy is:', clf.score(X_test1, Y_test1))
    print ('KNN accuracy is:', accuracy_score(Y_test1, pred))
    Accuracy1.append(clf.score(X_test1, Y_test1))
    DataSet_Size.append(x)
    Accuracy.append(accuracy_score(Y_test1, pred))
    print ("########################################################################")
    


fig = plt.figure()
Accuracy2 = [ '%.2f' % elem for elem in Accuracy ]
Accuracy3 = [ '%.2f' % elem for elem in Accuracy1 ]
Dataset1 = [ round(((elem/45000)*100)) for elem in DataSet_Size ]
plt.plot( Dataset1,Accuracy3,'C1', label='Multinomial LR')
plt.plot( Dataset1,Accuracy2,'C2', label='KNN(k=5)')
plt.legend()
plt.ylabel('Accuracy')
plt.xlabel('Dataset Size (In %)')
plt.title('Comparison between Multinomial LR and KNN')
plt.grid()
fig = plt.gcf()
fig.savefig('fig1.pdf')
plt.show()