import streamlit as st
import pandas as pd
import numpy as np

# Streamlit = end to end app framework that helps create web applications for ML and DataSci projects 

# RUN USING COMMAND - streamlit run filename.py
# Title in Streamlit

st.title("IFrst Streamlist APP")
st.write("This is text")

df = pd.DataFrame({'first': [1, 2, 3, 4], 'second': [5, 6, 7, 8]})
st.write("THIS IS FIRST DATAFRAME: ", df)

df2 = pd.DataFrame(np.random.randn(20, 3), columns= ['A', 'B', 'C'])
st.line_chart(df2)

# Taking input

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello {name}!")

# SLider can only be used for int, float or datetime - begin, end, defualt
age = st.slider("Select your age: ",18 , 50, 25)
st.write(f"Your age is {age}")    

# dropdown menu
options = ["Eng", "Math", "Science"]
choice = st.selectbox("Choose your fav subject", options)
st.write(f"Fav subject is {choice}")

# uploading files and restricting it to CSV file type
upload = st.file_uploader("Choose a file: ", type='csv')
if upload is not None:
    df = pd.read_csv(upload)
    st.write(df)