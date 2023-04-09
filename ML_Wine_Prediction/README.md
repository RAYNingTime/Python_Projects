# Decision Tree Classifier on Wine Dataset
This repository contains Python code to train a decision tree classifier on the wine dataset available in scikit-learn. The wine dataset includes 13 attributes, 178 instances, and 3 classes. These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines.
The decision tree classifier is trained using 70% of the dataset for training and the remaining 30% for testing. The accuracy of the classifier is calculated using the formula:

𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 = 𝐶𝑜𝑟𝑟𝑒𝑐𝑡 𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛𝑠 / 𝑇𝑜𝑡𝑎𝑙 𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛𝑠

The accuracy of the classifier is reported in the comments of the Python code.

## Bonus
An experiment is conducted to improve the accuracy of the decision tree classifier by changing the parameters of the algorithm. The parameters studied in the theoretical part of this section are focused on. By changing the parameters, the accuracy of the classifier is improved from the default settings. The report on the experimentations is provided in a PDF file which is uploaded alongside the Python code.

## Super Bonus
The values of each parameter are changed with a small step and the accuracy is measured. The same experiment is conducted on another classification dataset with a similar number of classes but larger in terms of attributes or instances. The results are reported in a PDF file which is uploaded alongside the Python code.

## Resources
- [Wine dataset – Original Source](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [Decision Tree Classifier at scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [Decision Tree Classifier, user guide, at scikit-learn](https://scikit-learn.org/stable/modules/tree.html#tree)
