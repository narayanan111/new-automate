import streamlit as st
import pandas as pd
import os  # Importing os module for file operations

# Function to read data from CSV file
def read_data():
    try:
        return pd.read_csv("student_data.csv")
    except FileNotFoundError:
        st.error("Error: File not found. Please make sure the file 'student_data.csv' exists.")

# Function to save data to CSV file
def save_to_csv(data):
    try:
        data.to_csv("new_student_data.csv", index=False, mode="a", header=not os.path.exists("new_student_data.csv"))
        st.success("Data saved to 'new_student_data.csv' successfully!")
    except Exception as e:
        st.error(f"Error occurred while saving data: {e}")

# Function to display all users' details
def view_users():
    st.title("View Users")
    data = read_data()
    if data is not None:
        st.write(data)
        selected_user_index = st.selectbox("Select a user", data.index)
        selected_user = data.iloc[selected_user_index]
        # Automatically navigate to User Information page and fill details
        st.session_state['selected_user'] = selected_user.to_dict()
        st.session_state['page'] = 'User Information'

# Function for user information form
def user_information():
    st.title("User Information")
    st.write("Please fill in the details:")
    st.markdown("---")

    selected_user = st.session_state.get('selected_user', {})
    if selected_user:
        full_name = st.text_input("Full Name", value=selected_user.get('Full Name', ''))
        roll_number = st.text_input("Roll Number", value=str(selected_user.get('Roll Number', '')))
        gender = st.text_input("Gender", value=selected_user.get('Gender', ''))
        father_name = st.text_input("Father's Full Name", value=selected_user.get("Father's Full Name", ''))
        mother_name = st.text_input("Mother's Full Name", value=selected_user.get("Mother's Full Name", ''))
        department = st.text_input("Department", value=selected_user.get('Department', ''))
        specialization = st.text_input("Specialization", value=selected_user.get('Specialization', ''))
        contact_number = st.text_input("Contact Number", value=selected_user.get('Contact Number', ''))
        aadhar_number = st.text_input("Aadhar Number", value=selected_user.get('Aadhar Number', ''))
        year_of_study = st.text_input("Year of Study", value=str(selected_user.get('Year of Study', '')))
        
        if st.button("Submit"):
            new_data = {
                "Full Name": [full_name],
                "Roll Number": [roll_number],
                "Gender": [gender],
                "Father's Full Name": [father_name],
                "Mother's Full Name": [mother_name],
                "Department": [department],
                "Specialization": [specialization],
                "Contact Number": [contact_number],
                "Aadhar Number": [aadhar_number],
                "Year of Study": [year_of_study]
            }
            new_data_df = pd.DataFrame(new_data)
            save_to_csv(new_data_df)
    else:
        st.warning("Please select a user from the 'View Users' page.")

# Main function to control page navigation
def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'View Users'

    if st.session_state['page'] == 'View Users':
        view_users()
    elif st.session_state['page'] == 'User Information':
        user_information()

if __name__ == "__main__":
    main()
