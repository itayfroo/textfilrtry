import streamlit as st
import os

# Function to read and write data to a file
def update_data_file(new_data):
    data_file_path = "data.txt"

    # Write new data to the file
    with open(data_file_path, "w") as file:
        file.write(new_data)

    # Read the data from the file
    with open(data_file_path, "r") as file:
        data = file.read()

    return data

# Display the text input field
inputfield = st.text_input("Text")

# Update the data file when the button is pressed
if st.button("Launch"):
    updated_data = update_data_file(inputfield)
    st.success(updated_data)
