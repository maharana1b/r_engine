import pandas as pd
import streamlit as st
import pickle
from iteration_utilities import unique_everseen
from iteration_utilities import duplicates

nav = st.sidebar.selectbox(
'PLEASE SELECT WHAT YOU ARE LOOKING FOR',
["HOME","JOB","HIGHER STUDIES"])

if nav == "HOME":
    st.image("inno.jpg")
    st.markdown(
        """ <h1 align="Center"><font face="Garamond" color="#4863A0"><b>CARRIER  RECOMMENDATION SYSTEM</b></font></h1>""",
        True)
#@@@@@@@@ SETTING JOB PAGE
if nav == "JOB":
    st.image("image.jpg", width=100)
    st.markdown(
        """ <h2 align="Left"><font face="Times New Roman" color="#4863A0">Job Recommendation System<b></b></font></h2>""",
        True)
    
    def recommend(job_name):
        job_index = job1[job1['INPUT'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1

    def recommend_ug(job_name):
        job_index = job1[job1['UG'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1


    def recommend_spe(job_name):
        job_index = job1[job1['SPECIALIZATION'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1

    def recommend_inti(job_name):
        job_index = job1[job1['INTERESTS'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1

    job_list = pickle.load(open('job.pkl', 'rb'))
    job1 = pd.DataFrame(job_list)
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    UG1 = set(job1['UG'].values)
    selected_ug = st.selectbox(
        'Please select your Under Graduate Programme',
        UG1)

    SPEC1 = set(job1['SPECIALIZATION'].values)
    selected_Specialization = st.selectbox(
        'Please select your specialization',
        SPEC1)


    SPEC2 = set(job1['INPUT'].values)

    key_skill = st.multiselect('Select Your Skills', SPEC2)
    skill = pd.Series(key_skill)
    skill_1 = skill.values
    container = st.container()

    SPEC3 = set(job1['INTERESTS'].values)
    INTERESTS = st.multiselect('Select Your Interests', SPEC3)
    interest = pd.Series(INTERESTS)
    skill_2 = interest.values

    if st.button('Recommend'):
        recommendation = []

        for i in skill_1:
            recommendation.extend(recommend(i))

        for i in skill_2:
            recommendation.extend(recommend_inti(i))
        recommendation.extend(recommend_ug(selected_ug))
        recommendation.extend(recommend_spe(selected_Specialization))
        result = pd.DataFrame(unique_everseen(duplicates(recommendation)))
        result = result.rename(columns={0:"Recommended Jobs for you"})

        st.write(result[1:16])
#@@@@@@@@ SETTING HIGHER STUDIES PAGE
if nav == "HIGHER STUDIES":
    st.image("image.jpg",width=100)
    st.markdown(
        """ <h2 align="Left"><font face="Times New Roman" color="#4863A0"><font size = "6"><b>Higher Studies Recommendation System</b></font></h2>""",
        True)
    def recommend(higher_studies):
        pg_index = pg[pg['INPUT'] == higher_studies].index[0]
        distances = similarity[pg_index]
        pg_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_studies = []
        for i in pg_list:
            recommended_studies.append(pg.iloc[i[0]].PG)
        recommended_studies1 = set(recommended_studies)
        return recommended_studies1


    def recommend_UG(higher_studies):
        pg_index = pg[pg['UG'] == higher_studies].index[0]
        distances = similarity[pg_index]
        pg_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_studies = []
        for i in pg_list:
            recommended_studies.append(pg.iloc[i[0]].PG)
        recommended_studies1 = set(recommended_studies)
        return recommended_studies1


    def recommend_Spec(higher_studies):
        pg_index = pg[pg['SPECIALIZATION'] == higher_studies].index[0]
        distances = similarity[pg_index]
        pg_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_studies = []
        for i in pg_list:
            recommended_studies.append(pg.iloc[i[0]].PG)
        recommended_studies1 = set(recommended_studies)
        return recommended_studies1


    pg_dict = pickle.load(open('pg_dict.pkl', 'rb'))
    pg = pd.DataFrame(pg_dict)
    similarity = pickle.load(open('similarity_pg.pkl', 'rb'))


    UG1 = set(pg['UG'].values)
    key_ug = st.selectbox('Select your Under Graduate', UG1)

    Spec1 = set(pg['SPECIALIZATION'].values)
    key_spec = st.selectbox('Select your Stream', Spec1)

    interests = set(pg['INTERESTS'].values)
    key_interest = st.multiselect('Select Your Interests', interests)
    interest = pd.Series(key_interest)
    interests = interest.values

    if st.button('Recommend'):
        recommendation1 = []
        for i in interests:
            recommendation1.extend(recommend(i))

        recommendation1.extend(recommend_UG(key_ug))
        recommendation1.extend(recommend_Spec(key_spec))

        result1 = pd.DataFrame(unique_everseen(duplicates(recommendation1)))
        result1 = result1.rename(columns={0:"PG streams Recommended for you"})
        st.write(result1)
