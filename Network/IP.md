IP
=========


# 3계층의 기능
서로 다른 네트워크 대역을 연결 시켜주는 역할. LAN과 LAN을 연결하는 WAN. 발신에서 착신까지의 패킷의 경로를 제어. 

# ifconfig 할 시, IP 주소 확인
IPv4 주소 : 현재 컴퓨터에 할당. 
서브넷 마스크 : IP 주소에 대한 네트워크의 대역을 규정.
게이트웨이 주소 : 외부와 통신할 때 사용하는 네트워크 출입구.


# classful IP주소
초창기에 쓰임. 낭비가 심한 단점이 있음.
- A클래스  0.0.0.0 ~ 127.255.255.255
- B클래스 128.0.0.0 ~ 191.255.255.255
- C클래스 192.0.0.0 ~ 223.255.255.255
- D클래스 224.0.0.0 ~ 239.255.255.255
- E클래스 240.0.0.0 ~ 255.255.255.255


# classless IP주소
서브넷 마스크 : classful한 네트워크 대역을 나눠주는데 사용하는 값이다. 어디까지가 네트워크 대역을 구분하는데 사용하고 어디서부터 호스트를 구분하는데 사용하는지 지정.
2진수로 표기했을 때 1로 시작함. 1과 1사이에는 0이 올 수 없다는 규칙을 가지고 있음. (즉, 0이 나오면 그 뒤에는 모두 0이어야 함)


# 공인 IP와 사설 IP
현재 사용하고 있는 IP 개념. 
공인 IP : 실제 인터넷에서 사용하고 통신하는 IP주소. 외부 네트워크 대역에서는 사설 IP 대역이 보이지 않는다. ex)네이버
사설 IP : 같은 네트워크 대역에서 사용하고 있는 IP주소.
NAT : network address translation. 네트워크 주소를 사설 ip에서 공인 ip로 바꿔주는 것. 


# 특수한 IP 주소
wildcard 0.0.0.0  - 나머지 모든 ip
127.0.0.1 - 자기 자신을 나타내는 주소
게이트웨이 주소 - 일반적으로 공유기의 ip. 