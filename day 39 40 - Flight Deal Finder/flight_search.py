from pprint import pprint

from flight_data import FlightData

KIWI_FLIGHT_API_KEY = "KIWI_FLIGHT_API_KEY"
KIWI_BASE_URL = "https://tequila-api.kiwi.com"
import requests
from datetime import datetime, timedelta


class FlightSearch:

    def get_code(self, city_name):
        headers = {"apikey": KIWI_FLIGHT_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=f"{KIWI_BASE_URL}/locations/query", params=query, headers=headers)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def search_flight(self, destination_code):
        tomorrow = datetime.now() + timedelta(1)
        six_months = datetime.now() + timedelta(180)
        formated_tomorrow = tomorrow.strftime("%d/%m/%Y")
        formated_six_months = six_months.strftime("%d/%m/%Y")

        headers = {"apikey": KIWI_FLIGHT_API_KEY}
        query = {
            "fly_from": "LON",
            "fly_to": destination_code,
            "date_from": formated_tomorrow,
            "date_to": formated_six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"}

        response = requests.get(url=f"{KIWI_BASE_URL}/v2/search", params=query, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
            #print(f"{destination_code}: £{data['price']}")
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{KIWI_BASE_URL}/v2/search", params=query, headers=headers)
            response.raise_for_status()
            try:
                data = response.json()["data"][0]
            except IndexError:
                flight_data = None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
        return flight_data
