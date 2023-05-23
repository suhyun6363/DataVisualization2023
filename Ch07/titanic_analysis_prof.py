import seaborn as sns                                  # 타이타닉 dataset load를 위해 필요
import pandas as pd                                    # dataFrame 자료구조 다루기 위해 필요
import numpy as np                                     # numpy 데이터 형식 변환을 위해 필요

#pip install scikit-learn 필요
from sklearn.linear_model import LogisticRegression    # sklearn  package 에서 제공하는 로지스틱 회기분석 모듈
from sklearn.metrics import classification_report, confusion_matrix # 학습결과의 성능지표를 확인하기 위해 임포트!~
from sklearn.model_selection import train_test_split   # 학습 데이터와 테스트 데이터 분리를 위해 필요
from sklearn.metrics import accuracy_score             # 학습 결과 자동으로 계산해주는 모듈

titanic = sns.load_dataset("titanic")
#print(titanic.head())
#print(titanic.info())
#print(titanic.describe())

#print(titanic.isnull().sum())
#titanic = titanic.drop(['embarked', 'deck', 'embark_town'], axis='columns', inplace=True) #inplace = True 내부에서 제거 처리 titanic = 할 필요 없음
#print(titanic.isnull().sum()) # deck 삭제
titanic.age = titanic.age.fillna(titanic['age'].median()) # age의 경우 중간 값으로 대체
titanic.drop(['embarked', 'deck', 'embark_town'], axis='columns', inplace=True)
#print(titanic.isnull().sum()) # age 0 으로 변환됨, embarked, embark_town 0 변환

titanic['age'] = titanic['age'].apply(lambda x: x % 10)
#print(titanic['age'])

#print(titanic.describe()) # 수치형 속성값들만 알아내기 위해 print / titanic.info()
print(titanic.info())
x_data = titanic[['pclass', 'age', 'sibsp', 'parch', 'adult_male', 'fare', 'alone']]
y_data = titanic[['survived']]

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, stratify = y_data, random_state=1568) # 시험 데이터 20%, 훈련 데이터 80%
# stratify 훈련, 시험마다 종속변수 결과에 대한 비율별로 추출(훈련: 0 30%, 1 70% / 시험: 0 30%, 1 70%)      # random_state: 반복 동안 계속 같은 train, test set 유지
# x_data=> x_train, x_test / y_data-> y_train, y_test

x_train = np.array(x_train)
x_test  = np.array(x_test)
y_train = np.array(y_train)
y_test  = np.array(y_test)
# 로지스틱 모델 지정
logit = LogisticRegression(solver='lbfgs', max_iter=1000) # max_iter default값 1000, 괄호 안 안 써줘도 무방

# logit 값을 traning set을 통해 학습
logit.fit(x_train, y_train.reshape(-1)) # fit함수 정답파라미터에 일차원 벡터 형태로 들어가야 하므로 변환해야 함 # 두번째 파리미터의 데이터 shape 변경위해 ravel() 사용 다차원 배열을 1차원으로 변경
                                    # ravel(), reshape(-1), flatten() 모두 동일하게 동작

y_test_pred = logit.predict(x_test) # x_test을 통해 예측한 값

print("Accuracy : ", accuracy_score(y_test, y_test_pred)) # 실제 정답과 비교 # y_test = ground_true / y_test_predict = prdict

print(classification_report(y_test, y_test_pred))   # accuracy 값 이외 다른 성능 지표 출력
print(confusion_matrix(y_test, y_test_pred))        # 성능지표를 계산하는 근거 값 출력 / 그림도 그려보자
# [[실제 정답인데 정답이라 한 경우, 실제 정답인데 오답이라 한 경우], [실제 오답인데 정답이라 한 경우, 실제 오답인데 오답이라 한 경우]]

#import matplotlib.pyplot as plt
#sns.heatmap(confusion_matrix(y_test, y_test_pred),cmap='Blues',annot=True,fmt='2.0f')
#plt.show()
'''
# 교재에서 나온 것 처럼 나이 등급으로 분류해봤다......
def category_age(x):  # describe()로 파악했을 때, max값이 80 내외라 이렇게 짧게 변경했음...
    return x % 10


titanic = sns.load_dataset('titanic')

#print(titanic.head(10))                               # 데이터 확인
print(titanic.isnull().sum())                          # 공백 포함 데이터 확인
titanic.drop(['embarked', 'deck', 'embark_town'], axis='columns', inplace=True) # 불필요할 것으로 판단되는 속성 삭제
#inplace=True 하면 아래와 같은 의미...변경된 데이터를 바로 반영하는 옵션
#titanic = titanic.drop(['embarked', 'deck', 'embark_town'], axis='columns', inplace=True) # 불필요할 것으로 판단되는 속성 삭제

titanic.age = titanic.age.fillna(titanic.age.median()) # age의 경우 중간 값으로 대체
titanic['age'] = titanic['age'].apply(category_age)        # 등급으로 바꿔봤다...
titanic['age'] = titanic['age'].apply(lambda x: x % 10)    # 간단한 기능을 함수로 만들기 귀찮은 경우 이렇게 멋지게 lambda 쓰면 있어보임... # 일회성 함수의 경우 사용


print(titanic.who.value_counts())
titanic.who = titanic.who.map({'child':0, 'woman':1, 'man':2}) # 범주형 데이터를 숫자형 데이터로 치환
print(titanic.describe())
print(titanic.info())

#회기모델에서는 숫자형, boolean형 데이터만 사용 가능, 범주형 데이터 일부를 숫자형으로 변환하여 적용해보자....
#성능 차이가 발생할까?
x_data = titanic[['pclass', 'age', 'sibsp', 'parch', 'fare', 'who', 'alone']] # 학습에 사용되는 독립변수들
y_data = titanic[['survived']]                                                # 정답 (종속변수)

#데이터세트 분할
x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, test_size=0.2, stratify = y_data, random_state=1568)

# numpy array 형태로 변환
x_train = np.array(x_train)
x_test  = np.array(x_test)
y_train = np.array(y_train)
y_test  = np.array(y_test)


# 로지스틱 모델 지정
logit = LogisticRegression(solver='lbfgs', max_iter=100) # default option이 이렇다...

# logit 값을 traning set을 통해 학습
logit.fit(x_train, y_train.reshape(-1)) # 두번째 파리미터의 데이터 shape 변경위해 ravel() 사용 다차원 배열을 1차원으로 변경
                                    # ravel(), reshape(-1), flatten() 모두 동일하게 동작

# 학습이 완료된 logit통해 test 데이터세트확인
y_test_pred = logit.predict(x_test) # x_test을 통해 예측한 값

print("Accuracy : ", accuracy_score(y_test, y_test_pred)) # 실제 정답과 비교


print(classification_report(y_test, y_test_pred))   # accuracy 값 이외 다른 성능 지표 출력
print(confusion_matrix(y_test, y_test_pred))        # 성능지표를 계산하는 근거 값 출력 / 그림도 그려보자

import matplotlib.pyplot as plt
sns.heatmap(confusion_matrix(y_test, y_test_pred),cmap='Blues',annot=True,fmt='2.0f')
plt.show()
'''

