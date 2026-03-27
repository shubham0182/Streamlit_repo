import streamlit as st 

st.title("Data Science Portfolio")
col1,col2,col3 =st.columns([1,1,1])
col1.header("Project 1")
col2.header("Project 2")
col3.header("Project 3")

st.sidebar.header("About Me")
st.sidebar.button('Introduction',icon_position='right')
st.sidebar.button('Contact',icon_position='right')
st.sidebar.button('Resume',icon_position='right')

st.image("image.png",width=200, caption="Data Science")