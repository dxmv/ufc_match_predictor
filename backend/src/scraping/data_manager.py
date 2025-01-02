import pandas as pd
from typing import List, Dict, Union

previous_matches_path = "../data/previous-matches.csv"
upcoming_matches_path = "../data/upcoming.csv"
fighters_path = "../data/fighters.csv"


def merge_upcoming_to_previous():
    """Adds upcoming matches data to the previous matches file"""
    upcoming_df = pd.read_csv(upcoming_matches_path)
    previous_df = pd.read_csv(previous_matches_path)
    
    # Combine dataframes
    combined_df = pd.concat([upcoming_df, previous_df], ignore_index=True)
    
    # Save back to previous matches file
    combined_df.to_csv(previous_matches_path, index=False)

def update_fighters_images(fighters: Dict[str, str]) -> None:
    """
    Updates the fighters.csv file with the new fighter images
    If a fighter is not in the file, a new row will be created.
    If the file is empty, it should be created.
    """
    try:
        fighters_df = pd.read_csv(fighters_path)
    except pd.errors.EmptyDataError:
        # Create an empty DataFrame with the required columns if the file is empty
        fighters_df = pd.DataFrame(columns=['FighterName', 'ImageLink'])
    
    # Update the DataFrame with new images or create new rows if the fighter isn't in the file
    for fighter, image_link in fighters.items():
        if fighter in fighters_df['FighterName'].values:
            fighters_df.loc[fighters_df['FighterName'] == fighter, 'ImageLink'] = image_link
        else:
            new_row = pd.DataFrame({'FighterName': [fighter], 'ImageLink': [image_link]})
            fighters_df = pd.concat([fighters_df, new_row], ignore_index=True)
    
    # Save the updated DataFrame back to the CSV file
    fighters_df.to_csv(fighters_path, index=False)

def update_upcoming_matches(new_matches: List[Dict[str, Union[str, float, int]]]) -> None:
    """
    Clears all existing rows from upcoming.csv and adds new match data.
    
    Args:
        new_matches: List of dictionaries containing match data.
                    Each dict should have keys matching the CSV columns.
                    
    Example:
        new_matches = [
            {
                'RedFighter': 'John Doe',
                'BlueFighter': 'Jane Doe',
                'RedOdds': 1.5,
                # ... other match data ...
            }
        ]
    """
    # Convert list of dictionaries to DataFrame
    new_df = pd.DataFrame(new_matches)
    
    # Save new data to upcoming matches file, overwriting existing content
    new_df.to_csv(upcoming_matches_path, index=False)

def populate_fighters_csv_with_previous_matches(scrape_fighter_profile):
    """
    Populates the fighters.csv file with the fighters from the previous matches
    and their profile images by scraping each fighter's profile
    
    Args:
        scrape_fighter_profile: Function to scrape fighter profiles
    """
    previous_df = pd.read_csv(previous_matches_path)
    
    # Extract unique fighters from both RedFighter and BlueFighter columns
    unique_fighters = pd.Series(previous_df[['RedFighter', 'BlueFighter']].values.ravel()).unique()[:500]
    
    # Create a dictionary to store fighter names and their image links
    fighter_images = {}
    
    print(len(unique_fighters))
    i = 0
    # Scrape profile for each fighter
    for fighter in unique_fighters:
        try:
            print(f"Scraping profile for {fighter}")
            profile = scrape_fighter_profile(f"https://www.ufc.com/athlete/{fighter.split(' ')[0].lower()}-{fighter.split(' ')[1].lower()}")
            fighter_images[fighter] = profile['ImageLink']
        except Exception as e:
            print(f"Error scraping profile for {fighter}: {str(e)}")
            continue
        i += 1
        if i % 100 == 0:
            print(f"Scraped {i} profiles")
    
    # Update the fighters.csv file with the new data
    update_fighters_images(fighter_images)

def populate_fights_with_images(file_path: str):
    """
    Populates the fights with images
    """
    fights_df = pd.read_csv(file_path)
    fighters_df = pd.read_csv(fighters_path)

    for index, row in fights_df.iterrows():
        print(f"Processing row {index}")
        red_fighter = row['RedFighter']
        blue_fighter = row['BlueFighter']
        
        # Check if the red fighter exists in the fighters_df
        red_fighter_image = None
        red_fighter_row = fighters_df[fighters_df['FighterName'] == red_fighter]
        if not red_fighter_row.empty:
            red_fighter_image = red_fighter_row['ImageLink'].values[0]
        
        # Check if the blue fighter exists in the fighters_df
        blue_fighter_image = None
        blue_fighter_row = fighters_df[fighters_df['FighterName'] == blue_fighter]
        if not blue_fighter_row.empty:
            blue_fighter_image = blue_fighter_row['ImageLink'].values[0]
        
        fights_df.at[index, 'RedFighterImage'] = red_fighter_image
        fights_df.at[index, 'BlueFighterImage'] = blue_fighter_image
    print("Finished")
    fights_df.to_csv(file_path, index=False)

if __name__ == "__main__":
    populate_fights_with_images(previous_matches_path)
    populate_fights_with_images(upcoming_matches_path)