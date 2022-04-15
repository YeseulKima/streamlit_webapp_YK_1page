import streamlit as st
import numpy as np
import pandas as pd
import joblib

def app():
    st.subheader('1. What is meningioma?')
    #st.write('>> 어떤 질병인지, median survival이나 PR ratio 관련 정보?\n 관련 링크 추가?or 위찬우 교수님 논문 DOI 링크?')
    with st.expander("Show me details!"):
        st.write('>> 어떤 질병인지, median survival이나 PR ratio 관련 정보?\n 관련 링크 추가?or 위찬우 교수님 논문 DOI 링크?')

    st.subheader('2. Model description.')
    with st.expander("Show me details!"):
        st.write('>> 모델링 완료 후, overall procedure fig 1 넣기? ')

    st.subheader('3. Endpoints description.')
    with st.expander("Show me details!"):
        PFS_text = '<p style="font-family:sans-serif; color:Black; font-size: 18px;">a. Progression free survival (PFS) prediction </p>'
        st.markdown(PFS_text, unsafe_allow_html=True)
        #st.write('a. Progression free survival (PFS) prediction')
        st.write('>> 정의, sample 설명? ')

        PRratio_text = '<p style="font-family:sans-serif; color:Black; font-size: 18px;">b. Progression/Recurrence (P/R) ratio prediction </p>'
        st.markdown(PRratio_text, unsafe_allow_html=True)
        #st.write('b. Progression/Recurrence (P/R) ratio prediction')
        st.write('>> 정의, sample 설명? ')

    st.subheader('4. Input clinical features description.')
    with st.expander("Show me details!"):
        df =pd.DataFrame({'Input features':['Age', 'Sex'], 'Description':['-------------------어쩌구 저쩌구-----------------------','-------------------어쩌구 저쩌구-----------------------'],
                          'Categories or Values':['-', '0:female / 1:Male'] })
        st.dataframe(df)
