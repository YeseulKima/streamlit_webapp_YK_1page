import streamlit as st
import numpy as np
import pandas as pd
import joblib
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        self.pages.append(
            {
                "title": title, 
                "function": func
            }
        )

    def run(self):
        # Drodown to select the page to run  
        page = st.selectbox(#st.sidebar.selectbox(
            'Module Navigation, ', #Select the module,
            self.pages, 
            format_func=lambda page: page['title']
        )

        # run the app function 
        page['function']()
        
def overall_app():
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
        
def PFS_app():
    sample_test = None
    patient_num = 0
    new_row = None
    new_df = None
    def change_df():
        sample_test = pd.DataFrame({'Age': [Age], 'Sex': [Sex], 'Pathology': [Pathology],
                                    'Metastasis_extent': [Meta], 'ALC_pre_IO': [ALC_pre_IO], 'PRT_EQD2': [PRT_EQD2],
                                    'PRT_fractional_dose': [PRT_fractional_dose], 'PRT_modality': [PRT_modality],
                                    'PRT_PTV': [PRT_PTV],
                                    'RT_induced_Lymphopenia': [RT_induced_Lymphopenia], 'Baseline_TLC': [Baseline_TLC],
                                    'BrainRT': [BrainRT],
                                    'BoneRT': [BoneRT], 'Irradiated_tumor_burden': [Irradiated_tumor_burden]})
        return sample_test

    def add_newpt(patient_num, sample_test):
        patient_num += 1
        new_row = pd.DataFrame({'Age': [Age], 'Sex': [Sex], 'Pathology': [Pathology],
                                    'Metastasis_extent': [Meta], 'ALC_pre_IO': [ALC_pre_IO], 'PRT_EQD2': [PRT_EQD2],
                                    'PRT_fractional_dose': [PRT_fractional_dose], 'PRT_modality': [PRT_modality],
                                    'PRT_PTV': [PRT_PTV],
                                    'RT_induced_Lymphopenia': [RT_induced_Lymphopenia], 'Baseline_TLC': [Baseline_TLC],
                                    'BrainRT': [BrainRT],
                                    'BoneRT': [BoneRT], 'Irradiated_tumor_burden': [Irradiated_tumor_burden]})
        new_row_df = pd.concat([sample_test, new_row])
        return (patient_num, new_row_df)
    #st.image('./sources/catholicNsnuh_logo_v1.png', width=300) #Images resolution: Lower thatn 1200 pixels (stable res: 1000pixel)
    #sub_title = '<p style="font-family:sans-serif; color:Black; font-size: 27px;">Selected module: <em><strong>Progression free survival</strong></em> prediction</p>'
    #st.markdown(sub_title, unsafe_allow_html=True)

    #st.subheader('Meningioma perfect prediction')

    # Load trained model.
    m = joblib.load('sample_RSF_14feats.pkl')

    # Load input features.
    st.sidebar.title('Insert patient infos!', )

    #with st.sidebar.expander("1. Biometric factors"): #Expander on sidebar is not supported yet.
    Age = st.sidebar.slider('1) Age', 10, 100)
    #st.sidebar.write('1) Age:', Age)

    Sex = st.sidebar.radio('2) Sex', (0, 1))
    #st.sidebar.write('Sex:', Sex)

    Pathology = st.sidebar.radio('3) Pathology', (0,1,2))
    #st.sidebar.write('Pathology:', Pathology)

    Meta = st.sidebar.radio('4) Metastasis extent', (0,1,2,3))
    #st.sidebar.write('Metastasis extent:', Meta)

    ALC_pre_IO = st.sidebar.slider('5) ALC_pre_IO', 0.0, 4.0)
    #st.sidebar.write('TLC before ICT:', ALC_pre_IO)

    PRT_EQD2 = st.sidebar.slider('6) PRT EQD2', 10, 70)
    #st.sidebar.write('PRT EQD2:', PRT_EQD2)

    PRT_fractional_dose = st.sidebar.slider('7) PRT fractional dose', 10, 3000)
    #st.sidebar.write('PRT fractional dose:', PRT_fractional_dose)

    PRT_modality = st.sidebar.radio('8) PRT modality', (1,2,3))
    #st.sidebar.write('PRT modality:', PRT_modality)

    PRT_PTV = st.sidebar.slider('9) PRT PTV', 0, 5000)
    #st.sidebar.write('PRT PTV:', PRT_PTV)

    RT_induced_Lymphopenia = st.sidebar.radio('10) RIL', (0,1))
    #st.sidebar.write('RIL:', RT_induced_Lymphopenia)

    Baseline_TLC = st.sidebar.slider('11) Baseline TLC', 0, 5)
    #st.sidebar.write('Baseline TLC:', Baseline_TLC)

    BrainRT = st.sidebar.radio('12) Brain RT', (0,1))
    #st.sidebar.write('Brain RT:', BrainRT)

    BoneRT = st.sidebar.radio('13) Bone RT', (0,1))
    #st.sidebar.write('Bone RT:', BoneRT)

    Irradiated_tumor_burden = st.sidebar.radio('14) Irradiated tumor burden', (1,2,3,4))
    #st.sidebar.write('Irradiated tumor burden:', Irradiated_tumor_burden)

    # Overall structure.
    st.subheader('>> Add & Check input infos!')
    #st.write('()')
    #with col1:
    '''if st.button('Add'):
        col1, col2, col3 = st.columns([1, 0.1, 10])
        with col1:
            sample_test = pd.DataFrame({'Age': [Age], 'Sex': [Sex], 'Pathology': [Pathology],
                                        'Metastasis_extent': [Meta], 'ALC_pre_IO': [ALC_pre_IO], 'PRT_EQD2': [PRT_EQD2],
                                        'PRT_fractional_dose': [PRT_fractional_dose], 'PRT_modality': [PRT_modality],
                                        'PRT_PTV': [PRT_PTV],
                                        'RT_induced_Lymphopenia': [RT_induced_Lymphopenia], 'Baseline_TLC': [Baseline_TLC],
                                        'BrainRT': [BrainRT],
                                        'BoneRT': [BoneRT], 'Irradiated_tumor_burden': [Irradiated_tumor_burden]})
            st.write('added!')
        with col3:
            st.write('Accumulated patient infos,')
            if sample_test is None:
                st.write('No patient added!')
            else:
                st.dataframe(sample_test)'''
    col1, col2, col3,col4 = st.columns([1, 1, 0.1, 10])
    with col1:
        st.write('')
        if st.button('Add'):
            st.write('Added!')
            sample_test = pd.DataFrame({'Age': [Age], 'Sex': [Sex], 'Pathology': [Pathology],
                                        'Metastasis_extent': [Meta], 'ALC_pre_IO': [ALC_pre_IO], 'PRT_EQD2': [PRT_EQD2],
                                        'PRT_fractional_dose': [PRT_fractional_dose], 'PRT_modality': [PRT_modality],
                                        'PRT_PTV': [PRT_PTV],
                                        'RT_induced_Lymphopenia': [RT_induced_Lymphopenia],
                                        'Baseline_TLC': [Baseline_TLC],
                                        'BrainRT': [BrainRT],
                                        'BoneRT': [BoneRT], 'Irradiated_tumor_burden': [Irradiated_tumor_burden]})
            #sample_test = change_df()
            with col4:
                st.dataframe(sample_test)
            #st.dataframe(sample_test)
        '''if st.button('New'):
            st.write('New added!')
            patient_num, new_df = add_newpt(patient_num, sample_test)
            st.write('pt_num')'''
    with col2:
        st.write('')
        if st.button('Remove'):
            st.write('Removed!')
    with col4:
        st.write('Accumulated patient infos,')
        if sample_test is None:
            st.write('Confirm the new patient!')
        else:
            st.write('See above!')
            #st.datafsrame(sample_test)
            #st.dataframe(new_df)
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
app.add_page("Overall description of this web calculator.", overall_app)
app.add_page("Progression free survival prediction.", PFS_app)
#app.add_page("Progression/Recurrence ratio prediction.", PRratio_predictions.app)
#app.add_page("Progression free survival prediction.", PFS_prediction.app)
#app.add_page("Progression/Recurrence ratio prediction.", PRratio_prediction.app)

# The main app
app.run()

#st.image('./sources/catholicNsnuh_logo_v1.png', width=300) #Images resolution: Lower thatn 1200 pixels (stable res: 1000pixel)

