from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_date()

if not sheet_data[0]["iataCode"]:
    pprint(sheet_data)
    for city in sheet_data:
        city["iataCode"] = flight_search.get_code(city["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

users = data_manager.get_customer_emails()
emails = [row["email"] for row in users]
names = [row["firstName"] for row in users]

for city in sheet_data:
    flight = flight_search.search_flight(city["iataCode"])

    if flight is None:
        continue

    if flight.price < city["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        print(message)


        if flight.stop_overs > 0:
            message +=f"Flight has {flight.stop_overs} stop over, via {flight.via_city}"
            print(message)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        # notification_manager.send_sms(message)
        notification_manager.send_emails(emails, message, link)
