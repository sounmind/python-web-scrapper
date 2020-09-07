## Before Learning a Django
### *args **kwargs
- 함수 인자를 무한대로 받고 싶을 때,
  - 인자는 두 종류가 있다.
    - Positional argument
      - 함수 인자에 `*args`를 추가하고, 입력된 값은 튜플 형태로 출력된다.
    - Keyword argument
      - 함수 인자에 `**kwargs`를 추가, 입력된 값은 딕셔너리로 출력된다
### 객체 지향 언어 (Object Oriented Programming)
- `Class`
  - 설계도 ( 작동방식, 기능, 설명 등이 들어 있다)
  - 클래스로 무언가를 만든다면 그것은 `instance`이다.
- `Method`
  - `Class` 안에 있는 `function`은 `Method`이다.
  - 함수 인자가 없는 Method를 만들고 함수 바깥에서 사용했을 경우 함수 인자에 하나의 인자가 입력됐다고 하며 오류가 발생한다. 왜 그럴까?
    - 파이썬은 모든 함수를 하나의 argument랑 함께 사용한다. 그것은 바로 `self`
    - 즉, 모든 method의 첫번째 argument는 **method를 호출하는 instance 자신**이다. 중요하니까 반복하자.
    - > 모든 method의 첫번째 argument는 method를 호출하는 instance 자신이다.
- 쉽게 수정(커스터마이즈)할 수 있게 `Class`를 만드는 방법
  - `dir(클래스이름)`를 해보자
    - 클래스 안에 있는 것들이 모두 리스트로 출력된다. 거기 안에 있는 것들을 살펴보면 ...
    - `__str__`
      - `method`이다. 호출되면 그 class의 `instance`를 출력한다.
      - 즉, `print(클래스이름)`하면, `클래스이름`의 `instance`를 출력한다.
    - `__init__`
      - 클래스를 만들 때 바로 만들어진 `method`
      - `self, args, kwargs` 모두 인자로 받는다.
      - 따라서 아래와 같이 함수 인자의 입력과 출력을 통제할 수 있다. (완전 놀랍다! 이제야 파이썬 수업에서 왜 init을 썼는지 이해가 된다.)
        ```python
        class Car():
            def __init__(self, **kwargs):
                self.wheels = 4
                self.doors = 4
                self.windows = 4
                self.color = kwargs.get("color", "black")
                self.price = kwargs.get("price", "$20")

        porche = Car(color="green", price="$40")
        print(proche.color, proche.price) # green $40
        ```
    - `Class`의 확장
      - 상속(inherit) 또는 확장(extend)
      - `새클래스이름(새클래스가상속받을원래클래스이름)`
      - 상속 받았던 `method`를 계속 쓸 수도 있고 재정의(override)해서 사용할 수도 있다. 하지만 예를 들어 ...
      - `__init__` method의 instance들 중 하나만 추가하여 사용하고 싶을 땐 어떻게 할까?
        - 그냥 method를 재정의해서 쓰면, `상속받았던원래클래스`의 instance들을 모두 잃어버린다. 그 method 전체를 대체해버리는 것이다. 이 문제를 해결하려면 ...
      - **`super`**로 **method**를 **extend**하자
        - 아래와 같이 사용하면 된다.
```python
class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # 부모클래스의 메서드(여기선 init)를 불러와 확장한다는 뜻
        self.time = kwargs.get("time", 10) # 추가하고 싶었던 instance
```

