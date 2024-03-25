import requests
from pprint import pprint
url = "http://127.0.0.1:8000/api/rest-auth/registration/"
data = {
    'username': 'rest_test_user_2',
    'email': 'test@test.com',
    'password1': 'test123456789',
    'password2': 'test123456789'
}

response = requests.post(url, data=data)
response_data = response.json()
pprint(response_data)
print("HTTP request failed with status code:", response.status_code)

