import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

# Centrally aligned title

# Load the dataset and prepare it
df = pd.read_csv("gdp_india_1960-2023.csv")
df = pd.melt(
    df,
    id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],  # Columns to keep as identifiers
    var_name='Year',      # The name of the new column for the years
    value_name='GDP'      # The name of the new column for the GDP values
)

# Setting the 'Year' column as the index and dropping unnecessary columns
df = df.set_index("Year").drop(columns=["Country Name", "Country Code", "Indicator Name", "Indicator Code"])

# Adding a new feature for GDP_L1
df['GDP_L1'] = df['GDP'].shift(1)
df = df.dropna()  # Drop rows with NaN values resulting from the shift

# Load the saved model
@st.cache(allow_output_mutation=True)  # Cache to avoid reloading the model multiple times
def load_model():
    model = joblib.load('india_gdp_forecasting_model.pkl')
    return model

# Load the model once
model = load_model()

# Function to make predictions
def make_prediction(gdp):
    """
    Predict the GDP for the next year based on a given year's GDP.
    """
    # Prepare the data for the next year's prediction
    X = np.array([[gdp]])
    
    # Make the prediction for the next year
    predicted_gdp = model.predict(X)
    
    # Return the predicted GDP value
    return predicted_gdp

def forecast():

    st.markdown(
        """
        <div style="text-align: center;">
        <h1 style="font-size: 36px;">Forecasting India's Economic Future: Predicting 2024 and 2025</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('')
    # GDP for 2023
    gdp_2023 = 3_353_470_000_000  # GDP value for 2023

    # Predict GDP for 2024 using 2023 GDP value
    gdp_predicted_2024 = make_prediction(gdp_2023)[0]

    # Predict GDP for 2025 using the predicted GDP value for 2024
    gdp_predicted_2025 = make_prediction(gdp_predicted_2024)[0]

    # Section: Displaying the prediction
    # Display the predicted GDP for 2024 with larger font and centered alignment

    with st.container():
        st.markdown(
        f"""
        <div style="text-align: center; border: 2px solid #4CAF50; border-radius: 10px; padding: 20px; background-color: #f9f9f9;">
            <h2 style="font-size: 32px; color: #4CAF50;">Predicted GDP for India in 2024</h2>
            <p style="font-size: 28px; font-weight: bold; color: #ff7f50;">${gdp_predicted_2024:,.2f}</p>
        </div>
        """,
        unsafe_allow_html=True
        )

    st.markdown('')
    # Display the predicted GDP for 2025 with larger font and centered alignment
    with st.container():
        st.markdown(
        f"""
        <div style="text-align: center; border: 2px solid #4CAF50; border-radius: 10px; padding: 20px; background-color: #f9f9f9;">
            <h2 style="font-size: 32px; color: #4CAF50;">Predicted GDP for India in 2025</h2>
            <p style="font-size: 28px; font-weight: bold; color: #ff7f50;">${gdp_predicted_2025:,.2f}</p>
        </div>
        """,
        unsafe_allow_html=True
        )
    st.markdown('')
    st.info("Looks like India is still charging ahead! A **3.5 trillion** economy in 2024, and we're on the way to an even higher number in 2025. Watch out world!")
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    This model can make mistakes. Check important info.
    </div>
    """, unsafe_allow_html=True)
    
def gdp_over_time():
    # Section: Plot India's GDP over time
    st.header("India's GDP Over Time", divider="rainbow")
    st.write("""
    This plot shows India's GDP from 1961 to 2023, reflecting the economic journey of the country over the decades. You can clearly see the rapid rise, particularly since the 1990s, as India emerges as one of the world's largest economies.
    """
            )

    # Plot India's GDP from 1960 to 2023
    fig1 = px.line(df.reset_index(), x='Year', y='GDP', 
                   title="India's GDP from 1961 to 2023",
                   labels={'GDP': 'GDP (in Trillions of USD)', 'Year': 'Year'},
                   markers=True
                  )

    # Show the first plot
    st.plotly_chart(fig1)

def actual_vs_predicted_gdp():
    # Section: Plot Actual vs Predicted GDP
    st.header("Actual vs Predicted GDP", divider="rainbow")
    st.write("""
    The following plot shows how well the model fits with the historical data. It compares the actual GDP values to the model's predicted values, showing that our model performs quite well.
    """
            )

    # Predict the entire dataset using the 'GDP_L1' feature
    feature = ["GDP_L1"]
    X = df[feature]
    predicted_gdp = model.predict(X)

    # Plot Actual vs Predicted GDP (using the model's prediction)
    fig2 = px.line(df.reset_index(), x='Year', y=[df['GDP'], predicted_gdp.flatten()], 
                   title="Actual vs Predicted GDP",
                   labels={'value': 'GDP (in Trillions of USD)', 'Year': 'Year'},
                   markers=True)
    
    # Update the legend with custom names
    fig2.for_each_trace(lambda t: t.update(name='Actual GDP' if t.name == 'wide_variable_0' else 'Predicted GDP'))

    # Show the second plot
    st.plotly_chart(fig2)





##

# Sidebar with options for navigation within the app
st.sidebar.header("Navigate the Dashboard")

navigation = st.sidebar.radio(
    "Go to:",
    ("Forecast GDP", "India's GDP Over Time", "Actual vs Predicted GDP", "GitHub Repository")
)

# Home section
if navigation == "Forecast GDP":
    forecast()

# India's GDP Analysis section
elif navigation == "India's GDP Over Time":
    gdp_over_time()

# Prediction for 2024 section
elif navigation == "Actual vs Predicted GDP":
    actual_vs_predicted_gdp()

# GitHub Repository section
elif navigation == "GitHub Repository":
    st.title("GitHub Repository")
    st.write("[Click here to visit the GitHub repository](https://github.com/neuraledgeai/India_GDP_Forecasting_Project)")
