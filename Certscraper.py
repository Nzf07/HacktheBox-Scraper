import requests
from bs4 import BeautifulSoup

BADGE_URL = "https://academy.hackthebox.com/achievement/badge/"

def getNumber(id):
    page = requests.get(BADGE_URL + id)
    soup = BeautifulSoup(page.text, "html.parser")

    number = soup.find('span', class_='font-size-20 text-white').get_text()
    return number

print(f"CWEE: {getNumber("9b5c7136-e85b-11ee-b18d-bea50ffe6cb4")}")
print(f"CPTS: {getNumber("e98588a1-4cf6-11ee-acfc-bea50ffe6cb4")}")
print(f"CBBH: {getNumber("cc831d18-c408-11ed-acfc-bea50ffe6cb4")}")
print(f"CDSA: {getNumber("8f840175-168f-11ef-b18d-bea50ffe6cb4")}")
