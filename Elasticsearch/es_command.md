### elasticSearch 상태 확인

`service elasticsearch status`

### ElasticSearch 서버 키기

`sudo /etc/init.d/elasticsearch start`
`service elasticsearch start`


### 환경 설정 파일 위치

/etc/elasticsearch
> elasticsearch.yml 

`network.host: 0.0.0.0`

-> 네트워크 대역 설정

입력하지 않으면, 연결이 안 된다.


### 포트 연결

`sudo curl -X GET "localhost:9200/”`

curl은 elasticsearch를 실행하는 서버에 http요청을 보낼 수 있는 명령어