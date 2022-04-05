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

