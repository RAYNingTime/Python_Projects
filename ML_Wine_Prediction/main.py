# pip install pandas scikit-learn numpy matplotlib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Reading the data set
data = pd.read_csv('wine.data', header=None)

# The attributes are:
#  	1) Alcohol, 2) Malic acid, 3) Ash, 4) Alcalinity of ash
#  	5) Magnesium, 6) Total phenols, 7) Flavanoids, 8) Nonflavanoid phenols
#  	9) Proanthocyanins, 10)Color intensity, 11)Hue
#  	12)OD280/OD315 of diluted wines, 13)Proline
data.columns = column_names = [
    'Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
    'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
    'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline'
]

X = data.drop('Class', axis=1)
y = data['Class']

# Using 70% and the rest, save it for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Setting up a max depth depending on the number of columns in X (excluding the column 'Class')
max_depths = [i for i in range(1, X.shape[1] + 1)]

# Pre-created arrays to save the result of the calculations
train_scores = []
test_scores = []
for max_depth in max_depths:
    # Setting the max_depth of the Decision Tree for each loop
    clf = DecisionTreeClassifier(max_depth=max_depth)
    clf.fit(X_train, y_train)

    # Prediction of the training set and accuracy calculation
    train_pred = clf.predict(X_train)
    train_accuracy = accuracy_score(y_true=y_train, y_pred=train_pred)

    # Prediction of the test set and accuracy calculation
    test_pred = clf.predict(X_test)
    test_accuracy = accuracy_score(y_true=y_test, y_pred=test_pred)

    # Append scores
    train_scores.append(train_accuracy)
    test_scores.append(test_accuracy)

# Setting up a plot and showing it
plt.plot(max_depths, test_scores, label='Test')
plt.plot(max_depths, train_scores, label='Train')
plt.ylabel('Accuracy Score')
plt.xlabel('Maximum Depth')
plt.legend(loc='upper left')
plt.show()
