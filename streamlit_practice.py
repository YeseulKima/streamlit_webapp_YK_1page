import streamlit as st
import numpy as np
import pandas as pd
import joblib
# Overall structure.
st.title('Meningioma perfect prediction')

# Load trained model.
m = joblib.load('./sample_RSF_14feats.pkl')

# Load input features.
Age = st.sidebar.slider('Age', 10, 100)
st.sidebar.write('Age:', Age)

Sex = st.sidebar.radio('Sex', (0, 1))
st.sidebar.write('Sex:', Sex)

Pathology = st.sidebar.radio('Pathology', (0,1,2))
st.sidebar.write('Pathology:', Pathology)

Meta = st.sidebar.radio('Metastasis extent', (0,1,2,3))
st.sidebar.write('Metastasis extent:', Meta)

ALC_pre_IO = st.sidebar.slider('ALC_pre_IO', 0.0, 4.0)
st.sidebar.write('TLC before ICT:', ALC_pre_IO)

PRT_EQD2 = st.sidebar.slider('PRT EQD2', 10, 70)
st.sidebar.write('PRT EQD2:', PRT_EQD2)

PRT_fractional_dose = st.sidebar.slider('PRT fractional dose', 10, 3000)
st.sidebar.write('PRT fractional dose:', PRT_fractional_dose)

PRT_modality = st.sidebar.radio('PRT modality', (1,2,3))
st.sidebar.write('PRT modality:', PRT_modality)

PRT_PTV = st.sidebar.slider('PRT PTV', 0, 5000)
st.sidebar.write('PRT PTV:', PRT_PTV)

RT_induced_Lymphopenia = st.sidebar.radio('RIL', (0,1))
st.sidebar.write('RIL:', RT_induced_Lymphopenia)

Baseline_TLC = st.sidebar.slider('Baseline TLC', 0, 5)
st.sidebar.write('Baseline TLC:', Baseline_TLC)

BrainRT = st.sidebar.radio('Brain RT', (0,1))
st.sidebar.write('Brain RT:', BrainRT)

BoneRT = st.sidebar.radio('Bone RT', (0,1))
st.sidebar.write('Bone RT:', BoneRT)

Irradiated_tumor_burden = st.sidebar.radio('Irradiated tumor burden', (1,2,3,4))
st.sidebar.write('Irradiated tumor burden:', Irradiated_tumor_burden)

# Save input features.
sample_test = pd.DataFrame({'Age':[Age], 'Sex':[Sex], 'Pathology':[Pathology],
                          'Metastasis_extent':[Meta], 'ALC_pre_IO':[ALC_pre_IO], 'PRT_EQD2':[PRT_EQD2],
                          'PRT_fractional_dose':[PRT_fractional_dose], 'PRT_modality':[PRT_modality], 'PRT_PTV':[PRT_PTV],
                          'RT_induced_Lymphopenia':[RT_induced_Lymphopenia],'Baseline_TLC':[Baseline_TLC], 'BrainRT':[BrainRT],
                          'BoneRT':[BoneRT], 'Irradiated_tumor_burden':[Irradiated_tumor_burden]})

#st.write(str(sample_test))
#st.write(str(m.estimators_[0]))

preds = m.predict_survival_function(sample_test)[0].y


st.write("Let's test a sample prediction! \n")
st.write(str(preds))

#'Age', 'Sex', 'Pathology', 'Metastasis_extent', 'ALC_pre_IO',
#'PRT_EQD2', 'PRT_fractional_dose', 'PRT_modality', 'PRT_PTV',
#'RT_induced_Lymphopenia', 'Baseline_TLC', 'BrainRT', 'BoneRT',
#'Irradiated_tumor_burden'
