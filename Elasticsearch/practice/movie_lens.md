# 실습


### 데이터 매핑하기

```
curl -XPUT 127.0.0.1:9200/movies -H 'Content-Type:application/json' -d '
{                    
    "mappings": {
        "properties": {
            "year": { 
                "type" : "date"    
            }
        } 
    } 
}  '
```

`-H` 헤더 타입 명시

### Mappings에 대한 GET 요청

``` bash 
curl -XGET 127.0.0.1:9200/movies/_mappings
```

{"movies":{"mappings":{"properties":{"year":{"type":"date"}}}}} 

로 정상 출력된 것을 확인.

### document 삽입


```
 curl -XPOST 127.0.0.1:9200/movies/_doc/109487 -H 'content-Type:application/json' -d ' { "genre" : ["IMAX", "Sci-fi"], "title": "Interstella", "year":2014 } '
```

출력 : {"_index":"movies","_type":"_doc","_id":"109487","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}


### 줄바꿈

``` bash
curl -XGET 127.0.0.1:9200/movies/_search?pretty
```

{
  "took" : 44,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "movies",
        "_type" : "_doc",
        "_id" : "109487",
        "_score" : 1.0,
        "_source" : {
          "genre" : [
            "IMAX",
            "Sci-fi"
          ],
          "title" : "Interstella",
          "year" : 2014
        }
      }
    ]
  }
}


### GET & POST

Elasticsearch에서

정보를 검색하는 경우 GET 사용

인덱스에 새로운 문서를 추가할 경우 POST 사용


### Bulk API 사용하기

Elasticsearch는 특정 문서를 주어진 샤드로 해시

개별 문서를 한 번에 하나씩 처리 해야 한다.

다운 받은 자료를 bulk로 가져오기

``` bash
curl -XPUT 127.0.0.1:9200/bulk?pretty -H 'Content-Type:application/json' --data-binary @movies.json
```

Elasticsearch는 동일 문서는 두 번 추가 할 수 없다

-> 동일 문서 추가 시, 버전 충돌 일어남


------------

## elasticsearch 데이터 업데이트 

Elasticsearch 도큐먼트는 불변이기 때문에, 작성된 것을 변경할 수 없다

그렇다면 이미 인덱싱 된 문서 변경 업데이트는 어떻게 하는가?

-> `_version`이라는 필드를 사용하면 됨

증가한 `_version` 번호로 문서의 새 복사본을 작성한다

도큐먼트의 고유 ID와 버전을 함께 사용하면 됨 

Elasticsearch는 자동으로 사용자가 작성한 최신 버전을 사용 

업데이트 요청을 하면 완전히 새로운 문서가 생성 되고, 새 도큐먼트는 증가한 버전 번호로 작성된 후 이전 도큐먼트는 삭제로 표시


``` bash

curl -XPOST 127.0.0.1:9200/[index]/_doc/[id]/_update -d ' {
  "doc": {
    "title" : "Interstella"
    }
  } '
```
-> `update` 기존의 기록을 가져와 하나 이상의 필드를 업데이트 

이전 기존 버전에 있던 다른 것들은 복사, 새 번호를 가진 새 복사본 형성

업데이트 수행 방법은 모든 필드를 포함하여 전체 문서 다시 지정 -> 업데이트 이벤트로 처리


### 모든 필드를 PUT 명령으로 지정하여 업데이트로 처리 

``` bash

curl -XPUT 127.0.0.01:9200/movies/_doc/109487?pretty -H 'Content-Type:application/json' -d ' {"genre": ["IMAX", "Sci-fi"], "title": "Interstella CAT", "year": 2014 } '

-- 출력 결과 -- 

{
  "_index" : "movies",
  "_type" : "_doc",
  "_id" : "109487",
  "_version" : 2,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 5,
  "_primary_term" : 3
} 

```

"result"가 "updated"인 것을 확인하며 이벤트가 발생한 것을 알 수 있다 

기존 아이디로 검색 결과 요청 시, 복사본1이었던 Interstella는 삭제 되고 Interstella CAT만 남게 된다 

그 전까지는 변경이 없었으므로 버전은 2가 된다


``` bash

curl -XGET 127.0.0.01:9200/movies/_doc/109487?pretty

-- 출력 결과 -- 

{
  "_index" : "movies",
  "_type" : "_doc",
  "_id" : "109487",
  "_version" : 3,
  "_seq_no" : 6,
  "_primary_term" : 3,
  "found" : true,
  "_source" : {
    "genre" : [
      "IMAX",
      "Sci-fi"
    ],
    "title" : "Interstella CAT",
    "year" : 2014
  }
}

```

### 부분 업데이트로 정보 필드의 하위 집합만 변경

부분 업데이트의 경우에는 POST 동사 활용

``` bash
 
 curl -XPOST 127.0.0.1:9200/movies/_doc/109487/_update -H 'Content-Type:application/json' -d '{"doc": {"title" : "Interstella" } } '
 
 ```

 결과는 똑같이 바뀜

 
 ## Elasticsearch로 데이터 삭제

당연하지만 도큐먼트를 수정히거나 삭제하려면 해당 도큐먼트의 아이디를 알아야 함

해당 아이디를 모를 경우 검색 예시

``` bash
curl -XGET 127.0.0.1:9200/movies/_search?q=[search_keyword]
``` 

삭제

 ``` bash

curl -XDELETE 127.0.0.1:9200/[index]/_doc/[document_s_id]

 ```


이벤트 발생은 `  "result" : "deleted"  ` 로 출력

