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
    match_data_list = []  # Initialize an empty list to store match data

    for match in matches:
        # get the fighter names
        red_fighter = match.find('div', class_='c-listing-fight__corner-name--red')
        blue_fighter = match.find('div', class_='c-listing-fight__corner-name--blue')
        [red_name, blue_name] = [fighter.text.strip().replace('\n', ' ') for fighter in [red_fighter, blue_fighter]]
        print(f"Adding match: {red_name} vs {blue_name}...")
        
        # get the odds
        [red_odds, blue_odds] = match.find_all('span', class_='c-listing-fight__odds-amount')
        red_odds = int(red_odds.text.strip().replace('+', ''))
        blue_odds = int(blue_odds.text.strip().replace('+', ''))

        # get the links to the fighters' profiles
        red_link = red_fighter.find('a').get('href')
        blue_link = blue_fighter.find('a').get('href')
        print(f"Scraping fighter profiles: {red_link} and {blue_link}...")
        
        # scrape both fighters' profiles
        red_profile = scrape_fighter_profile(red_link)
        blue_profile = scrape_fighter_profile(blue_link)

        # Create a dictionary for the match data
        match_data = {
            'RedFighter': red_name,
            'BlueFighter': blue_name,
            'RedOdds': red_odds,
            'BlueOdds': blue_odds,
        }
        
        # Add all keys from RedProfile separately
        for key, value in red_profile.items():
            match_data[f'Red_{key}'] = value
        
        # Add all keys from BlueProfile separately
        for key, value in blue_profile.items():
            match_data[f'Blue_{key}'] = value

        # Add differences in relevant attributes
        match_data['HeightDif'] = red_profile['height_cms'] - blue_profile['height_cms']
        match_data['ReachDif'] = red_profile['reach_cms'] - blue_profile['reach_cms']
        match_data['LegReachDif'] = red_profile['leg_reach_cm'] - blue_profile['leg_reach_cm']
        match_data['WinDif'] = red_profile['wins'] - blue_profile['wins']
        match_data['LossDif'] = red_profile['losses'] - blue_profile['losses']
        match_data['DrawDif'] = red_profile['draws'] - blue_profile['draws']
        match_data['AgeDif'] = red_profile['age'] - blue_profile['age']
        match_data['KODif'] = red_profile['wins_by_ko'] - blue_profile['wins_by_ko']
        match_data['SubDif'] = red_profile['wins_by_sub'] - blue_profile['wins_by_sub']
        match_data['SigStrDif'] = red_profile['sig_strikes_per_min'] - blue_profile['sig_strikes_per_min']
        # determine who has the better rank
        if red_profile['rank'] is None and blue_profile['rank'] is None:
            match_data['BetterRank'] = 'Neither'
        elif red_profile['rank'] is None:
            match_data['BetterRank'] = 'Blue'
        elif blue_profile['rank'] is None:
            match_data['BetterRank'] = 'Red'
        else:
            if red_profile['rank'] < blue_profile['rank']:
                match_data['BetterRank'] = 'Red'
            elif red_profile['rank'] > blue_profile['rank']:
                match_data['BetterRank'] = 'Blue'
            else:
                match_data['BetterRank'] = 'Neither'

        # Append the match data to the list
        match_data_list.append(match_data)
        print(f"Added match: {red_name} vs {blue_name}")

    # Use the data manager to update the upcoming matches CSV
    update_upcoming_matches(match_data_list)

def scrape_fighter_profile(fighter_link: str):
    """
    Scrapes the fighter's profile page and returns the fighter's information.
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

    # get the win/loss/draw
    [wins, draws, losses] = soup.find('p', class_='hero-profile__division-body').text.strip().split(' ')[0].split('-')

    # get the age
    age = soup.find('div', class_='field--name-age').text.strip()

    all_rows_with_3_cols = soup.find_all('div', class_='c-bio__row--3col')
    # row with height & weight
    bio_row_3 = all_rows_with_3_cols[0]
    # get the height
    height_div = bio_row_3.find_all('div', class_='c-bio__text')
    height_cms = inches_to_cms(float(height_div[1].text.strip())) if len(height_div) > 1 else 0.0
    # row with reach & leg reach
    bio_row_4 = all_rows_with_3_cols[1]
    # get the reach
    reach_div = bio_row_4.find_all('div', class_='c-bio__text')
    reach_cms = inches_to_cms(float(reach_div[1].text.strip())) if len(reach_div) > 1 else 0.0
    # get the leg reach
    leg_reach_cm = inches_to_cms(float(reach_div[2].text.strip())) if len(reach_div) > 2 else 0.0

    athlete_stats = soup.find_all('div', class_='athlete-stats__stat')
    # get wins by ko
    wins_by_ko = 0
    # get wins by submission
    wins_by_sub = 0
    for stat in athlete_stats:
        if isinstance(stat, str):  # Check if stat is a string
            continue  # Skip string nodes
        text = stat.find("p", class_="athlete-stats__text athlete-stats__stat-text").text.strip()
        value = stat.find("p", class_="athlete-stats__stat-numb").text.strip()
        if text.lower() == "wins by knockout":
            wins_by_ko = int(value)
        elif text.lower() == "wins by submission":
            wins_by_sub = int(value)
            
    # get the significant strikes
    sig_strikes_div = soup.find('div', class_='c-stat-compare__group c-stat-compare__group-1')
    sig_strikes_number = sig_strikes_div.find('div', class_='c-stat-compare__number') if sig_strikes_div else None
    sig_strikes_per_min = float(sig_strikes_number.text.strip()) if sig_strikes_number else 0.0
    # get the rank
    tags = soup.find_all('p', class_='hero-profile__tag')
    rank = None
    if len(tags) > 1:
        [pfp,text] = tags[1].text.strip().split(' ') if len(tags[1].text.strip().split(' ')) > 1 else [None, tags[1].text.strip()]
        if text == 'PFP':
            rank = int(pfp[1:]) if pfp else None

    # Return all the collected information as a dictionary
    return {
        "wins": int(wins),
        "draws": int(draws),
        "losses": int(losses),
        "age": int(age),
        "height_cms": height_cms,
        "reach_cms": reach_cms,
        "leg_reach_cm": leg_reach_cm,
        "wins_by_ko": wins_by_ko,
        "wins_by_sub": wins_by_sub,
        "sig_strikes_per_min": sig_strikes_per_min,
        "rank": rank
    }


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
    #scrape_fighter_profile("https://www.ufc.com/athlete/jon-jones")