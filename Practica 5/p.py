import requests
from bs4 import BeautifulSoup

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def espn():
    soup = get_soup("https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador/_/vista/batting")
    tr= soup.find_all('table') [0] .find_all("tr")
    for row in tr:
        cols = row.find_all('td')
        t = [ele.text.strip() for ele in cols]
        print(f'{t}')

if __name__ == '__main__':
    espn()
    
