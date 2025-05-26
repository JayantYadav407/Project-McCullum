# train_model.py

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
import os

# Paths to dataset directories
DATASET_PATH = 'data3'  # Replace with your dataset path
CATEGORIES = ['cats', 'dogs']

# Ensure dataset structure is correct
for category in CATEGORIES:
    assert os.path.exists(os.path.join(DATASET_PATH, category)), f"Missing {category} directory."

# Image Data Preparation
datagen = ImageDataGenerator(
    rescale=1.0/255,  # Normalize pixel values
    validation_split=0.2  # 80% train, 20% validation
)

# Training Data
train_data = datagen.flow_from_directory(
    directory=DATASET_PATH,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

# Validation Data
val_data = datagen.flow_from_directory(
    directory=DATASET_PATH,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Pre-trained Model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(150, 150, 3))
base_model.trainable = False  # Freeze base layers

# Custom Model
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train Model
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10,
    verbose=1
)

# Save Model
model.save('cat_dog_classifier.h5')

# Evaluation
loss, accuracy = model.evaluate(val_data)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")
