

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    'Temperature': [60, 70, 80, 90, 100, 110],
    'Vibration': [2, 3, 4, 7, 8, 9],
    'Pressure': [40, 50, 60, 80, 90, 100],
    'Failure': [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Input and output
X = df[['Temperature', 'Vibration', 'Pressure']]
y = df['Failure']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict new machine condition
prediction = model.predict([[95, 8, 90]])

if prediction[0] == 1:
    print("Machine Failure")
else:
    print("No Machine Failure")
