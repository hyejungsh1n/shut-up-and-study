### Nginx 서버 구축



‪

가. CentOS에 python3.7 설치

0. `su-` 
    root 계정 로그인

1. `yum install wget gcc openssl-devel  libffi-devel bzip2-devel`
    개발 환경을 구축하기 위한 컴파일러 설치

2. `wget [https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz](https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz)`
    python 파일 다운로드

3. `tar xzf Python-3.7.1.tgz`
    다운 받은 python 파일 압축 해제

4. `cd Python-3.7.1`
`./configure --enable-optimizations`
    빌드

5. `make altinstall`
    디폴트로 설치된 python 파일과 병행 사용을 위해 덮어쓰게 만듦

6.  `which python3.7`
    확인