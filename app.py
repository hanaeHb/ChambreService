from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# JWT Configuration
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", 604800))

# Initialize JWT
jwt = JWTManager(app)

# Test route
@app.route('/')
def hello_world():
    return 'Hello World! JWT is working '

if __name__ == '__main__':
    print("Starting Flask app on port 8088...")
    app.run(debug=True, port=8088)
