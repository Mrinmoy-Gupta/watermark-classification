import streamlit as st
import os
import numpy as np
import keras
from PIL import Image, ImageOps
from keras.models import load_model


@st.cache_resource
def load():
        return load_model('models/vgg16.h5')

model = load()


def predict(img, model):
        return model.predict(img)

st.write("""
# Watermark Detection App
---
>***This app predicts whether an image caontains watermark or not***
---
""")

st.sidebar.header('''User Input Image''')

uploaded_file = st.sidebar.file_uploader("Upload the file", type=['jpeg', 'png', 'jpg'], accept_multiple_files=True)
if uploaded_file is not None:
        results = []
        empty_slots = []
        for i in range(len(uploaded_file)):
                image = Image.open(uploaded_file[i])
                st.image(image, use_column_width=True)
                empty_slots.append(st.empty())
                #image sizing
                size = (224, 224)
                image = ImageOps.fit(image, size)
                img_arr = np.asarray(image)
                normalized_img_arr = (img_arr.astype(np.float32) / 255.0)
                normalized_img_arr = normalized_img_arr[:, :, ::-1]
                np_img = np.expand_dims(normalized_img_arr, 0)
                pred_prob = predict(np_img, model)
                pred="**Watermark**" if pred_prob>0.5 else "**No-watermark**"
                results.append(pred)
                st.write(f"probability", str(pred_prob))
        option = st.button(label=':red[Predict]:exclamation:')
        if option:
                with st.spinner("Wait for it..."):
                        for i in range(len(empty_slots)):
                                empty_slots[i].success(results[i])
                       
else:
        st.info("Please upload image using the sidebar")
