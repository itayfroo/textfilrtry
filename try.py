import streamlit as st
import sqlite3

# Function to create a SQLite database and table
def create_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user_data (text TEXT)")
    conn.commit()
    conn.close()

# Function to update and retrieve data from the database
def update_and_get_data(new_data):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # Update data in the database
    c.execute("INSERT INTO user_data VALUES (?)", (new_data,))
    conn.commit()

    # Retrieve all data from the database
    c.execute("SELECT * FROM user_data")
    data = c.fetchall()

    conn.close()

    return data

# Create the database table
create_table()

# Display the text input field
inputfield = st.text_input("Text")

# Update the database and retrieve data when the button is pressed
if st.button("Launch"):
    updated_data = update_and_get_data(inputfield)

    # Display the full database content
    st.table(updated_data)
