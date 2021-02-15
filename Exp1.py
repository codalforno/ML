import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

print(digits.data)
print('\n', digits.data.shape)
print('\n', digits.target)
print('\n', digits.target.shape)
print('\n', digits.images[0])
print('\n', digits.images[0].shape)
print(digits.data[0])
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-1:]))