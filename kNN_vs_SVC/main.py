import numpy as np
from sklearn import datasets
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

def evaluation_metrics(y_true, y_pred):
    # Calculate the evaluation metrics
    tp = np.sum(np.logical_and(y_true == 1, y_pred == 1))
    fp = np.sum(np.logical_and(y_true == 0, y_pred == 1))
    tn = np.sum(np.logical_and(y_true == 0, y_pred == 0))
    fn = np.sum(np.logical_and(y_true == 1, y_pred == 0))

    accuracy = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f_measure = 2 * precision * recall / (precision + recall)

    return accuracy, precision, recall, f_measure

def configurateDB (db, db_name):
    # Split the dataset into training and testing sets
    db_X_train, db_X_test, db_y_train, db_y_test = train_test_split(db.data, db.target, test_size=0.4, random_state=42)

    # Define the kNN classifier and set the number of neighbors
    knn = KNeighborsClassifier(n_neighbors=5)

    # Fit the kNN classifier with the dataset
    knn.fit(db_X_train, db_y_train)

    # Perform 10-fold cross-validation for the kNN classifier on the dataset
    knn_scores = cross_val_score(knn, db_X_train, db_y_train, cv=10)
    knn_accuracy, knn_precision, knn_recall, knn_f_measure = evaluation_metrics(db_y_test, knn.predict(db_X_test))

    print("\n ==== ==== " + db_name + " Dataset output ==== ====")
    print("\nkNN Classifier Evaluation Metrics on the " + db_name + " Dataset:")
    print("Accuracy:", knn_accuracy)
    print("Precision:", knn_precision)
    print("Recall:", knn_recall)
    print("F-measure:", knn_f_measure)

    # Define the support vector machine classifier and set the kernel and regularization parameter
    svm = SVC(kernel='linear', C=1.0)

    # Fit the SVM classifier with the dataset
    svm.fit(db_X_train, db_y_train)

    # Perform 10-fold cross-validation for the SVM classifier on the wines dataset
    svm_scores = cross_val_score(svm, db_X_train, db_y_train, cv=10)
    svm_accuracy, svm_precision, svm_recall, svm_f_measure = evaluation_metrics(db_y_test, svm.predict(db_X_test))

    print("\nSVM Classifier Evaluation Metrics on the " + db_name + " Dataset:")
    print("Accuracy:", svm_accuracy)
    print("Precision:", svm_precision)
    print("Recall:", svm_recall)
    print("F-measure:", svm_f_measure)


# Load the wines dataset
wines = datasets.load_wine()

# Load the iris dataset
iris = datasets.load_iris()

configurateDB(wines, "Wines")
configurateDB(iris, "Iris")

