import streamlit as st 
import pandas as pd
import numpy as np
import os
from matplotlib import image
import plotly.express as px


st.set_page_config(layout='wide')
page=st.sidebar.selectbox("Pages",("Introduction","Visualization","Prediction"))

if page=="Introduction":
    st.title("Titanic Tragedy Visualization")
    st.subheader("Sudhanshu Rastogi")
    st.write("On April 15, 1912, during her maiden voyage, the widely considered unsinkable"
          " RMS Titanic sank after colliding with an iceberg. Unfortunately, there were not"
           " enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.")
    
    img = image.imread("Titanic.jpg")
    st.image(img)
    col1,col2=st.columns(2)
    with col1:
        github="https://github.com/sudhanshu2198"
        var1=st.write("Github Link: {}".format(github))
    with col2:
        kaggle="https://www.kaggle.com/sudhanshu2198"
        var1=st.write("Kaggle Link: {}".format(kaggle))
elif page=="Visualization":
    data=pd.read_csv("Titanic.csv")

    #Pie Chart
    var=st.selectbox("Pie Chart",("Survived","Class","Sex","Embarked"))
    df=data[var].value_counts()
    fig = px.pie(values=df.values, names=df.index)
    st.plotly_chart(fig)
    
    #Histogram Chart
    var=st.selectbox("Histogram Chart",("Age","No_of_siblings","No_of_parents","Fare"))
    fig = px.histogram(data, x=var)
    st.plotly_chart(fig)
    
    #Bar Plot
    var=st.selectbox("Bar Chart",("Class","Sex","Embarked"))
    df=data.groupby([var,"Survived"])[["Age"]].count().reset_index()
    fig = px.bar(x=df[var], y=df["Age"], color=df["Survived"])
    st.plotly_chart(fig)

    col1,col2=st.columns(2)
    
    var1,var2="Class","Age"
    with col1:
        var1=st.selectbox("Box Plot",("Class","Sex","Embarked"))
    with col2:
        var2=st.selectbox("Box Plot",("Age","Fare"))
    
    #Box Plot
    fig = px.box(data, x=var1, y=var2, color="Survived")
    st.plotly_chart(fig)

    #Tree Map
    df=data.groupby(["Embarked","Class","Sex","Survived"])[["Fare"]].count().reset_index()
    vars = st.multiselect('Choose Variable',["Embarked","Class","Sex","Survived"])
    fig=px.treemap(df,path=vars,values='Fare')
    st.plotly_chart(fig)
else:
    st.error("Prediction Services will functional in future")
    st.title("Survival Prediction")
    with st.form('user_inputs'):
        Embarked=st.selectbox("Point of Departure",('Southampton', 'Cherbourg', 'Queenstown'))
        Class=st.selectbox("Social Status",('Upper', 'Lower', 'Middle'))
        Sex=st.selectbox("Gender of passenger",('male', 'female'))
        No_of_siblings=st.number_input("No of siblings on ship",min_value=0,max_value=4,value=2,step=1)
        No_of_parents=st.number_input("No of parents on ship(include paternal and maternal )",min_value=0,max_value=4,value=2,step=1)
        Fare=st.number_input("Ticket Price",min_value=0.0,max_value=512.0,value=100.0,step=1.0)
        Age=st.number_input("Age of passenger",min_value=0.5,max_value=80.0,value=20.0,step=0.5)
        st.form_submit_button()

