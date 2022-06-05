### Optimistic concurrency control

→ 웹 사이트, 엘라스틱 서치 서비스, 클러스터에 동시에 접속하는 클라이언트가 많을 경우 elasticsearch가 제공하는 동시성 처리 방법.

Elaticsearch는 기본적으로 `seq_no(sequece number)` 와 `_primary_term(primary term)` 을 이용한다.

기본적으로 Elasticsearch의 요청 자체에는 `sequece number` 를 요구하므로, 이 번호가 같을 경우에는 충돌이 발생하게 되어 재시도를 할 수 있게끔 만든다.
