import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4]])
y = np.array([1,4,9,16])

lin = LinearRegression()
lin.fit(X, y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

print("Linear Prediction:", lin.predict([[5]]))
print("Polynomial Prediction:", poly_model.predict(poly.transform([[5]])))
