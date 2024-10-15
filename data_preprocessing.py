import pandas as pd

def load_data(file_path):
    """Loads the dataset from a CSV file."""
    data = pd.read_csv(file_path, encoding='latin-1')
    return data

def preprocess_data(data):
    """Preprocesses the text data."""
    data = data[['Score', 'Text']]  # Adjust column names based on the dataset
    data['Text'] = data['Text'].str.lower().str.replace('[^\w\s]', '')
    return data
