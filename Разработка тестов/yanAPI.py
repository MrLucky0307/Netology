import requests

token_YandexDisk = '*****'
url = "https://cloud-api.yandex.net/v1/disk/resources"


def create_folder(folder_name):
    params = {'path': {folder_name}}
    headers = {"Authorization": f"OAuth {token_YandexDisk}"}
    res = requests.put(url, params=params, headers=headers)
    return res.status_code


def delete_folder(folder_name):
    params = {'path': {folder_name}}
    headers = {"Authorization": f"OAuth {token_YandexDisk}"}
    res = requests.delete(url, params=params, headers=headers)
    return res.status_code
