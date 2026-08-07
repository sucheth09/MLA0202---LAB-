from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

X = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 2, 1, 0],
    [2, 2, 1, 1],
    [1, 2, 1, 1],
    [0, 1, 0, 0],
    [0, 2, 1, 0],
    [2, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [2, 1, 0, 1]
]

Y = [0,0,1,1,1,0,1,0,1,1,1,1,1,0]

clf = DecisionTreeClassifier(criterion="entropy")

clf.fit(X, Y)

print("Decision Tree Model Built Successfully")

new_sample = [[0,2,0,1]]

prediction = clf.predict(new_sample)

print("\nNew Sample:", new_sample)

if prediction[0] == 1:
    print("Prediction: Yes")
else:
    print("Prediction: No")

feature_names = ["Outlook", "Temperature", "Humidity", "Wind"]

print("\nDecision Tree Rules:\n")
print(tree.export_text(clf, feature_names=feature_names))
