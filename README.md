
# FeatureFlow Implementation

This repository implements a backend solution for dynamic feature flag management using FeatureFlow. It includes an API for managing feature flags, evaluating feature flag states based on users' attributes, and supporting environment-specific configurations. The project also includes a simple front-end for managing feature flags.

## Features
- Manage multiple feature flags with on/off or variant values (e.g., A/B tests).
- Evaluate feature flags dynamically for specific users based on user attributes (e.g., `userID`, `subscriptionType`, `region`).
- Manage feature flags for different environments (`development`, `staging`, `production`).
- Toggle feature flags and track changes with audit logging.
- Use MongoDB to store feature flags and user configurations.
- Web interface to manage feature flags and toggle them.
  
## Prerequisites

Before running the project, make sure you have the following dependencies installed:

### 1. **Backend Setup (Python)**
Ensure you have Python 3.x installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### 2. **MongoDB Setup**
- Install [MongoDB](https://www.mongodb.com/try/download/community) and ensure it's running.
- Alternatively, you can use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for a cloud-based MongoDB instance.

### 3. **Install Required Dependencies**

Once you've cloned the repository, navigate to the project directory and install the necessary dependencies.

#### Using `pip` (Python)

```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt


### All the steps after creating all the files and uploading it you will see
here is the image demonstrating App interface



Running the Project
1. Start the Backend (API Server)
To start the backend API server, run the following command:
bash
Copy
Edit
python backend.py
The server will start, and you'll be able to test the feature flag endpoints via Postman or another API testing tool at http://127.0.0.1:5000.
2. Start the Frontend
Open the index.html file in your web browser to view and manage the feature flags.
API Endpoints
Here is a list of available API endpoints to interact with the feature flags:

GET /feature-flags/{feature_name}/{user_id}
Description: Returns the flag state (true/false or a variant) for a specific user.
Parameters:
feature_name: The name of the feature flag (e.g., darkMode).
user_id: The user ID for whom to check the feature flag state.
Example Request:
http
Copy
Edit
GET http://127.0.0.1:5000/feature-flags/darkMode/12345
POST /feature-flags/{feature_name}
Description: Create or update a feature flag.
Request Body:
json
Copy
Edit
{
  "enabled": true,
  "environment": "production"
}
Example Request:
http
Copy
Edit
POST http://127.0.0.1:5000/feature-flags/darkMode
GET /feature-flags
Description: Lists all feature flags with their current values and environments.
Example Request:
http
Copy
Edit
GET http://127.0.0.1:5000/feature-flags
PUT /feature-flags/{feature_name}/toggle
Description: Toggle the feature flag value between true and false for all users in a specific environment.
Example Request:
http
Copy
Edit
PUT http://127.0.0.1:5000/feature-flags/darkMode/toggle
Postman API Testing
You can use Postman to test the API endpoints. Here's how to set it up:

GET /feature-flags/{feature_name}/{user_id}:

Set the method to GET in Postman.
Enter the endpoint URL http://127.0.0.1:5000/feature-flags/darkMode/12345.
Click Send to see the response.
POST /feature-flags/{feature_name}:

Set the method to POST in Postman.
Enter the endpoint URL http://127.0.0.1:5000/feature-flags/darkMode.
Set the body to JSON format:
json
Copy
Edit
{
  "enabled": true,
  "environment": "production"
}
Click Send to create or update the feature flag.
PUT /feature-flags/{feature_name}/toggle:

Set the method to PUT in Postman.
Enter the endpoint URL http://127.0.0.1:5000/feature-flags/darkMode/toggle.
Click Send to toggle the feature flag.
