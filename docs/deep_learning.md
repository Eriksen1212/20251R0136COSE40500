# Deep Learning Overview

## 1. What Is Deep Learning?
Deep Learning is a subfield of machine learning that uses multi-layered neural networks to model complex patterns in data. Each layer extracts progressively higher-level features.

## 2. Core Architectures
1. **Feedforward Neural Networks (FNN)**  
2. **Convolutional Neural Networks (CNN)** — Excellent for images.  
3. **Recurrent Neural Networks (RNN)** / **LSTM/GRU** — Sequence data (text, time series).  
4. **Transformers** — Attention-based models (e.g., BERT, GPT).  

## 3. Typical Workflow
1. **Data Preparation** (normalization, augmentation)  
2. **Model Design** (layers, activation functions)  
3. **Training** (backpropagation, optimizer)  
4. **Evaluation** (loss, accuracy)  
5. **Deployment** (exporting model weights)

## 4. Code Snippet: Simple Keras Model

```python
# examples/simple_dl_model.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Build a simple feedforward network for MNIST-like data
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Assume X_train, y_train are preloaded NumPy arrays
# model.fit(X_train, y_train, epochs=5)
