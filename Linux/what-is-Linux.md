리눅스
==============

현 상태 : 리눅스 기본 명령어는 알고 있으나, 부족한 부분을 조금 채우기로 한다.


# What is Linux?
- 컴퓨터의 운영체제의 한 종류
- 핀란드 헬싱키 대학의 대학원생 리누스 토발즈가 1991년에 개발
- 윈도우와는 다르게 오픈 소스 운영체제
- 구글의 안드로이드 또한 리눅스가 운영체제


# 운영체제
- 사용자와 시스템 사이에서 편리한 인터페이스 제공
- 시스템의 각종 네트워크 장치또는 하드웨어를 관리 및 제어
- 운영체제의 종류는 윈도우, MAC os, IOS 등등


# 리눅스의 조상 : 유닉스
- 멀티태스킹을 지원하는 운영체제(멀틱스) 개발을 시작 -> 실패로 끝남.
- 멀틱스를 이어 받아 하나의 작업이라도 하는 유닉스(UNIX)라는 운영체제를 기계어로 만듦
- 기계어로 만든 것을 C언어로 개발.


# 리눅스의 특징
- C언어 기반이기 때문에 높은 이식성과 확장성
- 안정성과 신뢰성. 국제적이고 개방적으로 개발되어있기 때문에 문제점에 대한 대처가 빠름.
- 계층적인 파일 시스템. (최상위 디렉토리가 존재하고 모든 것들은 해당 디렉토리 하부에 존재.)


# 리눅스의 기본 구성 요소
명령어 > 쉘(명령어번역기) > 커널 > H/W


# 프롬프트
- 컴퓨터가 입력을 기다리고 있음을 가리키기 위해 화면에 나타나는 표시
- 일반적으로 리눅스의 프롬프트는 현재 작업 디렉토리, 현재 로그인한 사용자 등에 대한 정보를 표시


# 명령줄 인터페이스 
- 명령어로 모든 것을 처리
- 텍스트 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식.
- 명령어 구조
  명령어 : 시스템에서 특정 작업을 하기 위해 실행하는 실행 파일, 프로그램
  옵션 : 명령어를 어떻게 실행할 것인지 지정. 일반적으로 '-' 문자 뒤에 옵션을 지정.
  얼규먼트(Argument) : 명령어에 의해서 영향을 바든 파일 or 디렉토리 등 특정 대상 ex) netstat -anp, ifconfig -a, ls, -al