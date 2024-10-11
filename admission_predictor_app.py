import streamlit as st
import pickle
import numpy as np
import webbrowser

# Importing Model
model = pickle.load(open('model.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))

st.title('Admission Acceptance Predication')

gre = st.number_input('GRE Scores ( out of 340 )',min_value=float(50), max_value=float(340))
toefl = st.number_input('TOEFL Scores ( out of 120 )',min_value=float(60), max_value=float(120))
univ_rating = st.number_input('University Rating ( out of 5 )',min_value=float(1), max_value=float(5))
sop = st.number_input('Statement of Purpose -(SOP) Strength ( out of 5 )',min_value=float(1), max_value=float(5))
lor = st.number_input('Letter of Recommendation-(LOR) Strength ( out of 5 )',min_value=float(1), max_value=float(5))
cgpa = st.number_input('Undergraduate GPA-CGPA ( out of 10 )',min_value=float(1), max_value=float(10))
research = st.selectbox('Research Experience ( either Yes or No )',['Yes','No'])

if st.button('Predict Admission Acceptance'):

    pass

    if research == 'Yes':
       research = 1 
    else:
       research = 0    

    query = np.array([gre,toefl,univ_rating,sop,lor,cgpa,research])   

    query = query.reshape(1,-1)[0]   
     
    st.title('The propability of Admission Acceptance is ' + str(f'{model.predict([query])[0]*100:0.2f}%'))

    
 