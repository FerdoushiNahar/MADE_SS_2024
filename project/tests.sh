
#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Print commands and their arguments as they are executed.
set -x

# Check if Python 3 is installed
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

# Install required Python packages
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Execute the main pipeline script
echo "Running the main pipeline script..."
python3 pipeline.py

# Execute tests
echo "Running tests..."
python3 -m unittest tests

# If all tests pass
echo "All tests passed successfully."
