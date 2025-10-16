import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import math

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

if menu=="📊CSV Uploader":
    st.title("CSV Uploader & Interactive Table")
    uploaded = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    if uploaded is not None:
        if uploaded.name.endswith(".csv"):
            try:
                df = pd.read_csv(uploaded, sep=None, engine="python")
            except Exception:
                df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)

        st.success("✅ File loaded successfully!")
        st.title("Data Table")
        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        st.caption("Sort by column")
        sort_col = st.selectbox("", options=["— No Sort —"] + numeric_cols, index=0)
        if sort_col != "— No Sort —":
            df = df.sort_values(by=sort_col, ascending=True, kind="mergesort")

        PAGE_SIZE = 20
        total_rows = len(df)
        total_pages = max(1, math.ceil(total_rows / PAGE_SIZE))

        st.caption("Select page")
        page = st.slider("", min_value=1, max_value=total_pages, value=1, step=1)

        start = (page - 1) * PAGE_SIZE
        end = min(start + PAGE_SIZE, total_rows)
        page_df = df.iloc[start:end]

        st.dataframe(page_df, use_container_width=True, hide_index=True)

    else:
        st.info("⬅️ Please upload a CSV or Excel file to start.")