import requests
from pprint import pprint
# {'key': '4ff921435913f03eb28baf99492e7ac66339a17a'}
def client():
    credentials = {
        'username': 'test_user',
        'password': 'test123456789'
    }
    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        data = credentials,
    )
    print('Status Code:', response.status_code)
    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()