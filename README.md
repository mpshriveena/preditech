Project Name: PrediTech

Introduction
PrediTech is a web application which makes use of flask api to predict the price of a house based on certain user inputs. The application employs a machine learning model to make predictions

Features
1. Predicts the price of the house based on user input
2. Contains a trained machine learning model
3. Validations
4. Logging for tracking requests and predictions
5. Containerized using Docker

Technologies Used
1) Backend
        Flask
        Flask-CORS
        JobLib
2) Frontend
        Vue3
        Axios
3) Machine Learning
        Numpy
        Pandas
        SKLearn
        Catboost
4) Containerization
        Docker

Setup and Installation
Prerequisites
    Python 3.10 or above
    Node.js and npm
    Docker & Docker Compose

Installation
1) Clone the repository
    git clone https://github.com/mpshriveena/preditech.git
2) Installing and running locally
    1. Backend Installation
        cd preditech/backend
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
    2. Running the Backend
        python3 app.py
    3. Frontend Installation
        cd ../frontend
        npm install
    4. Running the frontend
        npm run dev
3) Running with Docker
        cd preditech
        docker-compose up --build

Logging and Monitoring
All the logs, requests and predictions can be viewed in the app.log file

Docker Integration
The project is fully containerized, with separate Dockerfiles for the backend and frontend:
Backend Dockerfile builds the Flask API.
Frontend Dockerfile builds the Vue.js application.
The docker-compose.yml file orchestrates the services for easy setup.

Viewing the application
The application will be running in the port 5173.
http://localhost:5173/

API Endpoints
HTTP Method--> POST
Endpoint--> /predict
Description--> Predict house price based on input data.                                 

Example Payload for /predict:
{
  "overall_quality": 7,
  "gr_liv_area": 1500,
  "garage_cars": 2,
  "garage_area": 400,
  "total_bsmt_sf": 800
}

Contact
Author: M. P. Shri Veena
Email: mpshriveena@gmail.com