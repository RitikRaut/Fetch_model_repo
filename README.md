# Fetch_model_repo

# Scanned Receipts Prediction for 2022 at Fetch.

This project aims to predict the approximate number of scanned receipts for each month of 2022 based on observed scanned receipts data from 2021. It includes building a machine learning model ARIMA and deploying it as an inference service in a Docker container.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Data](#data)
- [Model Development](#model-development)
- [Inference Service](#inference-service)
- [Dockerization](#dockerization)
- [Usage](#usage)


## Introduction

At Fetch Rewards, predicting the number of scanned receipts is crucial for business monitoring and planning. This project addresses this challenge by developing a machine learning model to predict scanned receipts for each month of 2022 based on historical data from 2021.

## Project Structure

The project is structured as follows:

- `data_daily.csv`: CSV file containing observed scanned receipts data for 2021.
- `app.py`: Python script for the inference service.
- `arima_model.ipynb`: Jupyter Notebook building the machine learning model.
- `requirements.txt`: List of Python packages required for the project.
- `Dockerfile`: Configuration file for creating a Docker container.

## Getting Started

### Prerequisites

- Python 3.x
- Docker

### Installation

1. Clone this repository:

git clone https://github.com/RitikRaut/Fetch_model_repo.git

3. Install the required Python packages:
   
pip install -r requirements.txt

3. Data
The data_daily.csv file contains observed scanned receipts data for 2021. Ensure this data is available or replace it with your own dataset.

4. Model Development
The machine learning model for scanned receipts prediction is developed in model.py. You can customize the model architecture and hyperparameters as needed.

5. Inference Service
The app.py script creates an inference service to predict scanned receipts for each month of 2022. It includes user interaction and visualization for the predictions.

6. Dockerization
The project can be packaged in a Docker container for easy deployment. Use the provided Dockerfile to build the container.

6. Usage
Train the machine learning model by running the notebook.
Deploy the inference service using app.py.
Build and run the Docker container for the service.
Access the service through the provided user interface.
