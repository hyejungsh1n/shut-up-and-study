### Object.assign

객체에 할당된 변수를 복사하면 동일한 객체에 대한 참조값이 하나 더 만들어진다. 

기존에 있던 객체와 똑같으면서도 독립적인 객체를 만드는 방법. (반복문 없이도 가능)


구문
`Object.assign(target(목표객체), ...sources(출처객체))`



```js
let pets = { name : "Moogoo" };
let permission1 = { canView : true };
let permission2 = { canEdit : true };

Object.assign(pets, permission1, permission2);
```

-pets ->  {name : "Moogoo", canView : true, canEdit : true } 

그러나 참조