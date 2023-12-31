import streamlit as st
import pandas as pd
import pickle

# Load your XGBoost model
with open('Water-Quality-Monitoring', 'rb') as f:
    model = pickle.load(f)

# Creating a preprocessor function to handle null values from the user's input
def pre_processors(df):
    cols = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']
    for i in cols:
        mean_value = df[i].mean()  # Fix the typo in this line
        df[i] = df[i].fillna(mean_value)
    return df

st.title('AI Powered Water Quality Monitoring')
ph = st.text_input('pH of Water : ')
Hardness = st.text_input('Hardness of Water: ')
Solids = st.text_input('Amount of solids present in water: ')
Chloramines = st.text_input('Amount of chloramines in water: ')
Sulfate = st.text_input('Amount of sulfate: ')
Conductivity = st.text_input('Conductivity level of water: ')
Organic_carbon = st.text_input('Amount of organic carbon present: ')
Trihalomethanes = st.text_input('Amount of trihalomethane present in water:')
Turbidity = st.text_input('Turbidity:')

if st.button('ANALYSE'):
    # Convert input values to float to ensure compatibility with your model
    input_data = {
        'ph' : float(ph),
        'Hardness' : float(Hardness), 
        'Solids' : float(Solids),
        'Chloramines' : float(Chloramines), 
        'Sulfate' : float(Sulfate), 
        'Conductivity' : float(Conductivity),
        'Organic_carbon' : float(Organic_carbon), 
        'Trihalomethanes' : float(Trihalomethanes), 
        'Turbidity' : float(Turbidity),
    }
    # Create a DataFrame from the user input
    user_input = pd.DataFrame([input_data])
    # Apply the preprocessor function
    user_input = pre_processors(user_input)
    # Make predictions
    result = model.predict(user_input)
    if(result == 0):
        st.success('Safe')
        st.success('No Immediate Action Required!')
    else:
        st.error('Not Safe, Immediate Action Required')
        st.error('1. Immediate Action: Do not use the water for any purpose until the issue is resolved.')
        st.error('2. Contact Authorities: Notify local water authorities or your water supplier about the unsafe water conditions.')
        st.error('3. Water Testing: Arrange for comprehensive water testing to identify the specific contaminants and their levels.')
        st.error('4. Water Treatment: Depending on the test results, follow treatment procedures recommended by experts to make the water safe for consumption and other uses.')
        st.error('5. Regular Monitoring: Implement regular water quality monitoring to prevent future issues and ensure safe, clean water.')
        
    







