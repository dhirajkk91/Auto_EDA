import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Backend.initial import load_data, columns_info

def uploader():
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv') or uploaded_file.name.endswith('.xlsx'):
            st.write("File details:")
            st.write(f"Filename: {uploaded_file.name}")
            st.write(f"File type: {uploaded_file.type}")
            st.write(f"File size: {uploaded_file.size} bytes")
            st.success("File uploaded successfully!")
            
            st.session_state['uploaded_file'] = uploaded_file
        else:
            st.error("Unsupported file type. Please upload a CSV or Excel file.")
    else:
        st.info("Please upload a CSV or Excel file to proceed.")
        
def main_ui():
    st.title("AUTO EDA")
    st.write("This application is to do EDA analysis faster and easier.")
    
    uploader()
    
    # Load data if uploaded
    if 'uploaded_file' in st.session_state:
        data = load_data(st.session_state['uploaded_file'])
        column_info = columns_info(data)
        if column_info is not None:
            st.write("Column Information:")
            st.dataframe(column_info)
        else:
            st.warning("Failed to load data.")
    else:
        st.info("Please upload a file to see column information.")


if __name__ == "__main__":
    main_ui()


