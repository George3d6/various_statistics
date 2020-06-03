import pandas as pd 
from scipy.stats import spearmanr, pearsonr


sal = pd.read_csv('data_europe.csv', names=['Country', 'Salary (USD)'])
pct = pd.read_csv('e.csv')

arr_map = []
for country in sal['Country']:
    if country in list(pct['Country']):
        arr_map.append({
                'pct': list(pct.loc[pct['Country'] == country]['English'])[0]
                ,'salary': list(sal.loc[sal['Country'] == country]['Salary (USD)'])[0]
                ,'country': country
            })
    
df = pd.DataFrame(arr_map)
print(df)
print(pearsonr(list(df['pct']), list(df['salary'])))
print(spearmanr(list(df['pct']), list(df['salary'])))

dict_keys(['explained_variance', 'r2', 'max_error', 'neg_median_absolute_error', 'neg_mean_absolute_error', 'neg_mean_squared_error', 'neg_mean_squared_log_error', 'neg_root_mean_squared_error', 'neg_mean_poisson_deviance', 'neg_mean_gamma_deviance', 'accuracy', 'roc_auc', 'roc_auc_ovr', 'roc_auc_ovo', 'roc_auc_ovr_weighted', 'roc_auc_ovo_weighted', 'balanced_accuracy', 'average_precision', 'neg_log_loss', 'neg_brier_score', 'adjusted_rand_score', 'homogeneity_score', 'completeness_score', 'v_measure_score', 'mutual_info_score', 'adjusted_mutual_info_score', 'normalized_mutual_info_score', 'fowlkes_mallows_score', 'precision', 'precision_macro', 'precision_micro', 'precision_samples', 'precision_weighted', 'recall', 'recall_macro', 'recall_micro', 'recall_samples', 'recall_weighted', 'f1', 'f1_macro', 'f1_micro', 'f1_samples', 'f1_weighted', 'jaccard', 'jaccard_macro', 'jaccard_micro', 'jaccard_samples', 'jaccard_weighted'])
