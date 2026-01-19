import streamlit as st

def uploader():
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv') or uploaded_file.name.endswith('.xlsx'):
            st.write("File details:")
            st.write(f"Filename: {uploaded_file.name}")
            st.write(f"File type: {uploaded_file.type}")
            st.write(f"File size: {uploaded_file.size} bytes")
            st.success("File uploaded successfully!")
        else:
            st.error("Unsupported file type. Please upload a CSV or Excel file.")
    else:
        st.info("Please upload a CSV or Excel file to proceed.")
        
def main_ui():
    st.title("AUTO EDA")
    st.write("This application is to do EDA analysis faster and easier.")
    
    uploader()
    
    


if __name__ == "__main__":
    main_ui()


