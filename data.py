import requests
import json


BUBBLE_API_URL = "https://app.planmyfirm.com/version-test/api/1.1/obj"
TABLE_NAME = "visapackage"
HEADERS = {
    "Authorization":"Bearer fd6c8e722db483d0e835146491fe3a29",
    "Content-Type": "application/json"
}

def fetch_bubble_data():
    url = f"{BUBBLE_API_URL}/{TABLE_NAME}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  
        data = response.json()
        print(json.dumps(data,indent=1 ))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error: Response is not valid JSON")

if __name__ == "__main__":
    fetch_bubble_data()
