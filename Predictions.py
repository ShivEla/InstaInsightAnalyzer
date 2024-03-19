#All Predictions here
import streamlit as st
from Package import returnAnswer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrice import confusion_matrix,accuracy_score
ans=returnAnswer()
st.header('Predictions!')
if ans=='User Analysis':
    df=pd.read_csv('Instagram(1).csv')
    st.header('Predictions!')
    st.text('The number of Likes for the next post is predicted using the previous post')
    st.text('The data used for the analysis is:')
    st.dataframe(df)
    st.code('import sklearn')
    st.bar_chart(data=df,x='NoHasgtags')
