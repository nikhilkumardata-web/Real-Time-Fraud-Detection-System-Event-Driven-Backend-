from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([[100], [200], [5000], [8000]])
y = [0, 0, 1, 1]

model = RandomForestClassifier()
model.fit(X, y)

def predict_fraud(amount):
    return model.predict([[amount]])[0]
