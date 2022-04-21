# uswgi 로그 확인하는 방법 

1. `ps -ef | grep uwsgi`  
uwsgi로 실행되는 파일을 확인
2. root 계정 접속
3. `cd /data/app/uwsgi/` 경로 이동 + `ls`로 확인
4. `tail -f uwsgi.log` 

* `tail -f` 실시간으로 에러로그를 확인하는 명령어.
