import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing # sklearn에서 보스톤 데이터세트는 더이상 지원하지 않음

import seaborn as sns                                 # 그림 그리기 위해서....
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression    # sklearn  package 에서 제공하는 로지스틱 회기분석 모듈
from sklearn.model_selection import train_test_split   # 학습 데이터와 테스트 데이터 분리를 위해 필요
from sklearn.metrics import mean_squared_error, r2_score             # 선형회기분석에서 성능수치 평가...



california = fetch_california_housing()             # 캘리포니아 집값 데이터세트 불러오기
print(california.keys())                            # sklearn에서 제공하는 데이터세트는 dict와 유사한 bunch라는 데이터타입을 사용함
print(california.DESCR)

california_df = pd.DataFrame(california.data, columns=california.feature_names) # dataframe 형태로 변환
california_df['price'] = california.target # target 에 가격정보 있어 dataframe에 추가
print(california_df.describe())

print(california_df.corr(numeric_only=True))     # 변수가 모두 숫자/연속형 데이터라  numeric_only=True는 필요 없음...
sns.heatmap(california_df.corr(), annot=True)    # heatmap으로 가시화하여 확인
plt.show()

x_data = california_df.drop(['price'], axis='columns')  # 다시 독립변수와 종속변수 분할
y_data = california_df['price']

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=1568)
x_train = np.array(x_train)        #  dataframe  형식을 사용해도 되지만...numpy객체로 변환하였다.
x_test = np.array(x_test)          # model fix()시 dataframe 형식을 사용했다면 predict() 호출 시에도 같은 타입을 입력해야함.
y_train = np.array(y_train)
y_test = np.array(y_test)
#x_train, x_test, y_train, y_test = train_test_split(california.data,california.target, test_size=0.3, random_state=1568)

model = LinearRegression()         # 선형회기 모형 생성
model.fit(x_train, y_train)        # 학습

print('학습 데이터 점수: {}'.format(model.score(x_train, y_train)))  #r-square 값
print('평가 데이터 점수: {}'.format(model.score(x_test, y_test)))

y_predict = model.predict(x_test)                                  #테스트세트를 통한 예측/추정
mse = mean_squared_error(y_test, y_predict)                        #MSE기반 모델 성능 평가
rmse = np.sqrt(mse)                                                #RMSE기반 모델 성능 평가
print('mes : ', mse)
print('rmse : ', rmse)
print('r-square : ', r2_score(y_test, y_predict))     #1에 가까울 수록 해당 회기선이 데이터에 대한 100% 설명력을 가진 모델로 평가

print('Y 절편 : ', model.intercept_)
coef = pd.Series(data=model.coef_, index=x_data.columns)
print('회기계수 : ', coef)


fig, ax = plt.subplots(figsize=(16,16), ncols = 2, nrows=4)
for i, feature in enumerate(x_data.columns):
    row = int(i/2)
    col = i%2
    sns.regplot(x=feature, y='price', data=california_df, ax=ax[row][col])

plt.show()




mydata  =[1,2,3,4,5,6,7,8]
print('우리집 가격은 : ', model.predict([mydata]))
