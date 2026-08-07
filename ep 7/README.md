<img width="832" height="368" alt="Screenshot 2026-08-07 222554" src="https://github.com/user-attachments/assets/73ebefba-32f2-42a3-b22e-afbbb6c580a6" />
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = LogisticRegression(max_iter=5000)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Predicted Values")
print(prediction)

print("\nActual Values")
print(y_test)

print("\nAccuracy")
print(accuracy_score(y_test, prediction))
