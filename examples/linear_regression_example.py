```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: study hours vs. exam score
X = np.array([[1], [2], [3], [4], [5]])  # hours studied
y = np.array([50, 60, 65, 70, 75])      # exam scores

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict score for 6 hours of study
hours = np.array([[6]])
predicted = model.predict(hours)
print(f"Predicted score for {hours[0][0]} hours of study: {predicted[0]:.2f}")
