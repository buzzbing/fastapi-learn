# GET: Used to request data from a specified resource. 
# It's used for retrieving data and should have no side effects on the server.
# POST: Used to submit data to be processed to a specified resource.
#  It's used for creating or updating a resource on the server, and it may have side effects (such as updating a database).
import requests

# url = 'http://127.0.0.1:8000/'
# response = requests.get(url)
# print(response.content)

# Define the JSON data representing the item
item_data = {
    "name": "Example Item",
    "description": "This is an example item",
    "price": 19.99,
    "tax": 1.50
}

# Make a POST request to the endpoint
response = requests.post("http://localhost:8000/items/", json=item_data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Item created successfully!")
    print("Response:", response.json())
else:
    print("Error:", response.text)