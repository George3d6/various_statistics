import pandas as pd 
from scipy.stats import spearmanr, pearsonr


sal = pd.read_csv('data_europe.csv', names=['Country', 'Salary (USD)'])
pct = pd.read_csv('ict_pct.csv')

arr_map = []
for country in sal['Country']:
    if country in list(pct['Country']):
        arr_map.append({
                'pct': list(pct.loc[pct['Country'] == country]['pct'])[0]
                ,'salary': list(sal.loc[sal['Country'] == country]['Salary (USD)'])[0]
                ,'country': country
            })
    
df = pd.DataFrame(arr_map)
print(df)
print(pearsonr(list(df['pct']), list(df['salary'])))
print(spearmanr(list(df['pct']), list(df['salary'])))
