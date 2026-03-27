
import streamlit as st 

st.title("Hello World")
st.write("This is my first Streamlit app!")

st.button("Click me!")

data = st.text_input("Enter your name")
age = st.radio("Select your age", options=["0-18", "19-35", "36-50", "51+"])
if age == "0-18":
    st.write("You are a child.")
elif age == "19-35":
    st.write("You are a young adult.")
elif age == "36-50":
    st.write("You are an adult.")
else:
    st.write("You are a senior.")
st.write(f"Hello, {data}, you are {age}!")

