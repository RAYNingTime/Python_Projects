import eli5

# Explain the model predictions using feature importance
def explain_model(model, X, feature_names):
    explanation = eli5.explain_weights(model, feature_names=feature_names)
    return explanation
