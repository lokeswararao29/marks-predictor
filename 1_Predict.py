import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Marks Prediction")

data = {
    'Hours': [1,2,3,4,5,6,7,8],
    'Marks': [20,30,40,50,60,70,80,90]
}

df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Marks']

model = LinearRegression()
model.fit(X, y)

hours = st.slider("Study Hours", 0, 12, 5)

if st.button("Predict"):
    prediction = model.predict([[hours]])
    st.success(f"Marks: {round(prediction[0],2)}")