# Forecasting India's Economic Future: A Linear Regression Approach
This project utilizes historical GDP data of India from 1960 to 2023 to predict future GDP values for 2024 and 2025. Using a linear regression model, it provides insights into the economic trajectory of one of the world's fastest-growing economies. 

At the heart of this project is the [`Forecasting_India_GDP.ipynb`](https://github.com/neuraledgeai/India_GDP_Forecasting_Project/blob/main/Forecasting_India_GDP.ipynb) notebook. This file contains the full analysis, from data preparation and feature engineering to model building and evaluation.

## Table of Contents

- [See the Model Live in Action!](#see-the-model-live-in-action)
- [Dataset Overview](#dataset-overview)
- [Purpose of This Project](#purpose-of-this-project)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Model Description](#model-description)
- [Access the Full Project](#access-the-full-project)

## See the Model Live in Action!

<img width="1431" alt="Screenshot 2024-09-29 at 6 41 11 PM" src="https://github.com/user-attachments/assets/4527c2d0-603e-4400-a4d6-f139adaa1237">

Curious about how the model works in practice? You can experience it firsthand by visiting the web app we've developed! This interactive dashboard lets you explore India's GDP forecasts, visualize historical GDP trends, and compare actual versus predicted values with ease.

Check it out here: [India GDP Forecasting Web App](https://india-gdp-forecasting.streamlit.app).

## Dataset Overview

The data used in this project is sourced from the [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN), which provides reliable and up-to-date global economic data. The dataset includes India’s GDP values from 1960 to 2023, offering a rich time series for analysis and forecasting.

- **Key Insights from Exploration**:

   - **GDP Growth Over Time**: The data reflects India's gradual economic growth, followed by rapid expansion starting around 2011, coinciding with key economic reforms and global      market shifts.
   - **Strong Temporal Relationships**: One of the key features analyzed in this project is the strong relationship between GDP and its one-year lag (GDP_L1). This provides insight     into how the previous year's GDP influences future economic outcomes, a fundamental aspect of the linear regression model applied here.
   - **Outliers and Economic Milestones**: Outliers in the data (such as the steep GDP growth around 2017-2023) mirror significant milestones in India’s economic history, reflecting    fast-paced development, investments, and policy changes.

- **Data Columns**:

  - **Year**: The year the GDP value corresponds to.
  - **GDP**: India’s Gross Domestic Product in current USD.
  - **GDP_L1**: A one-year lag of the GDP value used as a feature for model training and prediction.

The exploration phase of the data provided clear evidence of a strong linear trend between past and future GDP values, which was leveraged to build and train the model.

## Purpose of This Project
This project is designed for **educational purposes** and to demonstrate the **capabilities** of time series analysis using linear regression. Through this project, you’ll gain an intuitive understanding of how to approach time series forecasting in a practical and reasonable way. It encompasses various aspects of data science, such as:

- **Data preparation**
- **Model building**
- **Model evaluation**
- Showcasing special **data scientist skills** like dealing with real-world datasets, handling outliers, and visualizing results.

This project is proudly dedicated to the **open-source community**, with the goal of helping learners and professionals explore the practical applications of machine learning.

## Key Features

- **Dynamic GDP Predictions**: Forecasts GDP values for the upcoming years.
- **Interactive Dashboard**: Built using Streamlit, providing an engaging user interface.
- **Visualizations**: Clear and informative plots showcasing GDP trends over time and actual vs. predicted values.

## Technologies Used

- **Python**: Programming language used for data analysis and modeling.
- **Pandas**: Library for data manipulation and analysis.
- **NumPy**: Library for numerical computations.
- **Scikit-learn**: Machine learning library for building the regression model.
- **Plotly & Matplotlib**: Libraries for creating interactive visualizations.
- **Streamlit**: Framework for building web applications for data science.

## Model Description

This project employs a **Linear Regression** model to forecast India's GDP for the years 2024 and 2025.

- **Model Training**:

   - **Input Feature**: The model was trained using India's GDP_L1, which represents the GDP of the previous year. This feature was selected based on the observed strong correlation between current and past GDP values.
   - **Target Variable**: The actual GDP values from 1960 to 2023 served as the target variable, representing the ground truth for the model to learn from.

<p align="center"> <code>GDP = b1 + b2 * GDP_L1</code> </p>

- **Where**,
   - `b1` is the intercept (constant term),
   - `b2` is the coefficient (slope), representing the relationship between the GDP of the previous year and the predicted GDP.
 
- **Performance and Evaluation**:
   - The model was evaluated on the training data, and the predictions closely matched the actual GDP values, demonstrating the model’s ability to capture the linear relationship between consecutive years’ GDPs.
   - The **Actual vs Predicted GDP** plot (available in the web app) provides a visual representation of how well the model fits the historical data.

- **Prediction**:
   - The model used the **GDP of 2023** as the starting point to forecast India's GDP for **2024**.
   - The **2024 predicted GDP** value was then used as input to predict India’s GDP for **2025**.

While the model performs well on the training data and provides reasonable forecasts, it is important to note that linear regression models can have limitations, especially for highly complex or non-linear trends. The results should be interpreted as average forecasts based on historical patterns.

## Access the Full Project

For anyone interested in the full, detailed steps of this project, including everything from data importing, exploration, splitting, model building, tuning, evaluation, and prediction function to saving the model, please refer to the [`Forecasting_India_GDP.ipynb`](https://github.com/neuraledgeai/India_GDP_Forecasting_Project/blob/main/Forecasting_India_GDP.ipynb) notebook. This notebook is the heart of the project, containing all the comprehensive steps for creating the model.

Additionally, check out the [`streamlit_app.py`](https://github.com/neuraledgeai/India_GDP_Forecasting_Project/blob/main/streamlit_app.py) file, which is designed to serve as the main backend for deploying the model as a web app.


*This project is proudly dedicated to the open-source community for educational and capability demonstration purposes. It showcases the application of machine learning technology for time series data, while intuitively enhancing essential data science skills. We hope this serves as a valuable resource for anyone looking to explore and learn from practical, real-world examples.*

