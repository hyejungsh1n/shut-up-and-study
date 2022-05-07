## 소계(총계) 함수

### Rollup

`그룹함수`로  분류됨. 데이터를 `Group by` 하여 나타낼 수 있는 데이터를 구하는 함수. 

`소계(총계)함수` 의 일종이다

`Rollup` 소그룹 간의 소계 및 총계를 계산.

ROLLUP (A) -- A로 그룹핑
ROLLUP (A, B) -- A, B로 그룹핑, A로 그룹핑, 총합계
ROLLUP (A, B, C) -- A, B, C로 그룹핑, A,B로 그룹핑,  A로 그룹핑, 총합계 

```sql
SELECT ORDER_DT, ORDER_ITEM, REG_NAME, COUNT(*)
	FROM STARBUGS_ORDER
GROUP BY ROLLUP(ORDER_DT, ORDER_ITEM, REG_NAME)
ORDER BY ORDER_DT;

-- 날짜별, 주문음료별, 판매사원별로 그룹핑 + 날짜별, 주문음료별로 그룹핑
-- 날짜별로 그룹핑 총합계. 
-- 순서를 지키는 듯

-- 즉 출력결과는 전부 출력
-- REG_NAME이NULL인 상태의의 소계
-- REG_NAME과 ORDER_ITEM이 NULL인 상태로 소계(날짜)
-- 맨 하단 총계 
```

괄호로 묶이면 하나로 취급 ex) `GROUP BY ROLLUP((ORDER_DT, ORDER_ITEM), REG_NAME)` 이런 그룹 절이 들어갈 경우 괄호로 묶인것을 A로 보면 될 듯하다.