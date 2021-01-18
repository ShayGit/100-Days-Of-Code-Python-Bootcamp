SHEETY_TOKEN ="SHEETY_TOKEN"
SHEETY_URL="SHEETY_URL"
SHEET_USERS_ENDPOINT = "SHEET_USERS_ENDPOINT"
import requests

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_date(self):
        headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        response = requests.get(url=SHEETY_URL, headers=headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_data(self):
        headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        for destination in self.destination_data:
            price = {
                "price": {
                    "iataCode": destination["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_URL}/{destination['id']}",json=price, headers=headers)
            response.raise_for_status()

    def get_customer_emails(self):
        headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data