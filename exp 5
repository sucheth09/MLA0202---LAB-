from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Prediction:", model.predict([X[0]]))
