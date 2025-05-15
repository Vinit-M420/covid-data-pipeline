from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


cols = ['location', 'continent', 'date', 'total_cases', 'total_deaths']

## Transform top5 countries wit total deaths 
def top_5_totaldeaths(filepath='/opt/airflow/data/owid-covid-data.csv'):
    df = pd.read_csv(filepath, usecols= cols)
    df = df[df['continent'].notna()]  # ignore world/aggregate data
    df['date'] = pd.to_datetime(df['date'])
    latest  = df.sort_values('date').groupby('location').tail(1)
    
    top5 = latest.sort_values('total_deaths', ascending=False).head(5)
    top5.to_csv('/opt/airflow/output/top5_total_deaths.csv', index=False)
    print(top5)
    #return top5[['location', 'total_deaths']]


default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG (dag_id='covid_data_pipeline',
          schedule_interval = '@daily',
          default_args = default_args,
          catchup= False) as dag:
    
    transform = PythonOperator(
        task_id='transform_top5_countries',
        python_callable= top_5_totaldeaths
    )
    
