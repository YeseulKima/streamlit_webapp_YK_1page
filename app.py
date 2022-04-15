import streamlit as st
import numpy as np
import pandas as pd
import joblib
from multipage import MultiPage

from pages import PFS_predictions, PRratio_predictions, overall_description
app = MultiPage()
st.set_page_config(layout="wide")

# Overall structure.
col1,  col2, col3 = st.columns([2,0.8,4])
with col1:
    st.image('sample_logo_v1res600.png', width=400) #catholicNsnuh_logo_v1 #, col3
with col3:
    st.title('Meningioma perfect prediction')
    disclaimer = '<p style="font-family:sans-serif; color:Black; font-size: 18px;">* Disclaimer! "This application is for an academic use only!"<br> \
                                                                                * paper DOI: TO.BE.ADDED.<br> \
                                                                                * Contact e-mail: yeseulkim6393@gmail.com <br> \
                                                                                * Cite this paper: ?? 넣을까요? </p>'
    st.markdown(disclaimer, unsafe_allow_html=True)

#st.subheader('Module Navigation,')
# Add all your application here
app.add_page("Overall description of this web calculator.", overall_description.app)
app.add_page("Progression free survival prediction.", PFS_predictions.app)
app.add_page("Progression/Recurrence ratio prediction.", PRratio_predictions.app)
#app.add_page("Progression free survival prediction.", PFS_prediction.app)
#app.add_page("Progression/Recurrence ratio prediction.", PRratio_prediction.app)

# The main app
app.run()

#st.image('./sources/catholicNsnuh_logo_v1.png', width=300) #Images resolution: Lower thatn 1200 pixels (stable res: 1000pixel)

