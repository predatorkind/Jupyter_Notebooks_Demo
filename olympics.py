import pandas as pd

def clean_data():
    """Cleans the data in the 'Data Sets/olympics.csv' file.

    Returns:
        pandas.DataFrame: A cleaned DataFrame object with renamed columns.
    """
    data = pd.read_csv('Data Sets/olympics.csv', header=1).rename(
        columns={
            "Unnamed: 0": "Country",
            "? Summer": "Summer_Games",
            "01 !": "Summer_Gold",
            "02 !": "Summer_Silver",
            "03 !": "Summer_Bronze",
            "Total": "Summer_Total",
            "? Winter": "Winter_Games",
            "01 !.1": "Winter_Gold",
            "02 !.1": "Winter_Silver",
            "03 !.1": "Winter_Bronze",
            "Total.1": "Winter_Total",
            "? Games": "Games_Total",
            "01 !.2": "Games_Gold",
            "02 !.2": "Games_Silver",
            "03 !.2": "Games_Bronze",
            "Combined total": "Combined_Total",
                 }
    )

    # The last row contains totals for each column hence it needs dropping
    data.drop(data.index[-1], inplace=True)

    return data



