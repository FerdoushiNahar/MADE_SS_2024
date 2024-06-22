import os
import pandas as pd
from pipeline import load_and_process_data, main

def test_load_and_process_data():
    # Test CSV URLs (these should be real or mock URLs for testing)
    test_csv_url_1 = "https://offenedaten-konstanz.de/sites/default/files/Temperaturwerte_Rathaus_0.csv"
    test_csv_url_2 = "https://offenedaten-konstanz.de/sites/default/files/CO2_Werte_Rathaus_1.csv"

    # Load and process the data
    df_temp = load_and_process_data(test_csv_url_1, delimiter=';', date_col='Date', value_col='t')
    df_co2 = load_and_process_data(test_csv_url_2, delimiter=';', date_col='Date', value_col='eco2')

    # Check if dataframes are not empty
    assert not df_temp.empty, "Temperature DataFrame is empty"
    assert not df_co2.empty, "CO2 DataFrame is empty"

    # Check if expected columns exist
    assert 'Date' in df_temp.columns, "Date column is missing in Temperature DataFrame"
    assert 't' in df_temp.columns, "Temperature column is missing in Temperature DataFrame"
    assert 'Date' in df_co2.columns, "Date column is missing in CO2 DataFrame"
    assert 'eco2' in df_co2.columns, "CO2 column is missing in CO2 DataFrame"

    print("load_and_process_data() passed all tests.")

def test_main():
    # Run the main function
    main()

    # Check if the SQLite database file was created
    assert os.path.exists('merged_dataset.db'), "SQLite database file was not created"

    # Check if the merged CSV file was created
    assert os.path.exists('merged_dataset.csv'), "Merged CSV file was not created"

    # Load the CSV file to check its contents
    df_merged = pd.read_csv('merged_dataset.csv')

    # Check if the merged DataFrame is not empty
    assert not df_merged.empty, "Merged DataFrame is empty"

    print("main() passed all tests.")

if __name__ == "__main__":
    test_load_and_process_data()
    test_main()
    print("All tests passed.")
