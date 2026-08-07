def find_s(training_data):
    # Initialize hypothesis with None
    hypothesis = ['None'] * (len(training_data[0]) - 1)

    print("Initial Hypothesis:", hypothesis)

    # Process each training example
    for sample in training_data:
        if sample[-1].lower() == "yes":   # Consider only positive examples
            for i in range(len(hypothesis)):
                if hypothesis[i] == 'None':
                    hypothesis[i] = sample[i]
                elif hypothesis[i] != sample[i]:
                    hypothesis[i] = '?'

            print("Updated Hypothesis:", hypothesis)

    return hypothesis

training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

print("Training Data:")
for row in training_data:
    print(row)

print("\nRunning FIND-S Algorithm...\n")

final_hypothesis = find_s(training_data)

print("\nFinal Most Specific Hypothesis:")
print(final_hypothesis)



<img width="854" height="498" alt="Screenshot 2026-08-07 215241" src="https://github.com/user-attachments/assets/ece9a78d-de63-48e1-a81c-a50bb395f1ab" />
