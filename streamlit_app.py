import streamlit as st
from algorithm import *

st.set_page_config(
    page_title = 'Diabetes Predictor',
    page_icon = '👨🏿‍⚕️',
)

st.title('👨🏿‍⚕️ Diabetes Predictor')

intro = st.container()
calc = st.container()

with intro:
    st.header('Introduction')
    '''
    This is a project I'm doing to apply my understanding of the SVC algorithm and Streamlit. I am not a medical professional, so
    please do not take these results seriously. It is important to note that there are many ethical concerns that result from the 
    intersection of machine learning and health. When determining your risk for any medical condition, it is best to consult a 
    doctor.    
    '''


with calc:
    st.header('Calculator')
    col1, col2 = st.columns([2,1])

    with col1:
        form = st.form("Form")

        with form:
            st.subheader('Input')
            
            Age = st.number_input(
                'Age',
                min_value = 0,
                max_value = 100,
                value = 21
            )
            Sex = st.radio(
                'What is your sex?',
                options = {'Male', 'Female'}
            )
            HighChol = st.radio(
                'Do you have high cholestoral??',
                options = {'Yes', 'No'}
            )
            CholCheck = st.radio(
                'Have you checekd you cholestoral in the past five years?',
                options = {'Yes', 'No'}
            )
            BMIval = st.number_input(
                'BMI',
                min_value = 0,
                max_value = 60,
            )
            Smoker = st.radio(
                'Have you smoked atleast 100 cigarettes in your life?',
                options = {'Yes', 'No'}
            )
            HeartDiseaseorAttack = st.radio(
                'Have you ever been diagnosed with coronary heart disease (CHD) or myocardial infarction (MI)?',
                options = {'Yes', 'No'}
            )
            PhysActivity = st.radio(
                'Have you conducted physical activity in the past 30 days?',
                options = {'Yes', 'No'}
            )
            Fruits = st.radio(
                'Do you consume fruit one or more times a day?',
                options = {'Yes', 'No'}
            )
            Veggies = st.radio(
                'Do you consume vegtables one or more times a day?',
                options = {'Yes', 'No'}
            )

            if Sex == 'Female' or 0:
                alcVal = '7'
            elif Sex == 'Male' or 1:
                alcVal = '14'

            HvyAlcoholConsump = st.radio(
                'Do you consume more than {} drinks per week?'.format(alcVal),
                options = {'Yes', 'No'}
            )
            GenHlth = st.slider(
                'On a scale from 1 to 5 (with 5 being th highest), how would you rate your general health?',
                min_value = 1,
                max_value = 5
            )
            MentHlthBMIval = st.number_input(
                'In the past 30 days, how many day have you had poor mental health?',
                min_value = 0,
                max_value = 30,
            )
            PhysHlth = st.number_input(
                'In the past 30 days, how days have you suffered physical illness or injury?',
                min_value = 0,
                max_value = 30,
            )
            DiffWalk = st.radio(
                'Do you have difficulty walking or climbing stairs?',
                options = {'Yes', 'No'}
            )
            Stroke = st.radio(
                'Have you ever had a stroke?',
                options = {'Yes', 'No'}
            )
            HighBP = st.radio(
                'Do you have high blood pressure?',
                options = {'Yes', 'No'}
            )

            submit = st.form_submit_button('Submit')
        

        
        

    with col2:
        st.subheader('Results')

        if submit:
            pass


