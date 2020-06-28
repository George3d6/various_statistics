import pandas as pd
from scipy.stats import spearmanr, pearsonr


sal = pd.read_csv('data_europe.csv', names=['Country', 'Salary (USD)'])
stim = pd.read_csv('stimulants_2.csv')

# Pandas join seems broken so
arr_map = []
for country in sal['Country']:
    if country in list(stim['Country']):
        arr_map.append({
                'stim_usg': list(stim.loc[stim['Country'] == country]['Pct_last_year'])[0]
                ,'salary': list(sal.loc[sal['Country'] == country]['Salary (USD)'])[0]
                ,'country': country
            })

df = pd.DataFrame(arr_map)
print(df)
print(pearsonr(list(df['stim_usg']), list(df['salary'])))
print(spearmanr(list(df['stim_usg']), list(df['salary'])))
