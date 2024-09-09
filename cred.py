import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))

st.title("Credit card Fraud Detection Model")
input_df=st.text_input('Enter All Required Features Values')
input_df_splited=input_df.split(',')
submit=st.button('Submit')
if submit:

  features=np.asarray(input_df_splited,dtype=np.float64)
  prediction=model.predict(features.reshape(1,-1))
  if prediction[0]==0:
    st.write('Legitimate Transaction')
  else:
    st.write('Fraudalant Transaction')