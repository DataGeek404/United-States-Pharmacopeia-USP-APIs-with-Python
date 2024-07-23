# USP API Integration with Python

This project demonstrates how to interact with the United States Pharmacopeia (USP) APIs using Python. It includes a sample script to make GET requests to a USP API endpoint and process the JSON responses.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Key Setup](#api-key-setup)
- [Sample Code](#sample-code)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/DataGeek404/usp-api-python.git
    cd usp-api-python
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **API Key Setup**:

    Obtain your USP API key by registering on the [USP website](https://www.usp.org/).

2. **Edit the Configuration**:

    Open `config.py` and replace `'your_api_key'` with your actual API key.

    ```python
    API_KEY = 'your_api_key'
    BASE_URL = 'https://api.usp.org/v1/endpoint'  # Replace with the actual endpoint
    ```

3. **Run the Script**:

    ```bash
    python usp_api.py
    ```

## API Key Setup

1. Register on the [USP website](https://www.usp.org/).
2. Request access to the API and obtain your API key.
3. Update the `config.py` file with your API key.

## Sample Code

Here is an example of how to make a GET request to a USP API endpoint:

```python
import requests
import json
from config import API_KEY, BASE_URL

# Define the headers and parameters for the request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

params = {
    'param1': 'value1',
    'param2': 'value2'
}

# Make the GET request to the USP API
response = requests.get(BASE_URL, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(json.dumps(data, indent=4))  # Pretty print the JSON data
else:
    print(f'Error: {response.status_code}, {response.text}')
