from re import sub
import streamlit as st
import pickle

with open("model","rb") as f:
    model = pickle.load(f)

def predict(gender,age,pclass,fare):
    male = 0
    female = 0
    if gender == "Female":
        female = 1
    else:
        male = 1
    if model.predict([[pclass,age,fare,female,male]])[0]:
        st.success("Passenger survived")
    else:
        st.error("Passenger died")
        

st.title("Titaninc Survival Prediction :ship:")



gender = st.selectbox("Gender",["Male","Female"])



age = st.slider("Age",0,100)

fare = st.number_input("Enter Fare")

pclass = st.radio("Passenger Class",[1,2,3])

submit = st.button("Predict")

if submit:
    predict(gender,age,pclass,fare)