import pickle
from get_stats import get_stats
from collections import defaultdict
import streamlit as st
import pandas as pd
import numpy as np

import warnings

warnings.filterwarnings('ignore')

hop_list = ['Challenger','Citra',
 'Warrior',
 'Cascade',
 'Saaz',
 'Azacca',
 'Columbus',
 'Magnum',
 'Perle',
 'Simcoe',
 'Amarillo',
 'Cashmere',
 'Comet',
 'Galaxy',
 'Apollo',
 'Willamette',
 'Goldings',
 'Hellertau',
 'Fuggles',
 'Nugget',
 'Hop Shot',
 'Tettnanger',
 'Mosaic',
 "Brewer's Gold",
 'Northern Brewer',
 'Centennial',
 'Chinook',
 'Crystal', 'CTZ','Styrian Golding','Idaho 7','Nelson Sauvin','Experimental','Hallertau Mittelfrau','Noble Hops']

yeast_list = ['wylon', 'us5', 'us4', 'chico', 'vermont']
st.title('Is this an IPA?')

st.markdown(' ## Can we classify your beer based only on its ingredients?')
st.markdown(' ### Machine learning models will evaluate the hops in your beer and guess if you have an IPA!')
hops = str(st.multiselect("Select all hops in your beer!", hop_list))
dry = st.checkbox("Dry Hopped?")
if dry:
    dryh = 1
else:
    dryh = 0
yeast = st.multiselect("Are any of these yeasts in your beer?", yeast_list)

chal = 0
citra = 0
warrior = 0
casc = 0
saaz = 0
azacca = 0
colum = 0
mag = 0
perle = 0
simcoe = 0
amar = 0
cashmere = 0
comet = 0
galaxy = 0
apollo = 0
willam = 0
goldings = 0
heller = 0
fug = 0
nugg = 0
hopshot = 0
tett = 0
mosaic = 0
brewersg = 0
northb = 0
cent = 0
chinook = 0
crystal = 0
ctz = 0
styr = 0
idaho = 0
nelson = 0
exper = 0
hall = 0
noble = 0
if 'Challenger' in hops:
    chal +=1
if 'Citra' in hops:
    citra +=1
if 'Warrior' in hops:
    warrior += 1
if 'Cascade' in hops:
    casc += 1
if 'Saaz' in hops:
    saaz += 1
if 'Azacca' in hops:
    azacca += 1
if 'Columbus' in hops:
    colum += 1
if 'Magnum' in hops:
    mag += 1
if 'Perle' in hops:
    perle += 1
if 'Simcoe' in hops:
    simcoe += 1
if 'Amarillo' in hops:
    amar += 1
if 'Cashmere' in hops:
    cashmere += 1
if 'Comet' in hops:
    comet += 1
if 'Galaxy' in hops:
    galaxy += 1
if 'Apollo' in hops:
    apollo += 1
if 'Willamette' in hops:
    willam += 1
if 'Goldings' in hops:
    goldings += 1
if 'Hellertau' in hops:
    heller += 1
if 'Fuggles' in hops:
    fug += 1
if 'Nugget' in hops:
    nugg +=1
if 'Hop Shot' in hops:
    hopshot += 1
if 'Tettnanger' in hops:
    tett += 1
if 'Mosaic' in hops:
    mosaic += 1
if "Brewer's Gold" in hops:
    brewersg += 1
if 'Northern Brewer' in hops:
    northb += 1
if 'Centennial' in hops:
    cent += 1
if 'Chinook' in hops:
    chinook += 1
if 'Crystal' in hops:
    crystal +=1
if 'CTZ' in hops:
    ctz += 1
if 'Styrian Golding' in hops:
    styr += 1
if 'Idaho 7' in hops:
    idaho += 1
if 'Nelson Sauvin' in hops:
    nelson += 1
if 'Experimental' in hops:
    exper += 1
if 'Hallertau Mittelfrau' in hops:
    hall += 1
if 'Noble Hops' in hops:
    noble += 1

wylon = 0
us5 = 0
us4 = 0
chico = 0
vermont = 0
if 'wylon' in yeast:
    wylon += 1
if 'us5' in yeast:
    us5 +=1
if 'us4' in yeast:
    us4 +=1
if 'chico' in yeast:
    chico +=1
if 'vermont' in yeast:
    vermont += 1
hopy_array = np.array([chal,citra,warrior,casc,saaz,azacca,colum,mag,perle,simcoe,amar,cashmere,comet,galaxy,apollo,willam,goldings,heller,\
fug,nugg,hopshot,tett,mosaic,brewersg,northb,cent,chinook,crystal,ctz,styr,idaho,nelson,exper,hall,noble, dryh, wylon, us5, us4, chico, vermont])
test_df = pd.DataFrame(hopy_array, index=['chal','citra',
 'warrior',
 'casc',
 'saaz',
 'azacca',
 'colum',
 'mag',
 'perle',
 'simcoe',
 'amar',
 'cashmere',
 'comet',
 'galaxy',
 'apollo',
 'willam',
 'goldings',
 'heller',
 'fug',
 'nugg',
 'hopshot',
 'tett',
 'mosaic',
 'brewerg',
 'northb',
 'cent',
 'chinook',
 'crystal',
 'ctz','styr','idaho','nelson','exper','hall','noble', 'dryh', 'wylon', 'us5', 'us4', 'chico', 'vermont']).T



with open('foresth.pickle', 'rb') as to_read:
    foresth = pickle.load(to_read)
with open('knnh.pickle', 'rb') as to_read:
    knnh = pickle.load(to_read)
with open('logith.pickle', 'rb') as to_read:
    logith = pickle.load(to_read)
with open('bngbh.pickle', 'rb') as to_read:
    bngbh = pickle.load(to_read)
with open('svch.pickle', 'rb') as to_read:
    svch = pickle.load(to_read)
with open('xgbh.pickle', 'rb') as to_read:
    xgbh = pickle.load(to_read)


# test_df = get_stats()
def predictor(test_df):
    preds = [knnh.predict(test_df)[0], bngbh.predict(test_df)[0], logith.predict(test_df)[0],
             foresth.predict(test_df)[0], svch.predict(test_df)[0], xgbh.predict(test_df)[0]]
    clean_pred = defaultdict(int)
    if 1 in np.uint8(preds):
        return 'IPA/Pale Ale'
    else:
        return 'Not IPA'

#    for pred in preds:
#        if pred == 1:
#            clean_pred['IPA/Pale Ales'] += 1
#        elif pred == 0:
#            clean_pred['Not IPA'] += 1
#    res_dic = dict(clean_pred)
#    st.write(res_dic)
#    for key, value in res_dic.items():
#        if value == 3:
#            return("TIE")
#            break
#        elif value > 3:
#            return(key)
#        else:
#            continue

st.markdown("## Based on those ingredients, it seems like you're drinking: \n")
st.markdown("# " + predictor(test_df))
# print(res_dic, preds)



