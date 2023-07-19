import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from tkinter import *

# Load the dataset (replace 'data.csv' with your actual data file)
data = pd.read_csv('data.csv')

# Assuming 'mental_health' is the column representing the mental health label (0 or 1)
X = data.drop(columns=['mental_health'])
y = data['mental_health']

# Create and train the decision tree classifier
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X, y)

# Function to predict mental health and display the result
def predict_mental_health():
    input_data = [float(entry.get()) for entry in entry_fields]
    result = classifier.predict([input_data])[0]

    if result == 0:
        result_label.config(text="Healthy")
    else:
        result_label.config(text="Potential mental health issues")

# UI setup
root = Tk()
root.title("Mental Health Predictor")
root.geometry("400x200")

entry_labels = ["Feature 1", "Feature 2", "Feature 3"]  # Replace with actual feature names
entry_fields = []

# Create input fields for each feature
for idx, label_text in enumerate(entry_labels):
    label = Label(root, text=label_text)
    label.grid(row=idx, column=0, padx=10, pady=10)

    entry_field = Entry(root)
    entry_field.grid(row=idx, column=1, padx=10, pady=10)

    entry_fields.append(entry_field)

# Result label
result_label = Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=len(entry_labels) + 1, columnspan=2, padx=10, pady=20)

# Prediction button
predict_button = Button(root, text="Predict", command=predict_mental_health)
predict_button.grid(row=len(entry_labels) + 2, columnspan=2, padx=10, pady=10)

root.mainloop()
