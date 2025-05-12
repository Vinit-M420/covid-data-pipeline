import pandas as pd

cols = ['location', 'continent', 'date', 'total_cases', 'total_deaths']

def top_5_totalcases(filepath='data/owid-covid-data.csv'):
    df = pd.read_csv(filepath, usecols= cols)
    df = df[df['continent'].notna()]  # ignore world/aggregate data
    latest  = df.sort_values('date').groupby('location').tail(1)
    
    top5 = latest.sort_values('total_cases', ascending=False).head(5)
    return top5[['location', 'total_cases']]
