import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('DogBreedClassifier.h5')
  return model
model=load_model()
st.write("""
# Dog Breed Classifier By Quizon, Repani, Repolidon, Revilla, Reyes"""
)
file=st.file_uploader("Choose a Dog photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(64,64)
    image=ImageOps.fit(image_data,size)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['ShibaInu', 'GoldenRetriever', 'GermanSheperd', 'Chihuahua']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)
