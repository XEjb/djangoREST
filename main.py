import requests

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')