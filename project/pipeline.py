import pandas as pd
import re
import sqlite3

def load_and_process_data(csv_url, delimiter=';', date_col='Date', value_col='t'):
  
    # Reading the CSV file into a DataFrame
    df = pd.read_csv(csv_url, delimiter=delimiter)
    
    # Function to check if a value has multiple dot-separated groups of digits
    def is_invalid_format(value):
        if re.match(r'^-?\d+(\.\d{1,3})$', value):
            return False
        return True
    
    # Applying the function to filter out invalid rows
    df = df[~df[value_col].apply(is_invalid_format)]
    
    # Separating the 'Date' column into 'Date' and 'Time' columns
    df[[date_col, 'Time']] = df[date_col].str.split('T', expand=True)
    
    # Removing the 'Z' at the end of the 'Time' column
    df['Time'] = df['Time'].str.replace('Z', '')
    
    return df

def main():
    # URLs to the CSV files
    csv_url_1 = "https://offenedaten-konstanz.de/sites/default/files/Temperaturwerte_Rathaus_0.csv"
    csv_url_2 = "https://offenedaten-konstanz.de/sites/default/files/CO2_Werte_Rathaus_1.csv"
    
    # Loading and processing the datasets
    df_temp = load_and_process_data(csv_url_1, delimiter=';', date_col='Date', value_col='t')
    df_co2 = load_and_process_data(csv_url_2, delimiter=';', date_col='Date', value_col='eco2')
    
    # Merging the two DataFrames on the 'Date' column
    merged_df = pd.merge(df_temp, df_co2, on='Date', suffixes=('_temp', '_co2'))
    
    # Printing the first few rows of the merged DataFrame to confirm
    print("Merged DataFrame:")
    print(merged_df.head())
    
    # Creating an SQLite database connection
    conn = sqlite3.connect('merged_dataset.db')
    cursor = conn.cursor()
    
    # Storing the merged DataFrame in the SQLite database
    merged_df.to_sql('merged_data', conn, if_exists='replace', index=False)
    
    # Committing and closing the connection
    conn.commit()
    
    # Query all rows from the merged data table
    query = "SELECT * FROM merged_data LIMIT 5"
    queried_df = pd.read_sql_query(query, conn)
    
    # Displaying the first few rows of the queried DataFrame to confirm
    print("Queried DataFrame from SQLite:")
    print(queried_df)
    
    # Closing the connection
    conn.close()
    
    # Saving the merged DataFrame to a CSV file
    output_csv = 'merged_dataset.csv'
    merged_df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"Merged dataset saved as {output_csv}")

if __name__ == "__main__":
    main()
