import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# to load the data in cache and not need to download from sklearn
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data)
    df['species'] = iris.target
    return df, iris.target_names

df, target_name = load_data()
