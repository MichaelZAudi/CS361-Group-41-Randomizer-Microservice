import requests

url_num = 'https://cs361-group-41-randomizer-microservice.onrender.com/rand/num'
url_event = 'https://cs361-group-41-randomizer-microservice.onrender.com/rand/event'
url_weighted = 'https://cs361-group-41-randomizer-microservice.onrender.com/rand/weighted'


def test_num(data):
    # send JSON data to server
    response = requests.post(url_num, json = data)

    in_data = response.json()

    if in_data.get('status') == 'success':
        print(f"Your random number is: {in_data.get('return_value')}")


test_num({'type': 'int', 'start': 1, 'end': 15})
test_num({'type': 'float', 'start': 1, 'end': 15})