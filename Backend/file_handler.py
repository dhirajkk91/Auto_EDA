"""
File Handler Module
Handles file upload and validation operations
"""
import pandas as pd
from typing import Optional, List, Tuple


class FileHandler:
    """Handles file operations for CSV and Excel files"""
    
    SUPPORTED_EXTENSIONS = ['.csv', '.xlsx', '.xls']
    
    def __init__(self):
        self.supported_types = {
            '.csv': self._read_csv,
            '.xlsx': self._read_excel,
            '.xls': self._read_excel
        }
    
    def is_supported_file(self, filename: str) -> bool:
        """Check if the file extension is supported"""
        return any(filename.lower().endswith(ext) for ext in self.SUPPORTED_EXTENSIONS)
    
    def get_file_info(self, uploaded_file) -> dict:
        """Extract basic file information"""
        if uploaded_file is None:
            return {}
        
        return {
            'filename': uploaded_file.name,
            'file_type': uploaded_file.type,
            'file_size': uploaded_file.size,
            'extension': self._get_file_extension(uploaded_file.name)
        }
    
    def load_data(self, uploaded_file) -> Optional[pd.DataFrame]:
        """Load data from uploaded file"""
        if uploaded_file is None:
            return None
        
        file_extension = self._get_file_extension(uploaded_file.name)
        
        if file_extension not in self.supported_types:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
        try:
            return self.supported_types[file_extension](uploaded_file)
        except ImportError as e:
            if 'openpyxl' in str(e):
                raise Exception("Missing dependency: openpyxl is required for Excel files. Please install it with: pip install openpyxl")
            elif 'xlrd' in str(e):
                raise Exception("Missing dependency: xlrd is required for older Excel files. Please install it with: pip install xlrd")
            else:
                raise Exception(f"Missing dependency: {str(e)}")
        except Exception as e:
            raise Exception(f"Error loading file: {str(e)}")
    
    def _get_file_extension(self, filename: str) -> str:
        """Get file extension from filename"""
        return '.' + filename.split('.')[-1].lower()
    
    def _read_csv(self, uploaded_file) -> pd.DataFrame:
        """Read CSV file"""
        return pd.read_csv(uploaded_file)
    
    def _read_excel(self, uploaded_file) -> pd.DataFrame:
        """Read Excel file"""
        return pd.read_excel(uploaded_file)