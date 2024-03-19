import time as t
import streamlit as st

header=st.container()
with header:
    st.header('Instagram Post Analysis')
    ans=st.radio('Select option:',['User Analysis','Hashtag Analysis'])
    t.sleep(1)
    if ans=='User Analysis':
        st.subheader('User Analysis!')
        user=st.text_input('Enter User name:')
    else:
        st.subheader('Hashtag Analysis!')
        hashTag=st.text_input('Enter Hashtag name:')

def returnAnswer():
    return ans
        