# Step 1: Import Required Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Generate Dummy Data (Can replace with actual structural dataset later)
def generate_structural_data(samples=200, features=10):
    np.random.seed(42)
    X = np.random.rand(samples, features)
    y = np.random.randint(0, 2, size=samples)  # 0: No damage, 1: Damaged
    return X, y

# Step 3: Artificial Immune Recognition System (Clonal Selection)
class AISClonalSelection:
    def __init__(self, num_detectors=20, mutation_rate=0.1):
        self.num_detectors = num_detectors
        self.mutation_rate = mutation_rate

    def train(self, X_train):
        indices = np.random.choice(len(X_train), self.num_detectors, replace=False)
        self.detectors = X_train[indices]

    def predict(self, X_test):
        predictions = []
        for sample in X_test:
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            nearest_index = np.argmin(distances)
            predicted_label = int(nearest_index % 2)  # Dummy label mapping
            predictions.append(predicted_label)
        return np.array(predictions)

# Step 4: Load Data and Split
X, y = generate_structural_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Train the AIS Model
ais_model = AISClonalSelection(num_detectors=20, mutation_rate=0.1)
ais_model.train(X_train)

# Step 6: Predict and Evaluate
y_pred = ais_model.predict(X_test)

# Step 7: Evaluation Metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 8 (Optional): Plot Accuracy Bar
accuracy = accuracy_score(y_test, y_pred)
plt.bar(['AIS Model'], [accuracy], color='green')
plt.title("Structural Damage Detection Accuracy")
plt.ylabel("Accuracy Score")
plt.ylim(0, 1)
plt.show()