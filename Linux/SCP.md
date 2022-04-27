## SCP

`ssh 원격 접속 프로토콜`을 기반으로 해서 클라이언트에서 원격 서버로 파일을 보내거나 가져올 때 사용하는 프로토콜이다.

## 파일 전송 명령어

### LOCAL → REMOTE

- 단일 파일일 경우

`scp -P (PORT) (Local경로) (username)@(IP):/(경로)/(file명 또는 * )`

- 파일을 포함하고 있는 디렉토리를 보낼 경우

`scp -r 디렉토리명 원격지id@원격지ip:받는위치`

### REMOTE → LOCAL

- 단일 파일

`scp -P (PORT) (username)@(IP):/(경로)/(file명 또는 *) (Local경로) `

- 파일을 포함하고 있는 디렉토리를 보낼 경우

`scp -r 디렉토리명 원격지id@원격지ip:원본위치 받는위치`