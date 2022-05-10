
## Git

**.gitignore 쓰는 이유** 

각종 환경변수나 서비스 키 등 github에 올라가지 않게 무시해주기 때문. 숨김파일로 작성하면 된다.


그러나 이미 기존에 파일을 git에 올린 후에, .gitignore에 적용해도 달라지는 게 없는 것을 확인할 수 있다. 이럴 때 사용하는 명령어.

```bash
git rm -r --cached .
git commit -m update "commit message"
git push
```

**git push 하는데 reject 될 때 Updates were rejected because the remote contains work~**

```bash
* 이미 터미널이 친절하게 알려줌
git pull 
```

이러고 다시 push하면 됨. [README.md](http://README.md) 파일 건드렸는데 그 오류라고 함.


