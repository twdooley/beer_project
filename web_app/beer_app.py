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
st.markdown(' ### :point_left: Check the sidebar for more details!')
st.markdown(' ### All variables set to default mean values.')
ogi = st.slider(key='OG', label="Original Gravity", min_value=1.00, max_value=1.10, step=0.001, value = 1.063)
fgi = st.slider(key='FG', label="Final Gravity", min_value=1.00, max_value=1.10, step=0.001, value = 1.014)
abvi = st.slider(key='ABV', label="ABV", min_value=0.0, max_value=15.0, step=0.01, value = 6.23)
srmi = st.slider(key='SRM', label="SRM", min_value=0.0, max_value= 100.0, step=1.0, value = 13.5)
ibui = st.slider(key='IBU', label="IBU", min_value=0.0, max_value=120.0, step=1.0, value = 44.0)
hopi = st.slider(key='hop', label="How Complex is the Hop Profile?", min_value=0.0, max_value=10.0, step=0.25, value = 2.5) * 15

bugui = float(ibui / ((ogi - .999999999) * 1000))
beer_array = np.array([ogi, fgi, abvi, srmi, ibui, bugui, hopi])
test_df = pd.DataFrame(beer_array, index=['og', 'fg', 'abv', 'srm', 'ibu', 'bugu', 'hopcmp']).T

break_line = '<hr style="border:2px solid gray"> </hr>'

st.sidebar.markdown("### Background")
st.sidebar.markdown("This project was built from over 27,000 homebrewer recipes on BrewersFriend.com.  \
    The idea was to crowdsource what makes certain styles a style beyond just the marketing mumbo jumbo we get on our bottles. \
        Tim Dooley created me! You can find him on [GitHub](https://github.com/twdooley), [LinkedIn](https://www.linkedin.com/in/timothy-dooley-phd/), \
            and his own personal website https://timdooley.com where a write up about thsi project can be found!")
st.sidebar.markdown(break_line, unsafe_allow_html = True)
st.sidebar.markdown("### Key to Sliders")
st.sidebar.markdown("Beer is a complex thing! What you see here are more complex numerical ways to think about beer!  \
    All quantities are set to the global average of the 27,000 recipes.")
st.sidebar.markdown("* Original Gravity: You will sometimes see this on the bottle. It is the amount of sugar that the beer starts with \
    before yeast is pitched. You can read about it here [Wiki: Beer Gravity](https://en.wikipedia.org/wiki/Gravity_(alcoholic_beverage)#Original_gravity_(OG);_original_extract_(OE))")
st.sidebar.markdown("* Final Gravity: As above but after all is said and done in fermentation. How much sugar is left over? Leave default if not sure.")
st.sidebar.markdown("* ABV, Alcohol by Volume. You know this one! Turns out how much alcohol in a beer really matters for style!")
st.sidebar.markdown("* SRM, Standard Reference Method. What color is your beer? [Wiki: SRM](https://en.wikipedia.org/wiki/Standard_Reference_Method)")
# st.sidebar.image("app_pics/srm_pic.png") # this was for local testing
st.sidebar.image("/app/beer_project/web_app/app_pics/srm_pic.png")

st.sidebar.markdown("* IBU, International Bittering Units. How bitter is this beer? 0 water to 100+ super bitter. [Wiki: IBU](https://en.wikipedia.org/wiki/Beer_measurement#Bitterness)")
st.sidebar.markdown("* Hop Complexity. This ones a bit of a judgement call. On a scale of 0-10, how many different hops go into this beer? Just one? Around 0-3. A bunch, 9-10!")


# with open('forest3.pickle', 'rb') as to_read:
#     forest3 = pickle.load(to_read)
# with open('forest3op.pickle', 'rb') as to_read:
#     forest3op = pickle.load(to_read)
with open('/app/beer_project/web_app/knn3.pickle', 'rb') as to_read:
    knn3 = pickle.load(to_read)
# with open('mnb3.pickle', 'rb') as to_read:
#    mnb3 = pickle.load(to_read)
with open('/app/beer_project/web_app/logr3.pickle', 'rb') as to_read:
    logr3 = pickle.load(to_read)
with open('/app/beer_project/web_app/xgb3.pickle', 'rb') as to_read:
    xgb3 = pickle.load(to_read)


# test_df = get_stats()
def predictor(test_df):
    preds = [knn3.predict(test_df)[0], logr3.predict(test_df)[0],
             xgb3.predict(test_df)[0], xgb3.predict(test_df)[0]] #forest3op.predict(test_df)[0], forest3.predict(test_df)[0] mnb3.predict(test_df)[0],
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
    if 'Lager/Cream Ale' in res_dic.keys():
        return('Lager/Cream Ale')
    else:
        for key, value in res_dic.items():
            # if key == 'Lager/Cream Ale':
            #     return('Lager/Cream Ale')

            #     # if value >= 2:
            #     #break
            #     # else:
            #     #     continue
            # # elif value ==  2: #len(preds) //
            # #     return("Mmm.. that could be a few things, keep sliding.")
            # #     break
            if value >= 2:
                return(key)
            else:
                continue

st.markdown("## Oh, I know! You're drinking \n")
st.markdown("# " + predictor(test_df))
if predictor(test_df) == 'IPA/Pale Ales':
    st.image('/app/beer_project/web_app/ipa_img.jpg', use_column_width=True)
if predictor(test_df) == 'Strong/Dark Ales':
    st.image('/app/beer_project/web_app/stout_img.jpg', use_column_width=True)
if predictor(test_df) == 'Lager/Cream Ale':
    st.image('/app/beer_project/web_app/lager_img.jpg', use_column_width=True)
# print(res_dic, preds)



