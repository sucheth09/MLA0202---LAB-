<img width="848" height="279" alt="Screenshot 2026-08-07 221035" src="https://github.com/user-attachments/assets/dde477da-d82e-49c8-8a96-4d1e5f109396" />
# Candidate Elimination Algorithm

training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

num_attributes = len(training_data[0]) - 1

# Initialize Specific and General Hypotheses
S = ['0'] * num_attributes
G = [['?'] * num_attributes]

print('Initial Specific Hypothesis (S):', S)
print('Initial General Hypothesis (G):', G)

for example in training_data:
    attributes = example[:-1]
    label = example[-1].lower()

    if label == 'yes':
        G = [g for g in G if all(g[i] == '?' or g[i] == attributes[i] for i in range(num_attributes))]

        for i in range(num_attributes):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:<img width="848" height="279" alt="Screenshot 2026-08-07 221035" src="https://github.com/user-attachments/assets/5376434e-b5c4-4c21-b838-7b0c20a41185" />

                S[i] = '?'

    else:
        new_G = []
        for g in G:
            for i in range(num_attributes):
                if g[i] == '?':
                    if S[i] != '?':
                        new_h = g.copy()
                        new_h[i] = S[i]
                        new_G.append(new_h)
        G = new_G

    print('\nTraining Example:', example)
    print('Specific Hypothesis:', S)
    print('General Hypothesis:', G)

print('\nFinal Specific Hypothesis:')
print(S)

print('\nFinal General Hypothesis:')
for hypothesis in G:
    print(hypothesis)
