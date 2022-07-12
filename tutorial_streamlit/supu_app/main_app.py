import streamlit as st
from PIL import Image
import os

st.title('サプーアプリ')
st.caption("これはサプーの動画用のテストアプリです")

image = Image.open('./data/test_image.png')
st.image(image, width = 200)

