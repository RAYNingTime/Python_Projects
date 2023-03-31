**scikit-learn** comes with a few small standard ![datasets](https://scikit-learn.org/stable/datasets/toy_dataset.html) that do not require to download any
file from some external website. The wine dataset, includes 13 Attributes, 178 Instances and
3 Classes. These data are the results of a chemical analysis of wines grown in the same region
in Italy but derived from three different cultivars. The analysis determined the quantities of
13 constituents found in each of the three types of wines.

Use Python to train a decision tree classifier on the wine dataset. Don’t use the full dataset
for training. Use 70% and the rest, save it for testing. We are going to discuss more on
appropriate testing in the following sections but for now, we need to calculate a simple
measure of predictive performance which is:

𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 = 𝐶𝑜𝑟𝑟𝑒𝑐𝑡 𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛𝑠 / 𝑇𝑜𝑡𝑎𝑙 𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛𝑠

Calculate, printout and report on the accuracy of the decision tree classifier.

* Bonus. Try and experiment with the parameters of the algorithm a little bit. Focus on the
parameters that you have studied in the theoretical part of this section (see study material).
By changing the parameters, try to improve the accuracy that you have achieved with the
default settings. Is it easy to improve? Explain, what is the reason for that.

* Super Bonus. Report on your above experimentations by providing plots, where you change
the values of each parameters with a small step (x-axis) and measure the accuracy (y-axis).
Try to do the same thing for another classification dataset of your own choice (preferably with
similar number of classes but larger in terms of attributes or instances). Comment on the
results.

* Deliverables: The python code. Make sure the code is self contained (i.e. no external files
are necessary to run it). You can report of the accuracy you have achieved in the comments
of your code. For the bonus part, you can upload a report on a pdf file. Notebooks with results
are also acceptable but please export them as pdf as well.

____

* Resources
Wine dataset – Original Source
https://archive.ics.uci.edu/ml/datasets/Wine
Decision Tree Classifier at scikit-learn
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
Decision Tree Classifier, user guide, at scikit-learn
https://scikit-learn.org/stable/modules/tree.html#tree
