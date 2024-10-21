import streamlit as st
import random
from PIL import Image

st.title("おみくじ")

image = Image.open('4.png')

st.image(image,width=100)

def uranau():
    ph = ('1.png', '2.png', '3.png')
    rnd_ph = random.choice(ph)

    image = Image.open(rnd_ph)

    st.image(image,width=100)


if st.button('占う'):
    uranau()



