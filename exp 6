from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target

model = GaussianNB()
model.fit(X, y)

pred = model.predict(X)

print("Confusion Matrix:\n", confusion_matrix(y, pred))
print("Accuracy:", accuracy_score(y, pred))
