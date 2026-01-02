import requests
from bs4 import BeautifulSoup
from hostfile import shakes

"""
Source URI: https://autoinsult.com/
This file fetches insults from the above website's "Shakespearean insult" vertical. 
"""

def screwing_around():
    headers = {}
    payload = {}

    response = requests.get(shakes, headers=headers, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")
    target_div = soup.find("div", class_="insult")
    opus = target_div.contents[0]
    return opus

def main():
    opus = screwing_around()
    print(opus)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass 
    