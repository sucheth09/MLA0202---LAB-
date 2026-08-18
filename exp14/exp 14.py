import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.DataFrame({
    "Area": [1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 1600, 1900],
    "Bedrooms": [2, 3, 3, 4, 4, 4, 5, 5, 3, 4],
    "Age": [10, 8, 5, 7, 4, 3, 2, 1, 6, 5],
    "Price": [250000, 320000, 380000, 450000, 500000, 560000, 620000, 680000, 350000, 420000]
})

X = data[["Area", "Bedrooms", "Age"]]
y = data["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)

print("\nMean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

new_house = pd.DataFrame({
    "Area": [2100],
    "Bedrooms": [4],
    "Age": [3]
})

prediction = model.predict(new_house)

print("\nPredicted Price for New House:")
print(prediction[0])
