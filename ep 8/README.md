from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X, y = make_regression(
    n_samples=100,
    n_features=1,
    noise=10,
    random_state=1
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Predicted Values")
print(prediction[:10])

print("\nActual Values")
print(y_test[:10])

print("\nIntercept")
print(model.intercept_)

print("\nCoefficient")
print(model.coef_)
