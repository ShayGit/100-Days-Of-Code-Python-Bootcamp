import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "USERNAME"
TOKEN = "TOKEN"
GRAPH_ID = "GRAPH_ID"

user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Meditation Graph",
    "unit" : "Minutes",
    "type" : "int",
    "color" : "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


post_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = datetime.now()
today = date.strftime("%Y%m%d")


post_value_config = {
    "date": today,
    "quantity": "30"
}

# response = requests.post(post_value_endpoint,json=post_value_config,headers=headers)
# print(response.text)

date = datetime.now()
today = date.strftime("%Y%m%d")

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"


new_data = {
    "quantity": "60"
}

# response = requests.put(update_endpoint,json=new_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(delete_endpoint,headers=headers)
print(response.text)