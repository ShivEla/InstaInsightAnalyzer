import streamlit as st
header=st.container()
dashboard=st.container()
with header:
    st.header('Instagram Analysis!')
    ans=st.radio('Choose option:',['User analysis','Hashtag analysis'])
    if ans=='User analysis':
        st.subheader('User analysis!')
        user=st.text_input('Enter user name:')
        #st.components.html('https://www.google.com')
        st.components.v1.iframe('https://app.powerbi.com/reportEmbed?reportId=79cd1cc6-fb16-4d59-ac0a-c53dfa735b38&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c',width=1000,height=600)
    else:
        st.subheader('Hashtag analysis!')
        hashTag=st.text_input('Enter hash tag:')
    