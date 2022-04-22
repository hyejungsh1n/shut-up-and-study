# 리액트
요즘에 가장 많이 사용하고 있는 javascript 라이브러리
리액트의 가장 장점으로 꼽히는 것은 사용자 정의 태그를 만들어서 함수로 리턴해줘서 반복되는 코드를 최소화할 수 있다.

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