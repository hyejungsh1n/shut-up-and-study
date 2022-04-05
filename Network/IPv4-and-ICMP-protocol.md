IPv4 프로토콜
=============


# IPv4가 하는 일
- 네트워크 상에서 데이터를 교환하기 위한 프로토콜
- 데이터가 정확하게 전달될 것을 보장하지 않음 (멀리 있는 곳에만 전달)
- 중복된 패킷을 전달하거나, 패킷의 순서를 잘못 전달할 가능성도 있음. (악의적으로 이용되면 Dos 공격이 됨)
- 데이터의 정확하고 순차적인 전달으 그보다 상위 프로토콜 TCP에서 보장한다.


# IPv4 프로토콜의 구조
- 20바이트
 옵션이 붙을 때 4바이트. 10개의 옵션까지 붙을 수도 있음. 옵션 없이 사용하는 게 일반적.
- 출발지 ip 4바이트, 목적지 ip 4바이트
- version, Header Length, total length, Identification, Protocol, Fragemnt Offset, TTL(패킷이 사는 시간), Header checksum, 출발지, 목적지, IP option


=============
ICMP 프로토콜
============

# ICMP의 기능
- ICMP? 인터넷 제어 메시지 프로토콜.
- 네트워크에서 돌아가는 운영체제에서 오류 메시지를 전송받는데 주로 쓰인다
- 프로토콜 구조의 type과 code를 통해 오류 메시지를 전송 받음.


# ICMP 프로토콜의 구조
특정 대상과 자신의 통신이 잘 되는지 확인
- type : 대분류
- code : 소분류
- checksum : 헤더에 오류가 있나 없나 체크하는 값

# type
8번 : 요청
0번 : 통신
3번 : destination unreachable - 경로상 문제 (ex.. 라우터)
11번 : time exceeded - 상대방의 문제 (ex.. 방화벽)
5번 : redirect