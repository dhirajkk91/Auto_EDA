import pandas as pd

def load_data(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        else:
            data = None
        return data
    return None

def columns_info(data):
    if data is not None:
        column_info = pd.DataFrame({
            'Column Name': data.columns,
            'Data Type': data.dtypes,
            'Non-Null Count': data.notnull().sum(),
            'Unique Values': data.nunique()
        })
        return column_info
    return None