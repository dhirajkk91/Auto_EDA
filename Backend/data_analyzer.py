"""
Data Analyzer Module
Handles data analysis operations including column information extraction
"""
import pandas as pd
from typing import List, Dict, Optional


class DataAnalyzer:
    """Handles data analysis operations"""
    
    def __init__(self, data: Optional[pd.DataFrame] = None):
        self.data = data
    
    def set_data(self, data: pd.DataFrame) -> None:
        """Set the data for analysis"""
        self.data = data
    
    def get_column_names(self) -> List[str]:
        """Return list of column names"""
        if self.data is None:
            return []
        return self.data.columns.tolist()
    
    def get_column_info(self) -> Optional[pd.DataFrame]:
        """Get detailed column information"""
        if self.data is None:
            return None
        
        column_info = pd.DataFrame({
            'Column Name': self.data.columns,
            'Data Type': self.data.dtypes,
            'Non-Null Count': self.data.notnull().sum(),
            'Unique Values': self.data.nunique()
        })
        return column_info
    
    def get_basic_stats(self) -> Dict[str, any]:
        """Get basic statistics about the dataset"""
        if self.data is None:
            return {}
        
        return {
            'total_rows': len(self.data),
            'total_columns': len(self.data.columns),
            'column_names': self.get_column_names(),
            'memory_usage': self.data.memory_usage(deep=True).sum(),
            'has_missing_values': self.data.isnull().any().any()
        }
    
    def get_data_types_summary(self) -> Dict[str, int]:
        """Get summary of data types"""
        if self.data is None:
            return {}
        
        dtype_counts = self.data.dtypes.value_counts().to_dict()
        return {str(dtype): count for dtype, count in dtype_counts.items()}