import pickle
from get_stats import get_stats
from collections import defaultdict

import pandas as pd
import numpy as np
from broizer import search_desc
from scipy import stats


with open('f3.pickle', 'rb') as to_read:
    forest3b = pickle.load(to_read)
with open('knn3b.pickle', 'rb') as to_read:
    knn3b = pickle.load(to_read)
with open('mnb3b.pickle', 'rb') as to_read:
    mnb3b = pickle.load(to_read)
with open('svc3b.pickle', 'rb') as to_read:
    svc3b = pickle.load(to_read)
with open('xgb3b.pickle', 'rb') as to_read:
    xgb3b = pickle.load(to_read)

with open('x_test.pickle','rb') as to_read:
    x_test = pickle.load(to_read)
with open('y_test.pickle', 'rb') as to_read:
    y_test = pickle.load(to_read)



def predictor(test_df):
    full_pred = []
    """preds = [knn3b.predict(test_df)[0], mnb3b.predict(test_df)[0],\
             forest3b.predict(test_df)[0], svc3b.predict(test_df)[0], xgb3b.predict(test_df)[0]]
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
        max_vote = max(res_dic.items(), key=lambda x: x[1])
        full_pred.append(max_vote[0])
    return full_pred"""
    preds = [knn3b.predict(test_df), mnb3b.predict(test_df), \
             forest3b.predict(test_df), svc3b.predict(test_df), xgb3b.predict(test_df)]
    preds_np = np.array(preds).reshape(-1,5)
    preds_vote = stats.mode(preds_np, axis = 1)[0]
    return (preds_vote)


y_pred = predictor(x_test)
print(y_pred)


def acc_score(y_pred, y_test):
    for i in range(min(len(y_pred), len(y_test))):
        accs = []
        if y_pred[i] == y_test[i]:
            accs.append(1)
        num_ones = len(accs)
        print(f"len 1s {num_ones}")
        listlen = len(y_test)
        return float(num_ones/listlen)

print(acc_score(y_pred, y_test))


