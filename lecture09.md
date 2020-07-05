# 패키지

* 패키지는 디렉터리와 모듈로 구성된다.
* 패키지 > 패키지들... > 모듈들...

```
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
```
* game, sound, graphic, play는 디렉터리 이름이고 확장자가 .py인 파일은 파이썬 모듈이다.

* game 디렉터리가 이 패키지의 루트 디렉터리이고 sound, graphic, play는 서브 디렉터리이다.

* 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.

------------

## 패키지 사용하기
```py
# 첫번째: echo 모듈을 import하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()


# 두번째: echo 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법
from game.sound import echo
echo.echo_test()

# 세번째 : echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법
from game.sound.echo import echo_test
echo_test()

# 불가능
#import game
#game.sound.echo.echo_test()

# 불가능
# import game.sound.echo.echo_test
```

### __init__.py 의 용도
* ```__init__.py``` 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
* Version 3.3부터는 없어도 패키지로 인식한다.
