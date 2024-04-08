from flask import request, jsonify
from config import app
from odds import api_odds

@app.route("/odds", methods=["GET"])
def get_odds():
    odds = api_odds()
    return jsonify({"odds": odds})

if __name__ == "__main__":
    app.run(debug=True)
