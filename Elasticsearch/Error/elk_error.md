## Elasticsearch를 사용하며 겪었던 에러들 정리

### {"error":"Content-Type header [application/x-www-form-urlencoded] is not supported"}

에러 발생 이유 : Elasticsearch가 6.0 이후로 엄격해지면서 Content-Type을 확인해줘야 하는데, 그게 명시되어았지 않아서 생기는 오류

해결법 : `-H'Content-Type:application/json'` 추가.. 즉 명시해주면 된다는 것