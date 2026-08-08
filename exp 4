from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

data = load_iris()

X = data.data
y = data.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=3000,
    random_state=42
)

model.fit(X, y)

print("Accuracy:", model.score(X, y))
