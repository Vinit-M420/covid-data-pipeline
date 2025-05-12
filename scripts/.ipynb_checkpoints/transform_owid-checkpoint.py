import pandas as pd


def top_5_cases(filepath='data/owid-covid-data.csv'):
    df = pd.read_csv(filepath)
    df = df[df['continent'].notna()]  # ignore world/aggregate data
    latest  = df.loc[df['date'] == df['date'].max()]
    
    print(latest)