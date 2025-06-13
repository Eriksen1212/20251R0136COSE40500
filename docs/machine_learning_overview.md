# Machine Learning Overview

## 1. What Is Machine Learning?
Machine Learning (ML) is a field of artificial intelligence that enables computers to learn patterns and make predictions or decisions without being explicitly programmed for each task. Instead of writing rules by hand, ML algorithms infer rules from data.

## 2. Main Learning Paradigms
1. **Supervised Learning**  
   - Learns a mapping from input to output using labeled examples  
   - Common tasks: Regression, Classification  

2. **Unsupervised Learning**  
   - Discovers hidden structure in unlabeled data  
   - Common tasks: Clustering, Dimensionality Reduction  

3. **Reinforcement Learning**  
   - An agent interacts with an environment, learning to maximize cumulative reward  
   - Common applications: Game playing, Robotics  

4. **Semi-supervised Learning**  
   - Combines a small amount of labeled data with a large amount of unlabeled data  

5. **Self-supervised Learning**  
   - Creates its own labels from the data for tasks like pretraining  

## 3. Typical Workflow
1. **Data Collection & Cleaning**  
2. **Feature Engineering**  
3. **Model Selection**  
4. **Training & Validation**  
5. **Evaluation & Deployment**

---

## 4. Example: Linear Regression with scikit-learn

See the accompanying script for a minimal working example.

```python
# examples/linear_regression_example.py

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
