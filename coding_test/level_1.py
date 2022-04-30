# 대소문자 바꿔서 리버스소트

def solution(s):
    lis1 = list(s) # 문자열로 전부 자름
    lis1.sort(reverse=True) # 역 sort
    lis2 = ','.join(lis1) # g,f,e,~
    list_ = lis2.replace(',', '') 
    return list_