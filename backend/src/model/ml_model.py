import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Get the directory containing the script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_DATA = os.path.join(os.path.dirname(CURRENT_DIR), "data", "previous-matches.csv")
PATH_TO_UPCOMING_DATA = os.path.join(os.path.dirname(CURRENT_DIR), "data", "upcoming.csv")

class UFCModel:
    def __init__(self):
        # Load data
        self.df = pd.read_csv(PATH_TO_DATA)
        # TODO: Add more features
        self.features = ["AgeDif","BetterRank","ReachDif","RedOdds","BlueOdds","WinDif","LossDif","HeightDif","SigStrDif","KODif","SubDif"]
        self.extend_data()
        self.scaler = StandardScaler()
        self.model = LogisticRegression(random_state=42)

    def extend_data(self):
        # Create target variable (1 for R_fighter win, 0 for B_fighter win)
        self.df['target'] = (self.df['Winner'] == 'Red').astype(int)
        self.df['BetterRank'] = self.df['BetterRank'].map({'Red': 1, 'Blue': -1, 'Neither': 0})

        # Fill missing values with 0
        self.df[self.features] = self.df[self.features].fillna(0)

    def train(self) -> float:
        """
        This method trains the LogisticRegression model using the features and target variable from the dataset.
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

        # Add predicted column to the dataframe
        self.df['predicted'] = self.model.predict(X)
        self.df.to_csv(PATH_TO_DATA, index=False)

        return score

    def get_accuracy(self) -> float:
        """
        This method returns the accuracy of the trained model on the training data.
        
        Returns:
            float: The accuracy score of the model on the training data.
        """
        if not hasattr(self.model, 'coef_'):
            raise ValueError("Model has not been trained yet. Call train() first.")
            
        X, y = self.df[self.features], self.df['target']
        
        # Check if scaler has been fitted
        if not hasattr(self.scaler, 'mean_'):
            self.scaler.fit(X)
            
        X = self.scaler.transform(X)
        return self.model.score(X, y)

    def predict(self):
        """
        This method predicts the results for upcoming matches using the trained model.
        
        Returns:
            np.ndarray: Predictions for the upcoming matches (1 for R_fighter win, 0 for B_fighter win).
        """
        # Load upcoming data
        upcoming_df = pd.read_csv(PATH_TO_UPCOMING_DATA)

        # Preprocess the data
        upcoming_df['BetterRank'] = upcoming_df['BetterRank'].map({'Red': 1, 'Blue': -1, 'Neither': 0})
        upcoming_df[self.features] = upcoming_df[self.features].fillna(0)

        # Scale features
        X_upcoming = self.scaler.transform(upcoming_df[self.features])

        # Make predictions
        predictions = self.model.predict(X_upcoming)

        # Add predicted column to the upcoming dataframe
        upcoming_df['predicted'] = predictions

        # Save the result
        upcoming_df.to_csv(PATH_TO_UPCOMING_DATA, index=False)

        return predictions

# model = UFCModel()
# score = model.train()
# print(f"Model accuracy: {score:.5f}")
# accuracy = model.get_accuracy()
# print(f"Model accuracy on training data: {accuracy:.5f}")

# upcoming_predictions = model.predict()
# print("Predictions for upcoming matches:", upcoming_predictions)
