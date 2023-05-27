from sklearn.svm import SVC

def support_vector_machine(X, y):
    model = SVC()
    model.fit(X, y)
    return model
