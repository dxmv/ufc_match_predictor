from flask import Flask, request
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

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()