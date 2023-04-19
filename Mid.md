## 조회
1. column 조회
```
df['column']
```  


2. row 조회
```
df.ix[index]
```
- ix의 경우 주의할점은 index가 integer로만 이루어진 경우에는 index로 접근하지만, index에 문자가 껴있으면 순서로 접근한다는 점이다. 

## 통계함수
+ sum()
+ mean() : 열에 대한 통계량

> 조건별 평균
> ```
> df.loc[condition, 'column명'].mean()
> ```
> > skipna=False로 설정하게 된다면, NaN 값이 있는 column은 NaN 값으로 출력

## groupby함수
.groupby('컬럼명')+통계함수
+  `.agg()` 다중 통계량 구할 수 있음
    +  다중 통계량을 구할 때 컬럼별 적용할 통계 함수를 다르게 적용할 수 있음

## DataFrame 합치기
참조: <https://yganalyst.github.io/data_handling/Pd_12/>
