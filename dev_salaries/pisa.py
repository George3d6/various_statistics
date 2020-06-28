import pandas as pd 
from scipy.stats import spearmanr, pearsonr


sal = pd.read_csv('data_europe.csv', names=['Country', 'Salary (USD)'])
pisa = pd.read_csv('pisa_scores.csv')
pisa = pisa.drop(columns=['Code','Year'])


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
        arr_map.append({
                'pisa': list(pisa.loc[pisa['Country'] == country]['OECD PISA education score'])[0]
                ,'salary': list(sal.loc[sal['Country'] == country]['Salary (USD)'])[0]
                ,'country': country
            })
    
df = pd.DataFrame(arr_map)
print(df)
print(pearsonr(list(df['pisa']), list(df['salary'])))
print(spearmanr(list(df['pisa']), list(df['salary'])))
