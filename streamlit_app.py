import pandas as pd
import streamlit as st
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

options = {'time_options' :'Every Time,Most of the time,Rarely,Never'.split(','),
           'secondary' : 'Never,Just a few times,Occassionally,Often,All the time'.split(','),
           'chores' : 'I do it first time,They just ask me a couple of times,They have to remind me a lot,I never do my chores'.split(',')}

types = {'pleaseandthanks':'time_options',
         'disobey':'secondary',
         'hugs':'secondary',
         'sharing':'secondary',
         'chores': 'chores',
         'nice':'secondary'}

st.title('Will you get a present from Santa?')

answers = dict()

answers['pleaseandthanks'] = st.radio('How often did you say Please and Thank you?',options['time_options'])
answers['disobey'] = st.radio('How often did you disobey your parents?',options['secondary'])
answers['hugs'] = st.radio('How many times did you hug your parents?',options['secondary'])
answers['sharing'] = st.radio('How many times did you share?',options['secondary'])
answers['chores'] = st.radio('How much do your guardians have to nag to get you to do your chores?',options['chores'])
answers['nice'] = st.radio('How often did you do something nice for your parents, without being asked?',options['secondary'])
answers['swearing'] = st.slider('How many times did you swear in 2021?', min_value=0, max_value=1000)

logreg = pickle.load(open('santa.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

if st.button("Let's go", key=None, help=None, on_click=None, args=None, kwargs=None):
    new_data = []

    for k,v in types.items():
        new_list = list('0'*len(options[types[k]]))    
        new_list[options[v].index(answers[k])] = '1'
        new_data = new_data + new_list

    new_data = [int(x) for x in new_data[0]]
  
    new_data = np.array(new_data).reshape(1, -1)
    #result = logreg.predict_proba(new_data) 
    st.text(new_data)
