import pandas as pd
import streamlit as st
import numpy as np


time_options = 'Every Time,Most of the time,Rarely,Never'.split(',')
secondary = 'Never,Just a few times,Occassionally,Often,All the time'.split(',')
chores = 'I do it first time,They just ask me a couple of times,They have to remind me a lot,I never do my chores'.split(',')


st.title('Will you get a present from Santa?')

answers = dict()

answers['pleaseandthanks'] = st.radio('How often did you say Please and Thank you?',time_options)
answers['disobey'] = st.radio('How often did you disobey your parents?',secondary)
answers['hugs'] = st.radio('How many times did you hug your parents?',secondary)
answers['sharing'] = st.radio('How many times did you share?',secondary)
answers['chores'] = st.radio('How much do your guardians have to nag to get you to do your chores?',chores)
answers['nice'] = st.radio('How often did you do something nice for your parents, without being asked?',secondary)


if st.button("Let's go", key=None, help=None, on_click=None, args=None, kwargs=None):
  for x,i in answers.items():
  st.text(f'{x} : {i}')
