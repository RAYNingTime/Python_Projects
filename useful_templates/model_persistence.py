import joblib

# save model to a file
def save_model(model, file_path):
    joblib.dump(model, file_path)

# load model from file
def load_model(file_path):
    return joblib.load(file_path)
