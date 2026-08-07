<img width="843" height="328" alt="Screenshot 2026-08-07 222425" src="https://github.com/user-attachments/assets/4a9a2e4e-60cf-4c8a-a55a-4c5c3c1a838b" />
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

iris=load_iris()

X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(
X,y,test_size=0.3,random_state=1)

model=GaussianNB()

model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("Predicted Values")
print(prediction)

print("\nActual Values")
print(y_test)

print("\nConfusion Matrix")
print(confusion_matrix(y_test,prediction))

print("\nAccuracy")
print(accuracy_score(y_test,prediction))
