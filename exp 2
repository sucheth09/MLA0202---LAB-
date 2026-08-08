import numpy as np

def candidate_elimination(data):
    S = ['0'] * (len(data[0]) - 1)
    G = [['?' for _ in range(len(S))]]

    for example in data:
        if example[-1] == "Yes":
            for i in range(len(S)):
                if S[i] == '0':
                    S[i] = example[i]
                elif S[i] != example[i]:
                    S[i] = '?'
        else:
            for i in range(len(S)):
                if S[i] != example[i]:
                    G.append(['?' if j != i else S[j] for j in range(len(S))])
    
    return S, G

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
]

S, G = candidate_elimination(data)
print("Specific Hypothesis:", S)
print("General Hypothesis:", G)
