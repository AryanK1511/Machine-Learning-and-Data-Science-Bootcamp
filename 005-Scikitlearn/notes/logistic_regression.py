import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Create synthetic data with 2 features, where the number of informative features is 2
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Visualize the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate values for plotting
x_vals = np.linspace(-10, 10, 100)
y_vals = sigmoid(x_vals)

# Plot sigmoid curve
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r'$\sigma(x) = \frac{1}{1 + e^{-x}}$', color='blue')
plt.title('Sigmoid Function')
plt.xlabel('Input value (x)')
plt.ylabel('Sigmoid output')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.legend()
plt.show()

# Visualize the decision boundary
plt.figure(figsize=(8, 6))

# Plot the decision boundary
xx, yy = np.meshgrid(np.linspace(X_train[:, 0].min(), X_train[:, 0].max(), 100),
                     np.linspace(X_train[:, 1].min(), X_train[:, 1].max(), 100))

Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, levels=np.linspace(0, 1, 11), cmap="Blues", alpha=0.6)
plt.colorbar(label='Probability of Class 1')

# Plotting the data points
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', cmap=plt.cm.RdYlBu, marker='o', alpha=0.8)
plt.title('Decision Boundary and Data Points')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
