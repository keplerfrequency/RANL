import requests
from bs4 import BeautifulSoup
import json


def get_events_fortnite(url):
    response = requests.get(url)

    # Create a BeautifulSoup object from the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all the 'a' tags that have an 'href' attribute
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/party/')]

    return links

def parse_party_link(link):

    extension = link.split(":")

    url = "https://partyflock.nl" + extension[0]
    response = requests.get(url)

    # Create a BeautifulSoup object from the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all the 'a' tags that have an 'href' attribute
    address = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('https://www.google.com/maps/place')]
    party_link = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/jumpto/presence')]
    day = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/agenda/day')]
    #event_info = [div['class'] for div in soup.find_all('div', class=True) if div['ckass'].startswith('party body light8 box')]
    #genres = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/agenda/day')]

    #print("Address is:{}".format(address))
    #print("Party_link is:{}".format(party_link))
    #print("Day is:{}".format(day))
    #print("Genres are:{}".format(genres))

    event={
        "address": address,
        "party_link": "https://partyflock.nl" + party_link[0],
        "day": day
    }

    y= json.dumps(event)

    print(y)
    
    return


def main():
    url = 'https://partyflock.nl/agenda'
    links = get_events_fortnite(url)

    print(links[1])
    parse_party_link(links[1])


if __name__=="__main__":
    main()
