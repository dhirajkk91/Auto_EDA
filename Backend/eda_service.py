"""
EDA Service Module
Main service class that orchestrates file handling and data analysis
"""
from typing import Optional, Dict, List
import pandas as pd
from .file_handler import FileHandler
from .data_analyzer import DataAnalyzer


class EDAService:
    """Main service class for EDA operations"""
    
    def __init__(self):
        self.file_handler = FileHandler()
        self.data_analyzer = DataAnalyzer()
        self.current_data = None
        self.file_info = {}
    
    def process_uploaded_file(self, uploaded_file) -> Dict[str, any]:
        """Process uploaded file and return results"""
        try:
            # Validate file
            if not self.file_handler.is_supported_file(uploaded_file.name):
                return {
                    'success': False,
                    'error': 'Unsupported file type. Please upload CSV or Excel files only.',
                    'file_info': {},
                    'column_names': [],
                    'basic_stats': {}
                }
            
            # Get file information
            self.file_info = self.file_handler.get_file_info(uploaded_file)
            
            # Load data
            self.current_data = self.file_handler.load_data(uploaded_file)
            self.data_analyzer.set_data(self.current_data)
            
            # Get column names and basic stats
            column_names = self.data_analyzer.get_column_names()
            basic_stats = self.data_analyzer.get_basic_stats()
            
            return {
                'success': True,
                'error': None,
                'file_info': self.file_info,
                'column_names': column_names,
                'basic_stats': basic_stats
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'file_info': self.file_info,
                'column_names': [],
                'basic_stats': {}
            }
    
    def get_column_information(self) -> Optional[pd.DataFrame]:
        """Get detailed column information"""
        return self.data_analyzer.get_column_info()
    
    def get_data_types_summary(self) -> Dict[str, int]:
        """Get data types summary"""
        return self.data_analyzer.get_data_types_summary()
    
    def has_data(self) -> bool:
        """Check if data is loaded"""
        return self.current_data is not None
    
    def get_current_data(self) -> Optional[pd.DataFrame]:
        """Get current loaded data"""
        return self.current_data