from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def perform_cross_validation(X, y, cv=5):
    model = RandomForestClassifier()
    scores = cross_val_score(model, X, y, cv=cv)
    return scores.mean()
