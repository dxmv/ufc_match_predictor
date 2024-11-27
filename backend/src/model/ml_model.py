import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
PATH_TO_DATA = "../data/previous-matches.csv"

class UFCModel:
    def __init__(self):
        # Load data
        self.df = pd.read_csv(PATH_TO_DATA)
        # TODO: Add more features
        self.features = ["AgeDif","BetterRank","ReachDif","RedOdds","BlueOdds","WinDif","LossDif","HeightDif","WinStreakDif","LoseStreakDif","TotalTitleBoutDif"]
        self.extend_data()
        self.model = RandomForestClassifier()


    def extend_data(self):
        # Create target variable (1 for R_fighter win, 0 for B_fighter win)
        self.df['target'] = (self.df['Winner'] == 'Red').astype(int)
        self.df['BetterRank'] = (self.df["BetterRank"] == "Red").astype(int)

        # Fill missing values with 0
        self.df[self.features] = self.df[self.features].fillna(0)

    def train(self):
        # Split data into features and target
        X,y = self.df[self.features], self.df['target']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        self.model.fit(X_train, y_train)

        # Evaluate model
        score = self.model.score(X_test, y_test)
        return score


model = UFCModel()
score = model.train()
print(f"Model accuracy: {score:.2f}")
score = model.train()
print(f"Model accuracy: {score:.2f}")
score = model.train()
print(f"Model accuracy: {score:.2f}")


