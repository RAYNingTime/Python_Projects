# Imported os to work with files
import os
# Imported csv to export a result as csv file
import csv
# Imported string to remove all punctuation signs from words
import string

# Filter for the unwanted words
# If FILTER = True it'll remove all the unwanted words
# If FILTER = False it'll let the word be untouched
FILTER = True
filtered_words = ["the", "is", "are", "am", "and", "or", "for",
                  "an", "a", "in", "on", "of", "to", "at", "by",
                  "from", "with", "about", "above", "after", "before",
                  "below", "between", "but", "down", "during", "except",
                  "off", "out", "over", "past", "since", "through",
                  "until", "up", "via", "within", "without"]

# Getting a full path to the folder of data set
path = os.path.join(os.getcwd(), "dataSet")

# Variables that are going to save data for the future work
dictionary = set()
document_term_matrix = []

# Going through all the documents and saving all the unique words in the dictionary
for filename in os.listdir(path):
    if filename.endswith('.txt'):
        with open(os.path.join(path, filename), "r") as file:
            # Removing all punctuation signs while reading data
            data = file.read().translate(str.maketrans("", "", string.punctuation))
            words = data.split()
            dictionary.update(words)

if FILTER:
    filtered_dictionary = []
    for word in dictionary:
        if word.lower() not in filtered_words:
            filtered_dictionary.append(word)
    dictionary = filtered_dictionary


print(dictionary)

# Cycling through all the documents and checking each word from dictionary for appearance in that document
for filename in os.listdir(path):
    if filename.endswith('.txt'):
        with open(os.path.join(path, filename), "r") as file:
            # Removing all punctuation signs while reading data
            data = file.read().translate(str.maketrans("", "", string.punctuation))
            words = data.split()
            row = []
            for word in dictionary:
                if word in words:
                    row.append(1)
                else:
                    row.append(0)

            document_term_matrix.append(row)

# Creating a CSV file with the results that is going to show a dictionary and all the results for every document
with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(dictionary)

    for row in document_term_matrix:
        writer.writerow(row)
