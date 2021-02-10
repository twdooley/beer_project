import pickle
from get_stats import get_stats
from collections import defaultdict
import streamlit as st
import pandas as pd
import numpy as np

import warnings

warnings.filterwarnings('ignore')

st.title('Beer Classifier')

st.markdown(' ## What Type of Beer am I Drinking?')
st.markdown(' ### All variables set to default mean values.')
ogi = st.slider(key='OG', label="Original Gravity", min_value=1.00, max_value=1.10, step=0.001, value = 1.063)
fgi = st.slider(key='FG', label="Final Gravity", min_value=1.00, max_value=1.10, step=0.001, value = 1.014)
abvi = st.slider(key='ABV', label="ABV", min_value=0.0, max_value=15.0, step=0.01, value = 6.23)
srmi = st.slider(key='SRM', label="SRM", min_value=0.0, max_value= 100.0, step=1.0, value = 13.5)
ibui = st.slider(key='IBU', label="IBU", min_value=0.0, max_value=120.0, step=1.0, value = 44.0)
hopi = st.slider(key='hop', label="How Complex is the Hop Profile?", min_value=0.0, max_value=150.0, step=1.0, value = 35.0)

bugui = float(ibui / ((ogi - .999999999) * 1000))
beer_array = np.array([ogi, fgi, abvi, srmi, ibui, bugui, hopi])
test_df = pd.DataFrame(beer_array, index=['og', 'fg', 'abv', 'srm', 'ibu', 'bugu', 'hopcmp']).T



with open('forest3.pickle', 'rb') as to_read:
    forest3 = pickle.load(to_read)
with open('forest3op.pickle', 'rb') as to_read:
    forest3op = pickle.load(to_read)
with open('knn3.pickle', 'rb') as to_read:
    knn3 = pickle.load(to_read)
with open('mnb3.pickle', 'rb') as to_read:
    mnb3 = pickle.load(to_read)
with open('logr3.pickle', 'rb') as to_read:
    logr3 = pickle.load(to_read)
with open('xgb3.pickle', 'rb') as to_read:
    xgb3 = pickle.load(to_read)


# test_df = get_stats()
def predictor(test_df):
    preds = [knn3.predict(test_df)[0], mnb3.predict(test_df)[0], logr3.predict(test_df)[0],
             forest3op.predict(test_df)[0], forest3.predict(test_df)[0], xgb3.predict(test_df)[0],
             xgb3.predict(test_df)[0]]
    clean_pred = defaultdict(int)
    for pred in preds:
        if pred == 'IPA/Pale Ales':
            clean_pred['IPA/Pale Ales'] += 1
        elif pred == 'Strong/Dark Ales':
            clean_pred['Strong/Dark Ales'] += 1
        elif pred == 'Lager/Cream Ale':
            clean_pred['Lager/Cream Ale'] += 1
        else:
            clean_pred['Other'] += 1
    res_dic = dict(clean_pred)
    for key, value in res_dic.items():
        if key == 'Lager/Cream Ale':
            if value >= 2:
                return('Lager/Cream Ale')
                break
            else:
                continue
        elif value == len(preds) // 3:
            return("TIE")
            break
        elif value > len(preds) / 3:
            return(key)
        else:
            continue

st.markdown("## Oh, I know! You're drinking \n")
st.markdown("# " + predictor(test_df))
# print(res_dic, preds)



