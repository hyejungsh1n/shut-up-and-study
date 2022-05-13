## SCREEN

### What is Screen

screen은 가상 터미널로 물리적인 터미널을 다중화함

여러 window 실행 가능하고 다른 작업을 실행할 수 있음


### 스크린을 사용하는 이유

ssh 연결이 끊어져도 살아있기 때문에 작업을 수행할 수 있게 해줌


### screen 명령어 

생성 
 `screen -S web(스크린 이름)`

목록 확인
 `screen -list`

현재 유저와 연결을 끊고 재연결
`screen -dr web`
