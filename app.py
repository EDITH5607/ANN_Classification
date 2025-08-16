import pandas as pd
import numpy as np
import pickle
import streamlit as st
import tensorflow as tf



## loading model
model = tf.keras.models.load_model('model.h5')


##loading scalar,onehotencoder, label_encoder

with open('standard_scaler.pkl', 'rb') as file:
    scalar = pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)
with open('geo_onehot_encoder.pkl','rb') as file:
    onehotencoder_geo = pickle.load(file) 


## Streamlit App
st.title('Customer Churn Prediction.')

#User input 
geography = st.selectbox('Geography',onehotencoder_geo.categories_[0])
gender = st.selectbox("Gender",label_encoder_gender.classes_)
age = st.slider("Age", 18,100)
balance = st.number_input("Balance")
credit_score = st.number_input('credit score')
estimated_salary = st.number_input('Estimated Salary')
tenure =st.slider("Tenure", 0,10)
num_of_products = st.slider("Number of Products",1,4)
has_cr_card = st.selectbox("has Credit Card",[0,1])
is_active_member = st.selectbox("is active member",[0,1])


## Preparing the input data
input_data = pd.DataFrame({
    'CreditScore':[credit_score],
    'Gender':[label_encoder_gender.transform([gender])],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard':[has_cr_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary]
})

## onehot encoding Geography
geo_encoded = onehotencoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded,columns=onehotencoder_geo.get_feature_names_out(['Geography']))

##combine the encoded dataframe with the input data
input_data = pd.concat([input_data.reset_index(drop=True),geo_encoded_df],axis=1)

## scale the input
input_data_scaled = scalar.transform(input_data)

## predict churn
prediction = model.predict(input_data_scaled)
predicted_probability = prediction[0][0]

st.write(f"Churn Probability:{predicted_probability:.3f}")
##comparing the result
if predicted_probability>0.5:
    st.write("The Customer is likely to churn")
else:
    st.write("The Customer is not likely to churn")
