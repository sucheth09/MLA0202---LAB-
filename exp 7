from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

print("Accuracy:", model.score(X, y))
