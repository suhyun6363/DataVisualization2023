## 조회
1. column 조회
```
df['column']
```  

2. row 조회
```
df.ix[index]
```
- ix의 경우 주의할점은 index가 integer로만 이루어진 경우에는 `label`로 접근하지만, index에 문자가 껴있으면 `순서`로 접근한다는 점이다. 

## 통계함수 참조 : <https://teddylee777.github.io/pandas/pandas-tutorial-04/>
+ sum()
+ mean() : 열에 대한 통계량

조건별 평균
 ```
df.loc[condition, 'column명'].mean()
 ```
> skipna=False로 설정하게 된다면, NaN 값이 있는 column은 NaN 값으로 출력
+ `unique()`함수는 데이터에 고유값들이 어떠한 종류들이 있는지 알고 싶을때 사용하는 함수
+ `nunique()`함수는 데이터에 고유값들의 수를 출력해주는 함수
+ `value_counts()`는 값별로 데이터의 수를 출력해주는 함수(`ascending=True`오름차순 정렬)

## groupby함수
.groupby('컬럼명')+통계함수
+  `.agg()` 다중 통계량 구할 수 있음
    +  다중 통계량을 구할 때 컬럼별 적용할 통계 함수를 다르게 적용할 수 있음

## 참조: <https://yganalyst.github.io/data_handling/Pd_12/>
1. DataFrame 붙이기 `pd.concat()`
+ `concat([df1, df2])`  join default outer(합집합)
+ `concat([df1, df2], ignore_index=True)`       중복인덱스 제거
+ `concat([df1, df2], join=inner)`  교집합
2. DataFrame 병합 `pd.merge()`  
+ `merge()`함수는 두 데이터프레임을 각 데이터에 존재하는 고유값(key)을 기준으로 병합할때 사용한다.
```
pd.merge(df_left, df_right, how='inner', on=None)
```
> 아무 옵션을 적용하지 않으면, `on=None`이므로 두 데이터의 공통 열이름(id)을 기준으로 inner(교집합) 조인을 하게 된다.

## 데이터 정렬
+ `sorted_values()` default 오름차순 정렬, NaN값은 맨 마지막에 위치
```
df.sorted_values(by= ['컬럼명1', '컬럼명2', ...], ascending = [True, False, ...])
```

