import streamlit as st
import matplotlib.pyplot as plt
import pylab as pl
from algorithm import *

st.set_page_config(
    page_title = 'Diabetes Predictor',
    page_icon = '👨🏿‍⚕️',
)

st.title('⚕️ Diabetes Predictor')

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
    col1, col2 = st.columns([5,4])

    with col1:
        form = st.form("Form")

        with form:
            st.subheader('Input')
            
            Age = st.number_input(
                'Age',
                min_value = 18,
                max_value = 100,
                value = 18
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

            MentHlth = st.number_input(
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

        def ageg5yr(age):
            if age >= 18 and age <=24:
                return 1
            elif age >= 25 and age <=29:
                return 2
            elif age >= 30 and age <=34:
                return 3
            elif age >= 35 and age <=39:
                return 4
            elif age >= 40 and age <=44:
                return 5
            elif age >= 45 and age <=49:
                return 6
            elif age >= 50 and age <=54:
                return 7
            elif age >= 55 and age <=59:
                return 8
            elif age >= 60 and age <=64:
                return 9
            elif age >= 65 and age <=69:
                return 10
            elif age >= 70 and age <=74:
                return 11
            elif age >= 75 and age <=79:
                return 12
            elif age >= 80:
                return 13

        def val_to_bin(val):
            if val == "No" or "Female":
                return 0
            elif val == "Yes" or "Male":
                return 1

        user_input = pd.DataFrame(
            {
                'Age': ageg5yr(Age), 
                'Sex': val_to_bin(Sex),
                'HighChol': val_to_bin(HighChol),
                'CholCheck': val_to_bin(CholCheck),
                'BMI': BMIval,
                'Smoker': val_to_bin(Smoker),
                'HeartDiseaseorAttack': val_to_bin(HeartDiseaseorAttack),
                'PhysActivity': val_to_bin(PhysActivity),
                'Fruits': val_to_bin(Fruits),
                'Veggies': val_to_bin(Veggies),
                'HvyAlcoholConsump': val_to_bin(HvyAlcoholConsump),
                'GenHlth': GenHlth,
                'MentHlth': MentHlth,
                'PhysHlth': PhysHlth,
                'DiffWalk': val_to_bin(DiffWalk),
                'Stroke': val_to_bin(Stroke),
                'HighBP': val_to_bin(HighBP),
            },index=[0]
        )
        
        if submit:
            if svc.predict(user_input) == [0.]:
                pred = "No"
            elif svc.predict(user_input) == [1.]:
                pred = "Yes"

            st.markdown("**Classification:** {}".format(pred))
            st.markdown("**Likelihood:** {0:.2%}".format(max(svc.predict_proba(user_input)[0])))

