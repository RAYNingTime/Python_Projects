from sklearn.naive_bayes import MultinomialNB

def naive_bayes(X, y):
    # create a Naive Bayes classifier object
    model = MultinomialNB()
    # fit the model to the data
    model.fit(X, y)
    # return the model
    return model
