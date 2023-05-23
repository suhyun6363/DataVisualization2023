import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None) # 모든 열을 출력

red_df = pd.read_csv('winequality-red.csv', sep = ';', header = 0, engine = 'python')
white_df = pd.read_csv('winequality-white.csv', sep = ';', header = 0, engine= 'python')

red_df.columns = red_df.columns.str.replace(' ', '_')
white_df.columns = white_df.columns.str.replace(' ', '_')

red_df.insert(0, column = 'type', value = 'red')
white_df.insert(0, column = 'type', value = 'white')


#print(red_df.head(5))
#print(white_df.tail(5))

wine = pd.concat([red_df, white_df])

#print(wine.info())
#print(wine.head(5))
#print(wine.tail(5))
#print(wine.describe())

print(red_df.quality.unique())
print(white_df.quality.unique())

print(red_df['quality'].unique())
print(white_df.quality.value_counts())

from scipy import stats
from statsmodels.formula.api import ols
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality'] #red wine에 대한 quality
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']
stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)
#print(result)
#      Ttest_indResult(statistic = -10.149363059143164, pvalue = 8.168348870049682e-24)
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + \
      residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + \
      density + pH + sulphates + alcohol'   #ols에선 종속변수, 독립변수를 string형태로 받음
#regression_result = ols(Rformula, data = wine).fit()
#print(regression_result.summary())

'''
import numpy as np
sampleNumber = 1000000
korean = np.random.normal(170, 10, sampleNumber)   #평균 170, 표준편차 1 sampleNumber 만큼 뽑기
american = np.random.normal(169, 1, sampleNumber)
result = stats.ttest_ind(korean, american, equal_var = False)
print(result)   #표준편차 차이가 많이 나지만 통계 유의미


data = {"fixed_acidity" : [8.5, 8.1], "volatile_acidity":[0.8, 0.5],
"citric_acid":[0.3, 0.4], "residual_sugar":[6.1, 5.8], "chlorides":[0.055,
0.04], "free_sulfur_dioxide":[30.0, 31.0], "total_sulfur_dioxide":[98.0,
99], "density":[0.996, 0.91], "pH":[3.25, 3.01], "sulphates":[0.4, 0.35],
"alcohol":[9.0, 0.88]}
sample2 = pd.DataFrame(data, columns= wine.columns)     # 두 병의 와인 columns 별로 비교
print(sample2)

sample2_predict = regression_result.predict(sample2)
print(sample2_predict)
'''

#print(wine.describe())
wine = wine.sample(frac=1) # row전체 shuffle white, red 데이터를 섞기 위함
#print(wine)
#print(len(wine) * 0.7) # wine 70% 해당
train_set = wine[0:4548]
test_set = wine[4548:]
regression_result = ols(Rformula, data = train_set).fit()
#print(regression_result.summary())

test_set_predict = regression_result.predict(test_set) #예측한 값
test_set_predict = test_set_predict.round() #반올림
#print(test_set_predict)

ground_true = test_set['quality'] #원래 정답
#print(ground_true)

def calc_accuracy(gt, pred):    # 예측값과 정답 비교
    gt = np.array(gt)
    pred = np.array(pred)
    print(np.mean(gt == pred))

calc_accuracy(ground_true, test_set_predict) #0.5336069779374037 -> 등급을 판정하는 기준에 영향을 안 줌

import matplotlib.pyplot as plt
'''
import seaborn as sns
sns.set_style('dark')
sns.distplot(red_wine_quality, kde = True, color = "red", label = 'red wine')
sns.distplot(white_wine_quality, kde = True, label = 'white wine')
plt.title("Quality of Wine Type")
plt.legend()
plt.show()
'''
import statsmodels.api as sm
fig = plt.figure(figsize = (8, 13))
sm.graphics.plot_partregress_grid(regression_result, fig = fig)
plt.show()









