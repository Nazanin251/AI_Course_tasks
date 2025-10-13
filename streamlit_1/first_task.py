import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

menu=st.sidebar.radio(
    "Choose an Option",
    ["📝Form","📊CSV Uploader","🖼Image Gallery"]
)
if menu=="📝Form":
    st.title("User Information Form")
    name = st.text_input("Enter your name:")
    age = st.text_input("Enter your age:")
    feedback = st.text_area("Your feedback",height=100)
    agree = st.checkbox("I accept the terms of conditions")
    gender=st.radio(
        "Gender",
        ["Male","Female","Other"]
    )
    rating = st.slider("How many days do you work per week?", 1, 7, 1)

    if st.button("Submit"):
        st.success(f"Thank you for submitting {name}")
        st.write("Age:", age)
        st.write("Feedback:", feedback)
        st.write("Gender:", gender)
        st.write("Day active per week:", rating)
        st.write("You have accepted the terms and conditions.")

if menu=="🖼Image Gallery":
    uploaded_files = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"],accept_multiple_files=True)
    if uploaded_files:
        st.title("Gallery")
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)

            st.image(
                image,
                caption=uploaded_file.name,
                use_container_width=True , width=10
            )
