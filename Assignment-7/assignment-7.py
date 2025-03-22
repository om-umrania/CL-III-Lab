# === Artificial Immune Pattern Recognition System for Structural Damage Classification ===
# Fulfilling Assignment 7 steps from Computer Lab III - Distributed Computing

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1: Structure Data (Healthy & Damaged)
def generate_structural_data(samples=2000000, features=10):
    X = np.random.rand(samples, features)
    y = np.random.randint(0, 2, size=samples)  # 0 = Healthy, 1 = Damaged
    return X, y

# Step 2: Feature Extraction is simulated by random values in this dummy setup.

# Step 3: Data Encoding (Here, we simulate encoding by normalization)
def encode_data(X):
    return (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0) + 1e-6)

# Step 4: AIS Algorithm - Simplified Clonal Selection Model class
class AISClassifier:
    def __init__(self, num_detectors=10, mutation_rate=0.1):
        self.num_detectors = num_detectors
        self.mutation_rate = mutation_rate

    def train(self, X_train, y_train):
        # Select random detectors
        self.detectors = X_train[np.random.choice(len(X_train), self.num_detectors, replace=False)]
        self.labels = y_train[np.random.choice(len(y_train), self.num_detectors, replace=False)]

    def predict(self, X_test):
        predictions = []
        for sample in X_test:
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            nearest = np.argmin(distances)
            predictions.append(self.labels[nearest])
        return np.array(predictions)

# Step 5: Training and Testing the Model
X, y = generate_structural_data(samples=2000, features=8)
X_encoded = encode_data(X)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

model = AISClassifier(num_detectors=20, mutation_rate=0.1)
model.train(X_train, y_train)

# Step 6: Damage Detection (Prediction)
y_pred = model.predict(X_test)

# Step 7: Accuracy Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"\nClassification Accuracy: {accuracy * 100:.2f}%")
print("\nConfusion Matrix:")
print(conf_matrix)

# Step 8: Visualization (optional but informative)
plt.figure(figsize=(6,4))
plt.title("Confusion Matrix")
plt.imshow(conf_matrix, cmap='Blues', interpolation='nearest')
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.colorbar()
plt.show()

# === End of Assignment 7 Implementation ===
# Each step from the manual has been implemented in a simplified and demonstrable way.
