import pandas as pd
from scipy.stats import spearmanr, pearsonr
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
import numpy as np

def mean_absolute_percentage_error(estimator, X, y_true):
    y_pred = estimator.predict(X)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

sal = pd.read_csv('data_europe.csv', names=['Country', 'Salary (USD)'])
pisa = pd.read_csv('pisa_scores.csv')
pisa = pisa.drop(columns=['Code','Year'])
pppc = pd.read_csv('pppc.csv')
english = pd.read_csv('english.csv')

pisa_avg_map = {}
for i, row in pisa.iterrows():
    if row['Country'] not in pisa_avg_map:
        pisa_avg_map[row['Country']] = []
    pisa_avg_map[row['Country']].append(row['OECD PISA education score'])

for k in pisa_avg_map:
    pisa_avg_map[k] = sum(pisa_avg_map[k])/len(pisa_avg_map[k])

pisa_avg_arr = [{'Country':k,'OECD PISA education score':v} for k, v in pisa_avg_map.items()]

pisa = pd.DataFrame(pisa_avg_arr)
#pisa = pisa.loc[pisa['Year'] == 2012]



# Pandas join seems broken so
arr_map = []
for country in sal['Country']:
    if country in list(pisa['Country']):
        if country in list(pppc['Country']):
            #if country in list(english['Country']):
            arr_map.append({
                    'salary': list(sal.loc[sal['Country'] == country]['Salary (USD)'])[0]
                    ,'pisa': list(pisa.loc[pisa['Country'] == country]['OECD PISA education score'])[0]
                    ,'country': country
                    ,'pppc': list(pppc.loc[pppc['Country'] == country]['2012'])[0]
                    #,'english': list(english.loc[english['Country'] == country]['English'])[0]
                })

df = pd.DataFrame(arr_map)

Y = np.array(df['pisa'])
X = np.array([ [x['pppc']] for i, x in df.iterrows() ])
#X = np.array([ [x['pppc'], x['pisa']] for i, x in df.iterrows() ])
#X = np.array([ [x['pppc'], x['pisa'], x['english']] for i, x in df.iterrows() ])

model = LinearRegression()
#model = GradientBoostingRegressor(learning_rate=0.1,n_estimators=200)
#model = DecisionTreeRegressor()
#model = MLPRegressor(hidden_layer_sizes=(200,))


score = cross_val_score(model, X, Y, cv=4, scoring=mean_absolute_percentage_error).mean()
print(score)
