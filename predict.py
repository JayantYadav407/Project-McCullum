# predict_images.py

import tensorflow as tf
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the trained model
model = tf.keras.models.load_model('cat_dog_classifier.h5')

# Function to prepare image for prediction
def prepare_image(image_path):
    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img) / 255.0  # Normalize the pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Prediction Function
def predict_image(image_path):
    img_array = prepare_image(image_path)
    prediction = model.predict(img_array)
    return 'Dog' if prediction[0][0] > 0.5 else 'Cat'

# Predict on multiple images
def predict_multiple_images(image_paths):
    predictions = {}
    for path in image_paths:
        result = predict_image(path)
        predictions[path] = result
    return predictions

# Example usage
if __name__ == "__main__":
    # List of images to predict
    image_paths = ['man2.jpg']  # Replace with actual image paths
    
    predictions = predict_multiple_images(image_paths)
    
    # Print predictions
    for image_path, prediction in predictions.items():
        print(f"Prediction for {image_path}: {prediction}")
