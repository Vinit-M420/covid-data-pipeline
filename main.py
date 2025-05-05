import json
import requests


response = requests.get("https://disease.sh/v3/covid-19/countries/india")
data = response.json()
print(f"Total Cases of Covid-19 in India is {data['cases']}")

print(f"Total Death of Covid-19 in India is {data['deaths']}")

print(data['deathsPerOneMillion'])