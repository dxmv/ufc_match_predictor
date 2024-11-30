from data_manager import update_upcoming_matches
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.ufc.com/"

def fetch_events_page():
    """
    Fetches the content of the UFC events page.
    
    Returns:
        bytes: The content of the events page if the request is successful, otherwise None.
    """
    response = requests.get(BASE_URL + "events")
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    return response.content

def get_first_event_link(soup):
    """
    Extracts the link to the first event from the events page soup.
    
    Args:
        soup (BeautifulSoup): The parsed HTML of the events page.
    
    Returns:
        str: The URL of the first event if found, otherwise None.
    """
    first_event = soup.find('h3', class_='c-card-event--result__headline')
    if first_event and first_event.find('a'):
        return first_event.find('a').get('href')
    print("No event link found.")
    return None

def fetch_event_page(event_link):
    """
    Fetches the content of a specific event page.
    
    Args:
        event_link (str): The URL of the event page.
    
    Returns:
        bytes: The content of the event page if the request is successful, otherwise None.
    """
    event_response = requests.get(BASE_URL + event_link)
    if event_response.status_code != 200:
        print(f"Failed to retrieve event page. Status code: {event_response.status_code}")
        return None
    return event_response.content

def scrape_matches(event_soup):
    """
    Scrapes and prints the match details from the event page soup.
    
    Args:
        event_soup (BeautifulSoup): The parsed HTML of the event page.
    """
    matches = event_soup.find_all('div', class_='c-listing-fight__content')
    for match in matches:
        # get the fighter names
        red_fighter = match.find('div', class_='c-listing-fight__corner-name--red')
        blue_fighter = match.find('div', class_='c-listing-fight__corner-name--blue')
        [red_name, blue_name] = [fighter.text.strip().replace('\n', ' ') for fighter in [red_fighter, blue_fighter]]
        # get the odds
        [red_odds, blue_odds] = match.find_all('span', class_='c-listing-fight__odds')

        # get the links to the fighters' profiles
        red_link = red_fighter.find('a').get('href')
        blue_link = blue_fighter.find('a').get('href')
        # scrape both fighters' profiles
        red_profile = scrape_fighter_profile(red_link)
        blue_profile = scrape_fighter_profile(blue_link)
        # add all of this to the csv

def scrape_fighter_profile(fighter_link: str):
    """
    Scrapes the fighter's profile page.
    """
    def inches_to_cms(inches):
        """
        Converts inches to centimeters.
        
        Args:
            inches (float): The length in inches.
        
        Returns:
            float: The length in centimeters.
        """
        return inches * 2.54
        
    # fetch the fighter's profile page
    response = requests.get(fighter_link)
    if response.status_code != 200:
        print(f"Failed to retrieve fighter profile. Status code: {response.status_code}")
        return None
    soup = BeautifulSoup(response.content, 'html.parser')

    # get the age
    age = soup.find('div', class_='field--name-age').text.strip()
    # get the win/loss/draw
    [wins, draws, losses] = soup.find('p', class_='hero-profile__division-body').text.strip().split(' ')[0].split('-')
    # get the height

    # get the reach
    reach = soup.find('div', class_='field--name-reach').text.strip()

def scrape_upcoming_matches():
    """
    Orchestrates the scraping of upcoming matches by fetching the events page,
    extracting the first event link, and scraping match details from the event page.
    """
    events_page_content = fetch_events_page()
    if events_page_content is None:
        return

    soup = BeautifulSoup(events_page_content, 'html.parser')
    first_event_link = get_first_event_link(soup)
    if not first_event_link:
        return

    print("First event link found:", first_event_link)
    
    event_page_content = fetch_event_page(first_event_link)
    if event_page_content is None:
        return

    event_soup = BeautifulSoup(event_page_content, 'html.parser')
    scrape_matches(event_soup)

if __name__ == "__main__":
    scrape_upcoming_matches()