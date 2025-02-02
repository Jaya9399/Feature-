from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["feature_flags_db"]
feature_flags = db["feature_flags"]

# Create or Update a Feature Flag
@app.route('/feature-flags', methods=['POST'])
def create_feature_flag():
    data = request.json
    name = data.get('name')
    enabled = data.get('enabled', False)
    environment = data.get('environment', 'production')

    feature_flags.update_one(
        {"name": name, "environment": environment},
        {"$set": {"enabled": enabled}},
        upsert=True
    )
    
    return jsonify({"message": f"Feature flag '{name}' updated!", "enabled": enabled}), 201

# Get Feature Flag for a User
@app.route('/feature-flags/<name>/<user_id>', methods=['GET'])
def get_feature_flag(name, user_id):
    environment = request.args.get('environment', 'production')
    flag = feature_flags.find_one({"name": name, "environment": environment})

    if flag:
        return jsonify({"enabled": flag["enabled"]})
    return jsonify({"error": "Feature flag not found"}), 404

# Toggle a Feature Flag
@app.route('/feature-flags/<name>/toggle', methods=['PUT'])
def toggle_feature_flag(name):
    environment = request.args.get('environment', 'production')
    flag = feature_flags.find_one({"name": name, "environment": environment})

    if flag:
        new_status = not flag["enabled"]
        feature_flags.update_one({"name": name, "environment": environment}, {"$set": {"enabled": new_status}})
        return jsonify({"message": f"Feature flag '{name}' toggled!", "enabled": new_status})
    
    return jsonify({"error": "Feature flag not found"}), 404

# Edit a Feature Flag (Update name, enabled status, or environment)
@app.route('/feature-flags/<name>', methods=['PUT'])
def edit_feature_flag(name):
    data = request.json
    environment = data.get('environment', 'production')
    new_name = data.get('name')
    enabled = data.get('enabled', False)

    flag = feature_flags.find_one({"name": name, "environment": environment})

    if flag:
        updated_data = {"enabled": enabled}
        if new_name:
            updated_data["name"] = new_name
        
        feature_flags.update_one({"name": name, "environment": environment}, {"$set": updated_data})
        return jsonify({"message": f"Feature flag '{name}' updated to '{new_name}'!" if new_name else f"Feature flag '{name}' updated!"})
    
    return jsonify({"error": "Feature flag not found"}), 404

# Delete a Feature Flag
@app.route('/feature-flags/<name>', methods=['DELETE'])
def delete_feature_flag(name):
    environment = request.args.get('environment', 'production')
    flag = feature_flags.find_one({"name": name, "environment": environment})

    if flag:
        feature_flags.delete_one({"name": name, "environment": environment})
        return jsonify({"message": f"Feature flag '{name}' deleted!"})
    
    return jsonify({"error": "Feature flag not found"}), 404

# List All Feature Flags
@app.route('/feature-flags', methods=['GET'])
def list_feature_flags():
    flags = list(feature_flags.find({}, {"_id": 0}))
    return jsonify(flags)

@app.route('/')
def home():
    return "Feature Flag API is Running!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
