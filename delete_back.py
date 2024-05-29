import streamlit as st
from PIL import Image
from rembg import remove
import io
import os


# Functions

def process_image(image_upload):
    image = Image.open(image_upload)
    proccessed_image = remove_background(image)
    return proccessed_image

def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    proccesed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(proccesed_image_bytes))


# Front

st.image("assets/m3.jpg")
st.header("Backgroun Removal APP")
st.subheader("Upload an Image")
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Imagen subida", use_column_width=True)
    
    remove_button = st.button(label="Quitar fondo")
    
    if remove_button:
        
        proccesed_image = process_image(uploaded_image)
        
        st.image(proccesed_image, caption="Background Removed", use_column_width=True)
        
        proccesed_image.save("proccesed_image.png")
        
        with open("proccesed_image.png", "rb") as f:
            image_data = f.read()
        st.download_button("Download Processed Image", data=image_data, file_name="processed_image.png")
        os.remove("processed_image.png")