#!/bin/bash

# This script runs the tests for the project

# Downloading large datasets can be problematic in CI environments.
# Uncomment the following lines to run the actual tests if datasets are accessible.

# echo "Running tests with actual datasets"
# python tests.py

# For now, we mock the data or skip the download
echo "Running tests with mock data"

# Create mock data and save as CSVs (optional, adjust as needed)
echo "Date,t" > mock_temp.csv
echo "2023-06-25T12:00:00Z,25.6" >> mock_temp.csv
echo "2023-06-25T13:00:00Z,25.8" >> mock_temp.csv

echo "Date,eco2" > mock_co2.csv
echo "2023-06-25T12:00:00Z,400" >> mock_co2.csv
echo "2023-06-25T13:00:00Z,420" >> mock_co2.csv

# Replace URLs with mock files in tests.py
sed -i 's|https://offenedaten-konstanz.de/sites/default/files/Temperaturwerte_Rathaus_0.csv|mock_temp.csv|g' tests.py
sed -i 's|https://offenedaten-konstanz.de/sites/default/files/CO2_Werte_Rathaus_1.csv|mock_co2.csv|g' tests.py

# Run tests with mock data
python tests.py
