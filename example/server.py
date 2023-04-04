import requests

def get_random_json():
    # The API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()

    return "'" + str(response_json)[35:70] + "'"