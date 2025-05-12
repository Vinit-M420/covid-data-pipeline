import json

def get_country_stats(filepath = "data/global_covid_data.json", country_name='India'):
    with open(filepath, 'r') as f:
        data = json.load(f)

    for entry in data:
        if entry['country'].lower() == country_name.lower():
            return {
                'country': entry['country'],
                'cases': entry['cases'],
                'deaths': entry['deaths'],
                'recovered': entry['recovered']
            }

    raise ValueError(f"{country_name} not found in the data.")
