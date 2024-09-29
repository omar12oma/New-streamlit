import streamlit as st
import joblib

st.title("Hello, World!")


st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a regular text.")

model = joblib.load('lin.pkl')

X = st.slider('E',0,40)
y = model.predict([[X]])

st.write('salary is ',y)