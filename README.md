# Boston House Price Prediction - End-to-End Machine Learning Project

This repository contains a complete **end-to-end machine learning project** for predicting house prices in Boston using the **Boston House Price Dataset**. The project covers everything from data cleaning, exploratory data analysis, model building, deployment, and testing. The model is deployed on **Heroku** as a web application, utilizing **MLOps** principles.

## Project Overview

This project involves building a machine learning regression model to predict house prices based on various features. The process covers the full machine learning lifecycle, from **data cleaning** to **model deployment**.

### Key Steps:
1. **Data Collection**: Downloaded the **Boston House Price Dataset** from **Kaggle**.
2. **Data Cleaning**: Removed null values, handled missing data, and prepared the data for analysis.
3. **Exploratory Data Analysis (EDA)**:
   - Visualized the data to understand feature distributions.
   - Found **correlations** between features.
   - Removed unnecessary features to improve model performance.
4. **Model Building**: Created a **regression model** using a train-test split.
5. **Model Evaluation**:
   - Tested the model using various parameters.
   - Checked for **overfitting** and tuned the model for optimal performance.
6. **MLOps and Deployment**:
   - Built a **Flask app** to serve the model.
   - Created an **HTML page** for user interaction.
   - Deployed the app to **Heroku**.
   - Used **Postman** for routing and API testing.

### Key Features:
- **End-to-End Machine Learning**: Covers all aspects from data cleaning to model deployment.
- **Regression Model**: Predicts house prices based on various features like the number of rooms, crime rate, etc.
- **MLOps**: Implemented using Flask and Heroku for seamless deployment.
- **Model Testing**: Thoroughly tested to ensure it performs well without overfitting.
- **Exploratory Data Analysis**: Visualized important features and relationships in the data.
- **Deployment on Heroku**: The model is accessible as a web application deployed on the cloud.

## Tools and Technologies
- **Python**: Used for data cleaning, model building, and backend development.
- **Flask**: Built the web application to serve the model.
- **Heroku**: Deployed the machine learning model as a web app on the cloud.
- **Postman**: Used for API routing and testing.
- **Pandas/NumPy/Scikit-Learn**: Used for data analysis and machine learning model creation.
- **HTML/CSS**: Created the front-end interface for the app.

## Project Structure
- **Data**: Contains the cleaned dataset used for model training.
- **Python Files**: Includes scripts for data cleaning, exploratory data analysis, and model building.
- **Requirements File**: Contains all necessary dependencies to run the project.
- **Procfile**: Required for deploying the project on Heroku.
- **HTML Page**: The front-end interface for the web app.

## How to Set Up the Project

1. **Create a new environment** for the project:
   ```bash
   conda create -p venv python=3.12 -y
## How to Set Up the Project

2. **Activate the environment**:
   ```bash
   conda activate C:\Users\apurb\Downloads\end-to-end-ml\venv
3. **Deactivate the environment** (when you are done working):
   ```bash
   conda deactivate
4. **Install necessary libraries**:
   You can install all required dependencies with one command:
   ```bash
   pip install -r requirements.txt
5. **Run the Flask app** locally:
   ```bash
   python app.py
6. **Access the web app** by visiting `http://localhost:5000/` in your browser.
