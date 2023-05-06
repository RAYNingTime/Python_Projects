# Made by Ivan Kosiakov (U214N1534) on 06/05/2023

from sklearn import datasets
from sklearn.model_selection import cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

def configurateDB (ds, ds_name):
    # Split the dataset into training and testing sets
    X, y = ds.data, ds.target

    # Define the kNN classifier and set the number of neighbors
    knn = KNeighborsClassifier(n_neighbors=5)

    # Define the support vector machine classifier and set the kernel and regularization parameter
    svm = SVC(kernel='linear', C=1.0)

    scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']

    # Fit the kNN classifier with the dataset
    cv_knn = cross_validate(knn, X, y, cv=10, scoring=scoring)
    cv_svc = cross_validate(svm, X, y, cv=10, scoring=scoring)

    print("\n ==== ==== ==== ====")
    print("\nkNN Classifier Evaluation Metrics on the " + ds_name + " Dataset:")
    print("Accuracy:", cv_knn['test_accuracy'].mean())
    print("Precision:", cv_knn['test_precision_macro'].mean())
    print("Recall:", cv_knn['test_recall_macro'].mean())
    print("F-measure:", cv_knn['test_f1_macro'].mean())

    print("\nSVM Classifier Evaluation Metrics on the " + ds_name + " Dataset:")
    print("Accuracy:", cv_svc['test_accuracy'].mean())
    print("Precision:", cv_svc['test_precision_macro'].mean())
    print("Recall:", cv_svc['test_recall_macro'].mean())
    print("F-measure:", cv_svc['test_f1_macro'].mean())


# Load the wines dataset
wines = datasets.load_wine()

# Load the iris dataset
iris = datasets.load_iris()

configurateDB(wines, "Wines")
configurateDB(iris, "Iris")

# kNN Classifier Evaluation Metrics on the Wines Dataset:
# Accuracy: 0.6754901960784313
# Precision: 0.6652320827320827
# Recall: 0.6584920634920635
# F-measure: 0.645921660039307
#
# SVM Classifier Evaluation Metrics on the Wines Dataset:
# Accuracy: 0.9555555555555555
# Precision: 0.9642195767195767
# Recall: 0.9573015873015873
# F-measure: 0.9556129981129982
#
#  ==== ==== ==== ====
#
# kNN Classifier Evaluation Metrics on the Iris Dataset:
# Accuracy: 0.9666666666666668
# Precision: 0.9738095238095239
# Recall: 0.9666666666666666
# F-measure: 0.9659090909090908
#
# SVM Classifier Evaluation Metrics on the Iris Dataset:
# Accuracy: 0.9733333333333334
# Precision: 0.9793650793650794
# Recall: 0.9733333333333333
# F-measure: 0.9726430976430975

# Based on the evaluation results, it can be concluded that the SVM algorithm performed
# slightly better than the KNN algorithm in classifying the wine and iris datasets. The
# evaluation was done using 10-fold cross-validation and four performance metrics: Accuracy,
# Precision, Recall, and F-Measure. Therefore, for these particular datasets, the SVM algorithm
# is the most suitable for classification.
