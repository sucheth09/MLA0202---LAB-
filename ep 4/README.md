<img width="846" height="355" alt="Screenshot 2026-08-07 222001" src="https://github.com/user-attachments/assets/ebe21518-a1a2-4d0a-8b7b-ed9f52ab4e9b" />
from sklearn.neural_network import MLPClassifier

X = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

y = [0,1,1,0]

model = MLPClassifier(hidden_layer_sizes=(4,),
                      max_iter=5000,
                      random_state=1)

model.fit(X,y)

print("Training Completed")

print("\nPredictions:")

for sample in X:
    print(sample,"->",model.predict([sample])[0])

test = [[1,0]]
print("\nTest Sample:",test[0])
print("Prediction:",model.predict(test)[0])
