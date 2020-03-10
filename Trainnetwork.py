from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

names = ['C1,2','C1,3','C1,4','C1,5','C1,6','C1,7','C1,8','C1,9','C1,10','C1,11','C1,12','C2,3','C2,4','C2,5','C2,6','C2,7','C2,8','C2,9','C2,10','C2,11','C2,12','C3,4','C3,5','C3,6','C3,7','C3,8','C3,9','C3,10','C3,11','C3,12','C4,5','C4,6','C4,7','C4,8','C4,9','C4,10','C4,11','C4,12','C5,6','C5,7','C5,8','C5,9','C5,10','C5,11','C5,12','C6,7','C6,8','C6,9','C6,10','C6,11','C6,12','C7,8','C7,9','C7,10','C7,11','C7,12','C8,9','C8,10','C8,11','C8,12','C9,10','C9,11','C9,12','C10,11','C10,12','C11,12','flowtype']
dataset= read_csv("values.csv",names=names)
#print(dataset.shape)
#print(dataset.head(20))
#print(dataset.describe())
#print(dataset.groupby('flowtype').size())

# histograms
#dataset.hist()
#plt.show()
# Split-out validation dataset

array = dataset.values
X = array[:,0:65]
y = array[:,66]
X_train, X_validation,Y_train, Y_validation = train_test_split(X,y ,test_size=0.20, shuffle=False)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, shuffle=False)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))