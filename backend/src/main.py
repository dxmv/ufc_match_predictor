from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from model.ml_model import UFCModel

PATH_TO_UPCOMING_DATA = "./data/upcoming.csv"
PATH_TO_PREVIOUS_DATA = "./data/previous-matches.csv"


app = Flask(__name__)
CORS(app)
model = UFCModel()

# Initialize your model
model = UFCModel()

# Route: Train the model
@app.route('/train', methods=['POST'])
def train():
    score = model.train()
    return jsonify({"message": "Model trained successfully!", "accuracy": score})

# Returns the accuracy of the model
@app.route('/accuracy', methods=['GET'])
def accuracy():
    score = model.get_accuracy()
    return jsonify({"message": "Model accuracy!", "accuracy": score})

# Route: Predict upcoming matches
@app.route('/upcoming', methods=['GET'])
def upcoming():
    predictions = model.predict()
    # Load predictions for response
    upcoming_data = pd.read_csv(PATH_TO_UPCOMING_DATA)
    return upcoming_data.to_json(orient="records")

# Route: Get previous matches
@app.route("/previous")
def previous():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    previous_df = pd.read_csv(PATH_TO_PREVIOUS_DATA)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = previous_df.iloc[start:end]
    return paginated_data.to_json(orient="records")

# Route: Get a single upcoming match by ID
@app.route("/upcoming/match/<match_id>", methods=['GET'])
def get_upcoming_match(match_id):
    try:
        date, red_name, blue_name = match_id.split('_')
    except ValueError:
        return jsonify({"error": "Invalid match ID format"}), 400

    upcoming_df = pd.read_csv(PATH_TO_UPCOMING_DATA)
    matches = upcoming_df[
        (upcoming_df['RedFighter'] == red_name) &
        (upcoming_df['BlueFighter'] == blue_name)
    ]

    if matches.empty:
        return jsonify({"error": "Match not found"}), 404

    # If multiple matches, filter by date
    if len(matches) > 1:
        matches = matches[matches['Date'] == date]

    if not matches.empty:
        return matches.iloc[0].to_json()
    else:
        return jsonify({"error": "Match not found"}), 404

# Route: Get a single previous match by ID
@app.route("/previous/match/<match_id>", methods=['GET'])
def get_previous_match(match_id):
    try:
        date, red_name, blue_name = match_id.split('_')
    except ValueError:
        return jsonify({"error": "Invalid match ID format"}), 400
    print(date,red_name,blue_name)

    previous_df = pd.read_csv(PATH_TO_PREVIOUS_DATA)
    matches = previous_df[
        (previous_df['RedFighter'] == red_name) &
        (previous_df['BlueFighter'] == blue_name)
    ]

    if matches.empty:
        return jsonify({"error": "Match not found"}), 404

    # If multiple matches, filter by date
    if len(matches) > 1:
        matches = matches[matches['Date'] == date]

    if not matches.empty:
        return matches.iloc[0].to_json()
    else:
        return jsonify({"error": "Match not found"}), 404

def main():
    app.run(debug=True)

if __name__ == "__main__":
    model.train()
    main()