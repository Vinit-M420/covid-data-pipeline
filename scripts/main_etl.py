import json
import requests
import logging

from scripts.extract_owid import fetch_owid_data
from scripts.transform_api import get_country_stats
from scripts.transform_owid import top_5_totalcases
from scripts.load import display_stats, display_top5_cases

logging.basicConfig(level=logging.INFO)

url = "https://disease.sh/v3/covid-19/countries"

try:
    # Extract
    print("Fetching data...")
    response = requests.get(url,timeout=10)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    api_data = response.json()
    
    owid_data = fetch_owid_data()
    
    # Save JSON response to a file inside the data folder    
    with open("data/global_covid_data.json", "w") as f:
        json.dump(api_data, f, indent=4)

    logging.info("JSON data saved successfully.")
    
    print("\nTransforming and loading API data...")
    # Transform + Load API
    india_stats = get_country_stats("data/global_covid_data.json", country_name="India")
    display_stats(india_stats)
    
    print("\nTransforming and loading OWID data...")
    # Transform + Load OWID 
    top5_df = top_5_totalcases()
    display_top5_cases(top5_df)

except requests.exceptions.HTTPError as http_err:
    logging.error(f" HTTP error occurred: {http_err}")
except Exception as err:
    logging.error(f" An error occurred: {err}")