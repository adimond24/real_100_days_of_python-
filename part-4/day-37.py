import requests
from datetime import datetime

USERNAME = "ameliamaurine"
TOKEN = "ghtjel;wlk34;lk"
GRAPH_ID = "graph1"
WEBSITE_ACCESS = "https://pixe.la/v1/users/ameliamaurine/graphs/graph1.html"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ichou",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(input("How many pages did you read today?")),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers )
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"
}
# response = requests.put(url=update_endpoint,json=new_pixel_data, headers=headers)
# print(response)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response)