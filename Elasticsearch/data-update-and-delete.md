# Elasticsearch : 데이터 업데이트 및 삭제


### 들어가기 전에

Elasticsearch는 동일 도큐먼트는 두 번 추가 할 수 없다.

동일 문서를 추가할 시에는 버전 충돌이 일어난다.

도큐먼트는 불변이기 때문에 작성한 것을 변경할 수 없는데, 이미 인덱싱 된 도큐먼트의 업데이트는 어떻게 할까?


-- 

## 데이터 업데이트

`_version` 이라는 필드를 사용하면 됨

Elasticsearch는 업데이트 시 증가한 `_version` 번호로 도큐먼트의 새 복사본을 작성하게 된다.

Elasticserach는 자동으로 사용자가 작성한 최신 버전을 사용한다.

업데이트 요청을 하면 완전히 새로운 문서가 생성 되고 새 도큐먼트는 새 버전으로 작성 된 후 이전 도큐먼트는 삭제 처리 됨

→ 당연한 거지만 지금 다루는 도큐먼트의 업데이트는 물론 삭제할 때도 모두 ID가 필요하다.


#### 복습 겸, Elasticsearch에 저장된 데이터를 찾는 법

```bash
curl -XGET 127.0.0.1:9200/movies/_search?q=[search_keyword]
```



**업데이트**는 **2가지 방법을 사용할 수 있다**

Elasticsearch에서 업데이트는 기존의 기록을 가져와 하나 이상의 필드를 업데이트 한다.


- 모든 필드를 **PUT** 명령으로 지정하여 업데이트로 처리

```bash
curl -XPUT 127.0.0.01:9200/movies/_doc/109487?pretty 
-H 'Content-Type:application/json' -d ' 
{"genre": ["IMAX", "Sci-fi"], "title": "Interstellar CAT", "year": 2014 } '
```


- 부분 업데이트로 **POST**를 사용하여 정보 필드의 하위 집합만 변경

```bash
curl -XPOST 127.0.0.1:9200/movies/_doc/109487/_update 
-H 'Content-Type:application/json' -d '{"doc": {"title" : "Interstella" } } '
```


→ 결과는 똑같이 바뀜. 기존의 복사본이 변경 되었다는 것은 “_version“에 의해 알 수 있고, “result“를 통해 “updated“ 라는 이벤트가 발생했음을 알 수 있다.



## **데이터 삭제**

```bash
curl -XDELETE 127.0.0.1:9200/[index]/_doc/[document_s_id]
```

→ 이벤트 즉 result는 “deleted“ 로 출력

