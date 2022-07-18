
### 가비지 컬렉션

Js는 도달 가능성이라는 개념을 사용해 메모리 관리를 수행. 

그 값은 쉽게 말해 어떻게든 접근하거나 사용할 수 있는 값을 의미. 이것은 메모리에서 삭제 되지 않는다.


```js
let pet = { 
    name : "Moogoo"
};
```

전역변수 "pet"은 이름이 "Moogo"라는 객체를 참조.

```js
pet = null;
```

그럼 더 이상 "Moogoo"를  참조하지 않게 되고

 pet은 null이 된다.


#### 그렇다면 참조 두 개를 했을 때는?

```js
let pet = { name : "Moogoo" } ; 
let adminPet = pet

pet = null;
```

pet은 null이지만 adminPet을 통해서는 name은 "Moogoo"에 접근 가능. 


