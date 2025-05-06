import json
import requests
import logging

logging.basicConfig(level=logging.INFO)

url = "https://disease.sh/v3/covid-19/countries"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()
    
    #print(f"Total Cases of Covid-19 in India is {data['cases']}")
    #print(f"Total Death of Covid-19 in India is {data['deaths']}")
    

    
    # Save JSON response to a file inside the data folder
    with open("data/global_covid_data.json", "w") as f:
        json.dump(data, f, indent=4)

    logging.info("JSON data saved successfully.")

except requests.exceptions.HTTPError as http_err:
    logging.error(f" HTTP error occurred: {http_err}")
except Exception as err:
    logging.error(f" An error occurred: {err}")