import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Load the model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('DogBreedClassifier.h5')
    return model

model = load_model()

# Function to preprocess and make predictions
def import_and_predict(image_data, model):
    size = (64, 64)
    image = ImageOps.fit(image_data, size)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...] / 255.0  # Normalize pixel values
    return model.predict(img_reshape)

# Streamlit UI
st.write("""
# Dog Breed Classifier
""")
file = st.file_uploader("Choose a Dog photo from computer", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image file")
else:
    try:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        prediction = import_and_predict(image, model)
        class_names = ['ShibaInu', 'GoldenRetriever', 'GermanSheperd', 'Chihuahua']
        predicted_class = class_names[np.argmax(prediction)]
        st.success(f"Prediction: {predicted_class}")
    except Exception as e:
        st.error("An error occurred:")
        st.error(str(e))
