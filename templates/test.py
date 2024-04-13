import requests

# Kintone API details
BASE_URL = "https://heros.kintone.com/k/v1/records.json"  # Ensure this is correct
APP_ID = "4"  # The application ID
API_TOKEN = "MdfoNfYe3KAEiHy0FaRvS6o6THPuR8DoWasEp1sF"

def get_kintone_records():
    headers = {
        "X-Cybozu-API-Token": API_TOKEN,
        "Content-Type": "application/json"
    }
    
    # Query parameters
    params = {
        "app": APP_ID,
        "query": ""  # You can modify this later to filter or sort records
    }
    
    # Make the API request
    response = requests.get(BASE_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve records: {response.status_code}")
        print(response.json())  # This will print the error message in JSON format

# Fetch and print the records
records = get_kintone_records()
print(records)
