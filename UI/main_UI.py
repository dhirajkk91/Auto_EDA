"""
Main UI Module
Handles the Streamlit user interface for the AUTO EDA application
"""
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Backend.eda_service import EDAService


class AutoEDAUI:
    """Main UI class for AUTO EDA application"""
    
    def __init__(self):
        self.eda_service = EDAService()
        self._initialize_session_state()
    
    def _initialize_session_state(self):
        """Initialize session state variables"""
        if 'file_processed' not in st.session_state:
            st.session_state.file_processed = False
        if 'processing_result' not in st.session_state:
            st.session_state.processing_result = {}
    
    def render_header(self):
        """Render the application header"""
        st.title("AUTO EDA")
        st.write("This application performs EDA analysis faster and easier.")
        st.markdown("---")
    
    def render_file_uploader(self):
        """Render the file upload section"""
        st.subheader("📁 File Upload")
        uploaded_file = st.file_uploader(
            "Choose a CSV or Excel file",
            type=['csv', 'xlsx', 'xls'],
            help="Upload a CSV or Excel file to analyze"
        )
        
        if uploaded_file is not None:
            # Process the file
            with st.spinner("Processing file..."):
                result = self.eda_service.process_uploaded_file(uploaded_file)
                st.session_state.processing_result = result
                st.session_state.file_processed = True
            
            if result['success']:
                st.success("✅ File uploaded and processed successfully!")
                self._display_file_info(result['file_info'])
                self._display_column_names(result['column_names'])
                self._display_basic_stats(result['basic_stats'])
            else:
                st.error(f"❌ Error: {result['error']}")
                st.session_state.file_processed = False
        else:
            st.info("Please upload a CSV or Excel file to proceed.")
            st.session_state.file_processed = False
    
    def _display_file_info(self, file_info):
        """Display file information"""
        if not file_info:
            return
        
        st.subheader("📊 File Information")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Filename", file_info.get('filename', 'N/A'))
        with col2:
            st.metric("File Type", file_info.get('extension', 'N/A'))
        with col3:
            file_size_mb = file_info.get('file_size', 0) / (1024 * 1024)
            st.metric("File Size", f"{file_size_mb:.2f} MB")
    
    def _display_column_names(self, column_names):
        """Display column names"""
        if not column_names:
            return
        
        st.subheader("📋 Column Names")
        st.write(f"**Total Columns:** {len(column_names)}")
        
        # Display columns in a nice format
        cols_per_row = 3
        for i in range(0, len(column_names), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col_name in enumerate(column_names[i:i+cols_per_row]):
                with cols[j]:
                    st.write(f"• {col_name}")
    
    def _display_basic_stats(self, basic_stats):
        """Display basic statistics"""
        if not basic_stats:
            return
        
        st.subheader("📈 Basic Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Rows", basic_stats.get('total_rows', 0))
        with col2:
            st.metric("Total Columns", basic_stats.get('total_columns', 0))
        with col3:
            memory_mb = basic_stats.get('memory_usage', 0) / (1024 * 1024)
            st.metric("Memory Usage", f"{memory_mb:.2f} MB")
        with col4:
            has_missing = "Yes" if basic_stats.get('has_missing_values', False) else "No"
            st.metric("Missing Values", has_missing)
    
    def render_detailed_analysis(self):
        """Render detailed analysis section"""
        if not st.session_state.file_processed or not st.session_state.processing_result.get('success'):
            return
        
        st.markdown("---")
        st.subheader("🔍 Detailed Analysis")
        
        # Column information
        if st.button("Show Detailed Column Information"):
            column_info = self.eda_service.get_column_information()
            if column_info is not None:
                st.dataframe(column_info, use_container_width=True)
        
        # Data types summary
        data_types = self.eda_service.get_data_types_summary()
        if data_types:
            st.write("**Data Types Summary:**")
            for dtype, count in data_types.items():
                st.write(f"• {dtype}: {count} columns")
    
    def run(self):
        """Main method to run the UI"""
        self.render_header()
        self.render_file_uploader()
        self.render_detailed_analysis()


def main():
    """Main function to run the application"""
    st.set_page_config(
        page_title="AUTO EDA",
        page_icon="📊",
        layout="wide"
    )
    
    app = AutoEDAUI()
    app.run()


if __name__ == "__main__":
    main()


