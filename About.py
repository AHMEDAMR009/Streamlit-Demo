import streamlit as st
import pandas as pd

st.title("About")

st.info("This is a test")

st.success("This is a test")

name = st.text_input("Enter your name")

age = st.number_input("Enter yor age")

height = st.slider("Enter your height", min_value=0, max_value=200,value=100,step=10)

#def get_data():
 #   return pd.DataFrame(("name":[name] , "age" :[age],"height":[height]))

#dic= ('name':name , 'age' :age,'height':height)
#df = pd.dataframe(dic,index=[0])
#st.write(df)