## RESTFul API


### 들어가기 앞서 HTTP 요청이란?

- METHOD : 말 그대로 서버로 요청. GET, POST, PUT or DELETE
- PROTOCOL : HTTP의 종류 (ex) HTTP/1.1
- HOST : 네트워크에 연결 되어있는 컴퓨터
- URL : 해당 서버에 요청하는 리소스
- BODY : 요청 본문
- HEADERS : 요청에 대한 메타데이터를 포함

### RESTful API

HTTP 요청을 통해 웹 서비스를 연결하는 것.

- GET : 검색 결과처럼 정보를 찾는 요청
- PUT :  새 정보 추가
- DELETE : 삭제 요청

### REST

직역하면 대표 상태 전송

1. Client-server architecture 
클라이언트와 서버가 상호작용

2. Statelessness
모든 요청과 응답은 자급자족 → 여러 요청 간에 상태를 추적하지 않아야 함

3. Cacheabilty
응답에 정보가 캐시 될 수 있는지에 대한 정보가 포함될 수 있음 
4. Layered System 
특정 서버와 통신할 경우 특정 개별 서버와 통신하는 게 전부가 아님

5. Code on demand 
응답에 대한 페이로드로 코드를 전송할 수 있다는 개념

6. Uniform interface
전송하는 데이터는 예측 가능한 구조며 어떠한 변화에 구조화된 방식으로 대처 가능