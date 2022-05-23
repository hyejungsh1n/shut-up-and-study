## 실습


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


## Bulk API 사용하기

Elasticsearch는 특정 문서를 주어진 샤드로 해시

개별 문서를 한 번에 하나씩 처리 해야 한다.

다운 받은 자료를 bulk로 가져오기

``` bash
curl -XPUT 127.0.0.1:9200/bulk?pretty -H 'Content-Type:application/json' --data-binary @movies.json
```