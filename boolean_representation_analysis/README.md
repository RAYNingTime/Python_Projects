# Boolean Representation of Text Documents - Python Implementation

This project aims to implement a Boolean representation of text documents using Python. The boolean representation is a popular way to represent documents in which each document is represented with the same attributes - all words in the vocabulary. The attribute values in this case are 0 or 1. The value is 1 in case the word appears in the document or 0 in case it doesn't.

## Problem

The boolean representation of documents has some disadvantages. One of the main disadvantages is that it does not consider the frequency of words in the document. As a result, words that occur frequently in the document are not given any extra weightage. To alleviate this issue, other representations such as TF-IDF can be used.

## Implementation

The project implements a python code that analyzes a set of .txt files and exports a CSV file with the Boolean representation of each document. The code first reads all the .txt files from the specified directory and creates a vocabulary by extracting unique words from all documents. It then generates a Boolean representation of each document using the vocabulary and exports the results to a CSV file.

## Usage

To use the code, you can download the code from the repository and run the boolean_representation.py file. The code requires a directory containing the .txt files as input. Please provide a set of .txt files along with the code that will verify that the code works correctly.

## Optional Bonus

As an optional bonus, the project also implements an alternative representation to the Boolean representation mentioned above. The alternative representation considers the frequency of words in the document and assigns weights to words accordingly. 

## Conclusion

This project provides a Python implementation of the Boolean representation of text documents. Although the Boolean representation has some disadvantages, it is a popular way to represent documents and is useful in certain scenarios. The code is provided as an example for those interested in implementing the Boolean representation themselves.
