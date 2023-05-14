from sklearn.tree import DecisionTreeClassifier

def decision_tree(X, y):
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model
