## Elasticsearch란?

JSON 요청을 처리하고 JSON 데이터를 반환하는 서버. 

뛰어난 검색 능력과 대규모 분산 시스템을 구축할 수 있는 검색 엔진 기능 제공.

### 특징

1. 오픈 소스
2. 실시간 분석
3. 전문 (full text) 검색 엔진 → JSON 형식
4. RESTFul API
5. 멀티테넌시 
- 별도의 커넥션 없이 하나의 쿼리로 묶어 검색. 검색 결과를 하나의 출력으로 도출. 


## ELK
- Elasticsearch
JSON 요청을 처리하고 JSON 데이터를 반환하는 서버.

- Logstash
엘라스틱 서치에서 데이터 수집을 위한 도구

- Kibana
엘라스틱 서치의 시각화 도구

--

## 용어 정리

### Cluster

데이터베이스의 개념

### Documents

- 데이터베이스로 따지면 `documents`는 엔티티를 갖는 한 줄의 행과 같은 역할.
- 모든 문서는 고유 ID를 가질 수 있음. 고유 ID를 갖거나 es에서 자동으로 할당해줄 수도 있음

### INDEX

- 가장 높은 단계의 엔티티
- 여러 `document`를 포함할 수 있음
- 데이터베이스로 따지면 `table`

### etc

- indexing : 데이터가 검색될 수 있는 구조로 변경화기 위해 원본 문서 검색어를 토큰들로 변환하여 저장하는 일련의 과정
- search : 문서를 찾아가는 과정
- query : 데이터를 찾아내기 위해 입력하는 것.


## Elasticsearch의 원리

`elasticsearch`는 기본적으로 검색 엔진이 된다고 했다.

어떻게 효율적인 데이터를 뽑아낼 수 있을까?

### TF-IDF 개념

Term Frequency x Inverse Document Frequency. 

직역하자면 단어 빈도와 역 문서 빈도.

- TF : 단어빈도는 지정된 검색어가 문서 내에서 나타나는 빈도.
즉, 문서 내에서 ‘고양이’라는 단어가 자주 사용된다면 단어 빈도 👍
- DF : 모든 문서에서 단어가 사용되는 빈도
- TF / DF : 단어 빈도를 문서 빈도로 나눔 → 해당 문서에서 얼마나 특별한지 알 수 있음. 관련성 측정.