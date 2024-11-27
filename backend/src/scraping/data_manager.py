import pandas as pd
from typing import List, Dict, Union

previous_matches_path = "../data/previous-matches.csv"
upcoming_matches_path = "../data/upcoming.csv"

def merge_upcoming_to_previous():
    """Adds upcoming matches data to the previous matches file"""
    upcoming_df = pd.read_csv(upcoming_matches_path)
    previous_df = pd.read_csv(previous_matches_path)
    
    # Combine dataframes
    combined_df = pd.concat([upcoming_df, previous_df], ignore_index=True)
    
    # Save back to previous matches file
    combined_df.to_csv(previous_matches_path, index=False)

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