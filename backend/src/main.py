from flask import Flask, request
from flask_cors import CORS
import pandas as pd

PATH_TO_UPCOMING_DATA = "./data/upcoming.csv"
PATH_TO_PREVIOUS_DATA = "./data/previous-matches.csv"


app = Flask(__name__)
CORS(app)

@app.route("/upcoming")
def upcoming():
    upcoming_df = pd.read_csv(PATH_TO_UPCOMING_DATA)
    return upcoming_df.to_json(orient="records")

@app.route("/previous")
def previous():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    previous_df = pd.read_csv(PATH_TO_PREVIOUS_DATA)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_df = previous_df.iloc[start:end]
    return paginated_df.to_json(orient="records")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()