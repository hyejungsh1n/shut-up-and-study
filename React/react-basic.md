# 리액트
요즘에 가장 많이 사용하고 있는 javascript 라이브러리
리액트의 가장 장점으로 꼽히는 것은 사용자 정의 태그, 즉 함수형 컴포넌트를 만들어서 함수로 리턴해줘서 반복되는 코드를 최소화할 수 있다.

## create-react-app
`npx create-react-app`

생성된 디렉토리 초기 구조
```jsx
public > 
	생략
	index.html 
src >
생략
app.js 
index.js // index.js에서 app.js에 있는 것을 리턴함
```


## 배포판 만들기
`npm run build`  
실행 시, `build` 라는 디렉토리를 확인할 수 있다. 파일의 불필요한 공백이 제거되어있는 것을 확인할 수 있다.
사용이유 : 배포하기 전에 파일의 용량을 줄여주는 작업이 필요하다. 

`npx serve -s build`
한 번만 실행 시킬 웹 서버를 다운로드. 실행 시에 접속할 수 있는 port가 나온다.


## 컴포넌트 생성
What is Component? 사용자 정의 태그. 리팩토링에 용이.
prop을 통해 입력값이 있으면 return 해줌.
0. 함수형으로 입력과 출력이 있음
1. 생성 시, 첫글자는 모두 대문자여야 함.
2. `return` 옆에 바로 태그가 있어야 함.


## props
- 리액트의 속성.
- 기본적으로 객체를 반환함. 즉, 객체로 접근이 가능하다.

```
function Header(props) {
  return <header>
  <h1><a href="/">{ props.title }</a></h1>
	</header>
}

.. 생략

function App() {
  return (
    <div>
      <Header title="I want to go home"></Header>
      <Nav></Nav>
      <Article></Article>
    </div>
  );
}
``` 
* 중괄호와 중괄호 사이의 정보는 일반적인 문자열이 아니라 표현식으로 해석되어 반영.


- 이벤트 발생 또한 props의 객체 안의 함수로 접근할 수 있다. 
ex) `props.onChangeMode()`
입력값 또한 주는 방법도 명시해두면 된다.

## State
prop과 state의 공통점 : 값이 변경 되면 새로운 return을 만들어줘서 ui를 바꿔줌.
prop과 state의 차이점 : 
- prop은 컴포넌트를 사용하는 외부자를 위한 데이터
- state는 컴포넌트를 만드는 내부자를 위한 데이터
hook : react에서 제공하는 일반적인 함수.

사용법 
```
import `{useState} from 'react'`; // hook을 import
const [mode, setMode] = useState('출근'); // setMode함수로 바뀔 값을 리턴해주면 됨.

```

useState는 배열을 리턴함.
- useState의 인자로 들어가는 것은 초기값.
- 0번째 데이터는 상태의 값을 읽음. 
- 1번째 데이터는 상태를 변경할 때 사용하는 함수. 


state를 만들 때, state의 데이터가 원시 데이터의 type이다. 
const [value, setValue] = useState(PRIMITIVE); 
Primitive type? string, number, boolean, undefined, symbol, null