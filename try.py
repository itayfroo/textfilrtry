import streamlit as st
import os
with open("file.txt","w") as w:
    inputfield = st.text_input("Text")
    if st.button("launch"):
        b = w.write(inputfield)
with open("file.txt","r") as r:
    b= r.read()
    st.success(r)