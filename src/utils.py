# src/utils.py

import pandas as pd

def load_dataset(path: str):
    """
    Load dataset from CSV file.

    Parameters
    ----------
    path : str
        Path to CSV file

    Returns
    -------
    pd.DataFrame
    """
    return pd.read_csv(path)
