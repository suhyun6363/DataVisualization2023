## 조회
1. column 조회

  df['column']
  

2. row 조회

  df.ix[index]

+ ix의 경우 주의할점은 index가 integer로만 이루어진 경우에는 index로 접근하지만, index에 문자가 껴있으면 순서로 접근한다는 점이다. 

