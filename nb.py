from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(2,2)
print('MODEL')
print(model)
# make predictions
expected = 2
predicted = model.predict(2)# summarize the fit of the model
print('RESULT')

print(metrics.classification_report(expected, predicted))
print('CONFUSION MATRIX')
print(metrics.confusion_matrix(expected, predicted))
