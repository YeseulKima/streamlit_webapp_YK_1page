import streamlit as st
import numpy as np
import pandas as pd
import joblib
import sksurv
class MultiPage: 
    def __init__(self) -> None:
        self.pages = []
    
    def add_page(self, title, func) -> None: 
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

patient_num = 0
def increase_numPatient():
    global patient_num
    patient_num += 1
    return patient_num

numPatient = 0
def increment_counter():
    st.session_state.count += 1
def PFS_app():
    #global patient_num
    sample_test = None
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
    def add_new_sample(new_sample_df):
        if st.session_state.sample_df is None:
            st.session_state.sample_df = new_sample_df
        else:
            st.session_state.sample_df = pd.concat([st.session_state.sample_df , new_sample_df])
    # Load trained model.
    #m = joblib.load('sample_RSF_14feats.pkl')

    if 'numPatient' not in st.session_state:
        st.session_state["numPatient"] = 0
    def increment_counter():
        global numPatient
        numPatient +=1
        st.session_state.numPatient += 1

    if 'sample_df' not in st.session_state:
        st.session_state.sample_df = None


    sample_df = None
    st.subheader('1. Add & Check input infos!')
    st.write(': No. patient = ', st.session_state.numPatient)
    col1, col2= st.columns([5,1])

    # Load input features.
    st.sidebar.title('Insert patient infos!', )

    #with st.sidebar.expander("1. Biometric factors"): #Expander on sidebar is not supported yet.
    Age = st.sidebar.slider('1) Age', 10, 100)
    Sex = st.sidebar.radio('2) Sex', (0, 1))
    Pathology = st.sidebar.radio('3) Pathology', (0,1,2))
    Meta = st.sidebar.radio('4) Metastasis extent', (0,1,2,3))
    ALC_pre_IO = st.sidebar.slider('5) ALC_pre_IO', 0.0, 4.0)
    PRT_EQD2 = st.sidebar.slider('6) PRT EQD2', 10, 70)
    PRT_fractional_dose = st.sidebar.slider('7) PRT fractional dose', 10, 3000)
    PRT_modality = st.sidebar.radio('8) PRT modality', (1,2,3))
    PRT_PTV = st.sidebar.slider('9) PRT PTV', 0, 5000)
    RT_induced_Lymphopenia = st.sidebar.radio('10) RIL', (0,1))
    Baseline_TLC = st.sidebar.slider('11) Baseline TLC', 0, 5)
    BrainRT = st.sidebar.radio('12) Brain RT', (0,1))
    BoneRT = st.sidebar.radio('13) Bone RT', (0,1))
    Irradiated_tumor_burden = st.sidebar.radio('14) Irradiated tumor burden', (1,2,3,4))

    new_sample = pd.DataFrame({'Patient No.':[st.session_state.numPatient],
                                'Age': [Age], 'Sex': [Sex], 'Pathology': [Pathology],
                                'Metastasis_extent': [Meta], 'ALC_pre_IO': [ALC_pre_IO], 'PRT_EQD2': [PRT_EQD2],
                                'PRT_fractional_dose': [PRT_fractional_dose], 'PRT_modality': [PRT_modality],
                                'PRT_PTV': [PRT_PTV],
                                'RT_induced_Lymphopenia': [RT_induced_Lymphopenia],
                                'Baseline_TLC': [Baseline_TLC],
                                'BrainRT': [BrainRT],
                                'BoneRT': [BoneRT], 'Irradiated_tumor_burden': [Irradiated_tumor_burden]})
    with col1:
        st.dataframe(new_sample)
    with col2:
        if st.button('ADD'):
            st.session_state["numPatient"] += 1

            msg = 'Successfully added! ' + str(st.session_state["numPatient"]-1)  # str(st.session_state.numPatient)
            st.success(msg)

            add_new_sample(new_sample)
            #st.write(str(len(st.session_state.sample_df)))

    st.dataframe(st.session_state.sample_df)

    if "items" not in st.session_state:
        st.session_state["items"] = 0

    out_col1, out_col2, out_col3 = st.columns([1, 0.01, 3])
    with out_col1:
        st.subheader('2. Show an individual PFS prediction.')
        if st.button('ADDED'):
            st.session_state["items"] += 1
        st.write(str(st.session_state["items"]))
    with out_col3:
        st.subheader('3. Show multiple PFS predictions.')


st.set_page_config(layout="wide", page_title='Meningioma Prediction', page_icon='🧠')
# Overall structure.
col1,  col2, col3 = st.columns([2,0.8,4])
with col1:
    st.write('Hello')
    #st.image('sample_logo_v1res600.png', width=200) #catholicNsnuh_logo_v1 #, col3
with col3:
    st.title('Meningioma perfect prediction')
    disclaimer = '<p style="font-family:sans-serif; color:Black; font-size: 18px;">* Disclaimer! "This application is for an academic use only!"<br> \
                                                                                * paper DOI: TO.BE.ADDED.<br> \
                                                                                * Contact e-mail: yeseulkim6393@gmail.com <br> \
                                                                                * Cite this paper: ?? 넣을까요? </p>'
    st.markdown(disclaimer, unsafe_allow_html=True)

page = st.selectbox('How do you want to find data?',
                                    ['overall', 'PFS'])

if page == 'overall':
    overall_app()
else:
    PFS_app()

