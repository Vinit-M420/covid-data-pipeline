import pandas as pd
import os

def fetch_owid_data(filepath="data/owid-covid-data.csv"):
    if os.path.exists(filepath):
        print("Using local OWID CSV.")
        return pd.read_csv(filepath)
    else:
        raise FileNotFoundError(f"{filepath} not found. Please download OWID data manually.")