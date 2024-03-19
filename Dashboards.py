#Connect Dashboards here
import time as t
import streamlit as st
from Package import returnAnswer
ans=returnAnswer()
if ans=='User Analysis':
    def dash1():
        t.sleep(0.5)
        st.components.v1.iframe('')
    def dash2():
        t.sleep(0.5)
        st.components.v1.iframe('')
    def dash3():
        t.sleep(0.5)
        st.components.v1.iframe('')
    def dash4():
        t.sleep(0.5)
        st.components.v1.iframe('')
    st.header('User Analysis!')
    st.sidebar.button('Dashboard 1',on_click=dash1())
    st.sidebar.button('Dashboard 2',on_click=dash2())
    st.sidebar.button('Dashboard 3',on_click=dash3())
    st.sidebar.button('Dashboard 4',on_click=dash4())
else:
    st.header('Hashtag Analysis!')
    t.sleep(1)
    st.components.v1.iframe('')

