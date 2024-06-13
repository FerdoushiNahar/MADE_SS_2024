import unittest
import pandas as pd
from io import StringIO
import sqlite3
from unittest.mock import patch

# Assuming the module's functions are imported correctly
from pipeline import load_and_process_data, main

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
    
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

    def test_load_and_process_data(self):
        with patch('pandas.read_csv', side_effect=[self.df_temp, self.df_co2]):
            processed_data = load_and_process_data(StringIO(self.csv_data_temp), delimiter=';', date_col='Date', value_col='t')
            self.assertTrue(len(processed_data) > 0)
            self.assertFalse(processed_data['t'].isnull().any())

    def test_database_integration(self):
        with patch('pandas.read_csv', side_effect=[self.df_temp, self.df_co2]):
        
            with sqlite3.connect(':memory:') as conn:
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE merged_data (Date TEXT, Time TEXT, t FLOAT, eco2 INTEGER)")
                conn.commit()

            
                with patch('sqlite3.connect', return_value=conn):
                    main()
                    cursor.execute("SELECT * FROM merged_data")
                    result = cursor.fetchall()
                    self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
