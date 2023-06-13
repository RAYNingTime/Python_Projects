import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocess_text(text):
    for index, email in text.items():

        # Remove special characters and numbers
        email = re.sub(r'[^a-zA-Z]', ' ', email)

        # Convert to lowercase
        email = email.lower()

        # Tokenize text into words
        words = word_tokenize(email)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]

        # Join the words back into a single string
        processed_text = ' '.join(words)

        # Plug processed email back
        text[index] = processed_text

    return text
