### Mapping

스키마 정의 중 하나

``` JSON
curl -XPUT 127.0.0.1:9200/indexname  -d '
{
		"mappings": {
					"properties" : {
								"year" : {"type": "date"}
											}
					}
}'
```

`PUT` index에 정보를 입력하기 위해 사용

`127.0.0.1:9200` localhost의 루프백 주소와 elasticsearch의 포트인 9200

`/[indexname]` 사용할 인덱스 이름

`-d '{본문의 내용} '` 작은따옴표  안에 있는 내용은 요청의 본문 (JSON 데이터를 포함)

매핑은 필드의 유형을 날짜뿐 아니라 문자열, 바이트, 정수, 부동소수 및 불리언 값으로도 정할 수 있음

또한, 필드의 ‘전체 텍스트 검색 여부’도 설정 가능 