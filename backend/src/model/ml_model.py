import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
PATH_TO_DATA = "../data/previous-matches.csv"

class UFCModel:
    def __init__(self):
        # Load data
        self.df = pd.read_csv(PATH_TO_DATA)
        # TODO: Add more features
        self.features = ["AgeDif","BetterRank","ReachDif","RedOdds","BlueOdds","WinDif","LossDif","HeightDif","SigStrDif","KODif","SubDif"]
        self.extend_data()
        self.scaler = StandardScaler()
        self.model = LogisticRegression(max_iter=500)


    def extend_data(self):
        # Create target variable (1 for R_fighter win, 0 for B_fighter win)
        self.df['target'] = (self.df['Winner'] == 'Red').astype(int)
        self.df['BetterRank'] = self.df['BetterRank'].map({'Red': 1, 'Blue': -1, 'Neither': 0})

        # Fill missing values with 0
        self.df[self.features] = self.df[self.features].fillna(0)

    def train(self) -> float:
        """
        This method trains the RandomForestClassifier model using the features and target variable from the dataset.
        It splits the data into training and testing sets, trains the model on the training set, and evaluates the model
        on the testing set. The method returns the accuracy score of the model on the testing set.
        
        Returns:
            float: The accuracy score of the model on the testing set.
        """
        
        # Split data into features and target
        X, y = self.df[self.features], self.df['target']

        # Scale features
        X = self.scaler.fit_transform(X)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        self.model.fit(X_train, y_train)

        # Evaluate model
        score = self.model.score(X_test, y_test)
        return score

    def predict(self, upcoming_data_path: str):
        """
        This method predicts the results for upcoming matches using the trained model.
        
        Args:
            upcoming_data_path (str): The path to the CSV file containing upcoming match data.
        
        Returns:
            np.ndarray: Predictions for the upcoming matches (1 for R_fighter win, 0 for B_fighter win).
        """
        # Load upcoming data
        upcoming_df = pd.read_csv(upcoming_data_path)

        # Preprocess the data
        upcoming_df['BetterRank'] = upcoming_df['BetterRank'].map({'Red': 1, 'Blue': -1, 'Neither': 0})
        upcoming_df[self.features] = upcoming_df[self.features].fillna(0)

        # Scale features
        X_upcoming = self.scaler.transform(upcoming_df[self.features])

        # Make predictions
        predictions = self.model.predict(X_upcoming)
        return predictions

model = UFCModel()
score = model.train()
print(f"Model accuracy: {score:.5f}")

# Example usage
upcoming_predictions = model.predict("../data/upcoming.csv")
print("Predictions for upcoming matches:", upcoming_predictions)


