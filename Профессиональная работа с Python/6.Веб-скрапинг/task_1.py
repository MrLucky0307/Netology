import time
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json


def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()


def get_links(text):
    response = requests.get(
        url=f'https://hh.ru/search/vacancy?text={text}&area=1&area=2&page=1', headers=get_headers()
    )
    if response.status_code != 200:
        return
    soup = BeautifulSoup(response.content, "lxml")
    page_count = int(
        soup.find('div', attrs={"class": "pager"}).find_all('span', recursive=False)[-1].find("a").find("span").text
    )
    for page in range(page_count):
        response = requests.get(
            url=f'https://hh.ru/search/vacancy?text={text}&area=1&area=2&page={page}', headers=get_headers()
        )
        if response.status_code != 200:
            continue
        soup = BeautifulSoup(response.content, "lxml")
        for _ in soup.find_all("a", attrs={"class": "serp-item__title"}):
            yield f"{_.attrs['href'].split('?')[0]}"
    time.sleep(1)


def get_vacancy(link):
    response = requests.get(url=link, headers=get_headers())
    if response.status_code != 200:
        return
    soup = BeautifulSoup(response.content, "lxml")
    salary = soup.find(attrs={"data-qa": "vacancy-salary"}).text.replace("\xa0", "")
    name_company = soup.find(attrs={"data-qa": "vacancy-company-name"}).text.replace("\xa0", "")
    try:
        city = soup.find(attrs={"data-qa": "vacancy-view-location"}).text
    except:
        city = soup.find(attrs={"data-qa": "vacancy-view-raw-address"}).text
    vacancy = {"link": link, "salary": salary, "name_company": name_company, "city": city}
    return vacancy


if __name__ == '__main__':
    data = []
    for a in get_links('python+flask+django'):
        data.append(get_vacancy(a))
        time.sleep(1)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
