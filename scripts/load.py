
def display_stats(stats):
    print(f"\nCovid Stats for {stats['country']}:")
    print(f"Total Cases: {stats['cases']}")
    print(f"Total Deaths: {stats['deaths']}")
    print(f"Total Recovered: {stats['recovered']}")


def display_top5_cases(df):
    print("\nTop 5 Countries with Highest Total Cases:")
    print(df)