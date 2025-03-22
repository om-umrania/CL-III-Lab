# === Artificial Immune Pattern Recognition System for Structural Damage Classification ===
# Fulfilling Assignment 7 steps from Computer Lab III - Distributed Computing

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Simulate Structured Dataset (Replace this with real dataset for practical use)
def generate_structural_data(samples=2000, features=8):
    data = pd.DataFrame(np.random.rand(samples, features), columns=[f"feature_{i+1}" for i in range(features)])
    data['district_id'] = np.random.choice(range(12, 37), samples)
    data['damage_grade'] = np.random.choice(['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5'], samples, p=[0.1, 0.15, 0.25, 0.25, 0.25])
    data['land_surface_condition'] = np.random.choice(['Flat', 'Moderate slope', 'Steep slope'], samples, p=[0.82, 0.13, 0.05])
    data['foundation_type'] = np.random.choice(['Mud mortar-Stone/Brick', 'Bamboo/Timber', 'Cement-Stone/Brick', 'RC', 'Other'], samples, p=[0.63, 0.1, 0.1, 0.1, 0.07])
    data['roof_type'] = np.random.choice(['Bamboo/Timber-Light roof', 'Bamboo/Timber-Heavy roof', 'RCC/RB/RBC'], samples, p=[0.6, 0.25, 0.15])
    data['ground_floor_type'] = np.random.choice(['Mud', 'RC', 'Brick/Stone', 'Timber', 'Other'], samples, p=[0.6, 0.12, 0.12, 0.1, 0.06])
    data['other_floor_type'] = np.random.choice(['TImber/Bamboo-Mud', 'Timber-Planck', 'Not applicable', 'RCC/RB/RBC'], samples, p=[0.64, 0.16, 0.16, 0.04])
    data['vdcmun_id'] = np.random.choice(range(1, 111), samples)
    data['ward_id'] = np.random.choice(range(1, 946), samples)
    return data

# Create Dataset
df_stru = generate_structural_data()

# === Data Exploration ===
print("\nInitial Glimpse of Dataset (df.head()):")
print(df_stru.head())

print("\nData Structure Overview (df.info()):")
df_stru.info()

print("\nStatistical Summary (df.describe()):")
print(df_stru.describe(include='all'))

print("\nColumn Data Types (df.dtypes):")
print(df_stru.dtypes)

# Introduce missing values
df_stru.loc[np.random.choice(df_stru.index, 50), 'feature_2'] = np.nan

# Handle Missing Data
df_temp = df_stru.isnull().sum().reset_index(name='count')
print(df_temp[df_temp['count'] > 0])
df_stru.dropna(inplace=True)

# Display All Categorical Features
print("\nCategorical Feature Distributions:")
for col in ['land_surface_condition', 'foundation_type', 'roof_type', 'ground_floor_type', 'other_floor_type']:
    print(f"\n{col} distribution:")
    print(df_stru[col].value_counts(normalize=True))

# One-Hot Encoding of Categorical Features
categorical_features = ['land_surface_condition', 'foundation_type', 'roof_type', 'ground_floor_type', 'other_floor_type']
df_encoded = pd.get_dummies(df_stru[categorical_features], drop_first=True)

# Combine with numerical features
feature_cols = [col for col in df_stru.columns if col.startswith('feature_')]
X_numeric = df_stru[feature_cols].reset_index(drop=True)
X_combined = pd.concat([X_numeric, df_encoded.reset_index(drop=True)], axis=1)

X = X_combined.values
y_map = {'Grade 1': 0, 'Grade 2': 1, 'Grade 3': 2, 'Grade 4': 3, 'Grade 5': 4}
y = df_stru['damage_grade'].map(y_map).values

# Normalize Features
def encode_data(X):
    return (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0) + 1e-6)
X_encoded = encode_data(X)

# Enhanced AIS Classifier with Mutation and Cloning
class AISClassifier:
    def __init__(self, num_detectors=10, mutation_rate=0.1, clone_rate=3, max_generations=10):
        self.num_detectors = num_detectors
        self.mutation_rate = mutation_rate
        self.clone_rate = clone_rate
        self.max_generations = max_generations
        self.convergence_history = []

    def _mutate(self, detector):
        mutation_vector = np.random.normal(0, self.mutation_rate, size=detector.shape)
        return np.clip(detector + mutation_vector, 0, 1)

    def train(self, X_train, y_train):
        self.detectors = np.asarray(X_train[np.random.choice(len(X_train), self.num_detectors, replace=False)], dtype=np.float64)
        self.labels = y_train[np.random.choice(len(y_train), self.num_detectors, replace=False)]

        for gen in range(self.max_generations):
            mutated_detectors = []
            mutated_labels = []
            distances = []

            for i in range(len(self.detectors)):
                for _ in range(self.clone_rate):
                    clone = self.detectors[i].copy()
                    mutated = self._mutate(clone)
                    mutated_detectors.append(mutated)
                    mutated_labels.append(self.labels[i])
                    distance = np.linalg.norm(mutated - self.detectors[i])
                    distances.append(distance)

            avg_distance = np.mean(distances)
            self.convergence_history.append(avg_distance)
            self.detectors = np.array(mutated_detectors[:self.num_detectors])
            self.labels = np.array(mutated_labels[:self.num_detectors])

    def predict(self, X_test):
        predictions = []
        self.detectors = np.asarray(self.detectors, dtype=np.float64)
        for sample in X_test:
            sample = np.asarray(sample, dtype=np.float64)
            if sample.ndim > 1:
                sample = sample.flatten()
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            nearest = np.argmin(distances)
            predictions.append(self.labels[nearest])
        return np.array(predictions)

    def plot_convergence(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 4))
        plt.plot(self.convergence_history, marker='o')
        plt.title("Detector Convergence over Generations")
        plt.xlabel("Generation")
        plt.ylabel("Average Mutation Distance")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Train/Test Split and Classification
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)
model = AISClassifier(num_detectors=20, mutation_rate=0.05, clone_rate=4, max_generations=15)
model.train(X_train, y_train)
y_pred = model.predict(X_test)

# Classification Metrics
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=list(y_map.keys()))

print(f"\nClassification Accuracy: {accuracy * 100:.2f}%")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report (Precision, Recall, F1-score):")
print(class_report)

# Visualize Confusion Matrix
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(6,4))
plt.title("Confusion Matrix")
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Visualize Detector Convergence
model.plot_convergence()
