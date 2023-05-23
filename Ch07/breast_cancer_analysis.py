import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler # 데이터 전처리 모듈

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import seaborn as sns
import matplotlib.pyplot as plt


b_cancer = load_breast_cancer()                    # data load
#print(b_cancer.keys())                            # sklearn에서 제공하는 데이터세트는 dict와 유사한 bunch라는 데이터타입을 사용함
print(b_cancer.DESCR)

########### - data의 형태와 내용을 확인하기 위해 Dataframe형태로 변환 (데이터의 생김새 확인을 위해)
b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
b_cancer_df['diagnosis'] = b_cancer.target
print(b_cancer_df.head())
print(b_cancer_df.info())
print(b_cancer_df.isnull().sum())
print(b_cancer_df.describe())

########### - 악성 cancer 진단을 위해 변수별 상관분석을 수행해봤다.....
#sns.heatmap(b_cancer_df.corr(), annot=True)
#plt.show()

# 학습율 향상을 위해 학습에 사용할 데이터들에 대한 분포를 조정하였음(평균 0, 분산 1)
scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)  #학습에 사용한 데이터 포멧은 numpy.ndarray

#데이터 확인을 위하 다시 df로 변환
b_cancer_scaled_df = pd.DataFrame(b_cancer_scaled, columns=b_cancer.feature_names)
print(b_cancer_scaled_df.head())

#b_cancer_df.reset_index().plot(kind='scatter', x='index', y='mean radius')
#b_cancer_scaled_df.reset_index().plot(kind='scatter', x ='index',  y='mean radius')
#plt.show()

# 학습에 사용할 데이터 구성
X = b_cancer_scaled       # feature set
Y = b_cancer.target       # ground truth
print(Y.mean())           # 음성/양성 비율 확인

#학습용/테스트용 데이터세트 분할
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, stratify = Y, random_state=1568)


logit = LogisticRegression() # logistic reg 모델 생성
logit.fit(x_train, y_train)  # 학습데이터 기반 학습 -> 모델 학습 완료
y_predict = logit.predict(x_test) # 테스트 세트로 평가


from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

conMat = confusion_matrix(y_test, y_predict)
print(conMat)
#sns.heatmap(conMat,cmap='Blues',annot=True,fmt='2.0f')
#plt.show()


print('ACC : ', accuracy_score(y_test, y_predict))
print('Precision : ', precision_score(y_test, y_predict))
print('Recall : ', recall_score(y_test, y_predict))
print('AUC : ', roc_auc_score(y_test, y_predict))


