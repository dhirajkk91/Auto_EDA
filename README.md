# Auto EDA Project

An automated Exploratory Data Analysis (EDA) application built with Streamlit that follows Object-Oriented Programming and Design (OOPD) principles.

## Features

- **File Upload**: Support for CSV and Excel files (.csv, .xlsx, .xls)
- **Column Analysis**: Displays column names, data types, and basic statistics
- **Data Overview**: Shows file information, memory usage, and missing value indicators
- **Detailed Analysis**: Provides comprehensive column information and data type summaries

## Architecture

The project follows OOPD principles with clear separation of concerns:

### Backend Structure
- **`FileHandler`** (`Backend/file_handler.py`): Handles file operations and validation
- **`DataAnalyzer`** (`Backend/data_analyzer.py`): Performs data analysis operations
- **`EDAService`** (`Backend/eda_service.py`): Main service orchestrating file handling and analysis

### UI Structure
- **`AutoEDAUI`** (`UI/main_UI.py`): Handles all Streamlit UI components and user interactions

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run UI/main_UI.py
```

## Project Goals

### First Goal (Completed)
1. ✅ Make a Streamlit website that takes a .csv or excel file
2. ✅ Take that file and give out the column names and their data types
3. ✅ Implement OOPD principles with proper separation of concerns
4. ✅ Each feature has its own class and dedicated functions

## File Structure

```
├── Backend/
│   ├── __init__.py
│   ├── file_handler.py      # File operations
│   ├── data_analyzer.py     # Data analysis
│   └── eda_service.py       # Main service
├── UI/
│   └── main_UI.py          # Streamlit interface
├── requirements.txt
└── README.md
```
