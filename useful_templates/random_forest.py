from sklearn.ensemble import RandomForestClassifier

def random_forest(X, y):
    # create a Random Forest classifier object
    model = RandomForestClassifier()
    # fit the model to the data
    model.fit(X, y)
    # return the model
    return model
