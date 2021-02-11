import pickle
from get_stats import get_stats
from collections import defaultdict
import streamlit as st
import pandas as pd
import numpy as np
from broizer import search_desc

import warnings

warnings.filterwarnings('ignore')


st.title('Magical Beer BRO')

st.markdown(' ## Beer Review Organizer')
st.markdown(' ### Type a stereotypical description of your beer and see if the machine learning models can predict your beer!')
desc = st.text_area('Write a description or review of your beer. Be descriptive!')

test_df = search_desc(desc)




# with open('f3.pickle', 'rb') as to_read:
#     forest3b = pickle.load(to_read)
with open('beer_project/web_app/pkl_models/knn3b.pickle', 'rb') as to_read:
    knn3b = pickle.load(to_read)
with open('beer_project/web_app/pkl_models/mnb3b.pickle', 'rb') as to_read:
    mnb3b = pickle.load(to_read)
with open('beer_project/web_app/pkl_models/svc3b.pickle', 'rb') as to_read:
    svc3b = pickle.load(to_read)
with open('beer_project/web_app/pkl_models/xgb3b.pickle', 'rb') as to_read:
    xgb3b = pickle.load(to_read)


# test_df = get_stats()
def predictor(test_df):
    preds = [knn3b.predict(test_df)[0], #mnb3b.predict(test_df)[0],\
             svc3b.predict(test_df)[0], xgb3b.predict(test_df)[0]] #forest3b.predict(test_df)[0]]
    clean_pred = defaultdict(int)
    for pred in preds:
        if pred == 'Pale Ales and Lagers':
            clean_pred['Pale Ales and Lagers'] += 1
        elif pred == 'Strong/Dark Ales':
            clean_pred['Strong/Dark Ales'] += 1
        elif pred == 'Other (Sours, Wild, Holiday styles)':
            clean_pred['Other (Sours, Wild, Holiday styles)'] += 1
        else:
            clean_pred['Other'] += 1
    res_dic = dict(clean_pred)
    max_vote = max(res_dic.items(), key=lambda x: x[1])[0]
    return str(max_vote)
    """for key, value in res_dic.items():
        if value == len(preds) // 2:
            return("TIE")
            break
        elif value > len(preds) / 2:
            return(key)
        else:
            continue"""
button = st.button('Guess!')
if button:
    st.markdown("## Oh I know that beer! It's a: \n")
    st.markdown("# " + predictor(test_df))
    if predictor(test_df) == 'Pale Ales and Lagers':
        st.image('ipa_img.jpg', use_column_width=True)
    if predictor(test_df) == 'Strong/Dark Ales':
        st.image('stout_img.jpg', use_column_width=True)
    if predictor(test_df) == 'Other (Sours, Wild, Holiday styles)':
        st.image('gose_img.jpg', use_column_width=True)



