import requests
from pprint import pprint
# {'key': '4ff921435913f03eb28baf99492e7ac66339a17a'}
def client():
    token = 'Token 4ff921435913f03eb28baf99492e7ac66339a17a'
    headers = {
        'Authorization': token,
    }
    credentials = {
        'username': 'test_user',
        'password': 'test123456789'
    }
    response = requests.get(
        url = 'http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers = headers,
    )
    print('Status Code:', response.status_code)
    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()