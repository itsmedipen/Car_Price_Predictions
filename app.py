# app.py
import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Car Price Prediction App 🚗 ")
st.write("Enter the car details below to predict its price.")

# Numeric inputs
wheelbase = st.number_input("Wheelbase (inches)", value=94.5, max_value=120.9)
carlength = st.number_input("Car Length (inches)", value=144.6, max_value=208.1)
carheight = st.number_input("Car Height (inches)", value=58.3, max_value=59.8)
curbweight = st.number_input("Curb Weight (lbs)", value=3770, max_value=4066)
enginesize = st.number_input("Engine Size (cc)", value=122, max_value=326)
horsepower = st.number_input("Horsepower", value=175, max_value=288)
peakrpm = st.number_input("Peak RPM", value=6000, max_value=6600)
citympg = st.number_input("City MPG", value=37, max_value=49)
highwaympg = st.number_input("Highway MPG", value=53, max_value=54)
carwidth = st.number_input('Car Width', value=70.5, max_value=72.3)
boreratio = st.number_input('Bore Ratio', value=3.62, max_value=3.94)


# Categorical inputs
fueltype = st.selectbox("Fuel Type", ['gas', 'diesel'])
fuelsystem = st.selectbox("Fuel System", ['mpfi', '2bbl', '1bbl', '4bbl', 'idi', 'spdi', 'spfi'])
enginetype = st.selectbox("Engine Type", ['dohc', 'ohcv', 'ohc', 'l', 'rotor'])
doornumber = st.selectbox("Number of Doors", ['two', 'four'])
cylindernumber = st.selectbox("Number of Cylinders", ['two', 'three', 'four', 'five', 'six', 'eight', 'twelve'])
carbody = st.selectbox('Body Type', ['sedan','hatchback','wagon','hardtop','convertible'])
drivewheel = st.selectbox('Number of wheel', ['fwd','rwd','4wd'])
enginelocation = st.selectbox('Engine Location', ['front','rear'])
aspiration = st.selectbox('Aspiration', ['std','turbo'])

# Prepare input data
input_df = pd.DataFrame({
    'wheelbase': [wheelbase],
    'carlength': [carlength],
    'carheight': [carheight],
    'curbweight': [curbweight],
    'enginesize': [enginesize],
    'horsepower': [horsepower],
    'peakrpm': [peakrpm],
    'citympg': [citympg],
    'highwaympg': [highwaympg],
    'fueltype': [fueltype],
    'fuelsystem': [fuelsystem],
    'enginetype': [enginetype],
    'doornumber': [doornumber],
    'cylindernumber': [cylindernumber],
    'carbody': [carbody],
    'drivewheel': [drivewheel],
    'enginelocation': [enginelocation],
    'aspiration': [aspiration],
    'carwidth': [carwidth],
    'boreratio': [boreratio],

})

# Transform and predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Car Price: ${prediction[0]:,.2f}")

