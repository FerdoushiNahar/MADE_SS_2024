import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from io import StringIO
import sqlite3

from pipeline import load_and_process_data, main

class TestPipeline(unittest.TestCase):
    def setUp(self):
        # Sample CSV data mimicking real CSV files
        self.csv_data_temp = """Date;t
2023-06-01T12:00:00Z;23.5
2023-06-02T12:00:00Z;24.5
2023-06-03T12:00:00Z;20.1
"""
        self.csv_data_co2 = """Date;eco2
2023-06-01T12:00:00Z;400
2023-06-02T12:00:00Z;450
2023-06-03T12:00:00Z;420
"""
        self.df_temp = pd.read_csv(StringIO(self.csv_data_temp), delimiter=';')
        self.df_co2 = pd.read_csv(StringIO(self.csv_data_co2), delimiter=';')

    @patch('pandas.read_csv')
    def test_load_and_process_data(self, mock_read_csv):
        # Mocking pandas.read_csv to return predefined DataFrames based on input
        def side_effect(url, delimiter):
            if "Temperaturwerte_Rathaus_0.csv" in url:
                return self.df_temp
            elif "CO2_Werte_Rathaus_1.csv" in url:
                return self.df_co2
        mock_read_csv.side_effect = side_effect

        # Testing data loading and processing function
        df_temp = load_and_process_data("https://offenedaten-konstanz.de/sites/default/files/Temperaturwerte_Rathaus_0.csv", delimiter=';', date_col='Date', value_col='t')
        df_co2 = load_and_process_data("https://offenedaten-konstanz.de/sites/default/files/CO2_Werte_Rathaus_1.csv", delimiter=';', date_col='Date', value_col='eco2')
        self.assertFalse(df_temp.empty)
        self.assertFalse(df_co2.empty)
        self.assertIn('Time', df_temp.columns)
        self.assertIn('Time', df_co2.columns)

    @patch('sqlite3.connect')
    def test_database_interaction(self, mock_connect):
        # Mocking sqlite3 connection to use an in-memory database
        mock_connect.return_value = sqlite3.connect(':memory:')
        
        # Running the main function which should use the mocked database
        main()
        
        # Assuming main function also prints the outputs, we don't assert here
        # Instead, we just ensure the database interaction doesn't raise an exception

if __name__ == '__main__':
    unittest.main()
