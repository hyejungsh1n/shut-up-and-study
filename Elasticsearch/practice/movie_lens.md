## 실습

1. root 계정에 bin directory 생성 > vi로 파일 만들어주기

2. 데이터 매핑하기

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

3. Mappings에 대한 GET 요청

``` bash 
curl -XGET 127.0.0.1:9200/movies/_mappings
```

{"movies":{"mappings":{"properties":{"year":{"type":"date"}}}}} 

로 정상 출력된 것을 확인.

