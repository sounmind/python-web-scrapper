## Python Theory
1. 파이썬의 데이터 타입
     - string, integer, float, boolean, none 이 있다.
     - 파이썬에서 불리언 타입은 `True`, `False` 이렇게 쓴다.
     - 비어 있음, 존재하지 않는다, 를 뜻하는 `None`이 있다. JS에서 `null`과 가깝다.
2. 코딩 스타일
      - snake_case가 파이썬의 기본 코딩 스타일이다.
3. [파이썬의 Lists, Sequence types](https://docs.python.org/ko/3/library/stdtypes.html#sequence-types-list-tuple-range)
   - `squence type` 은 [순서가 있는 데이터 구조](https://python.bakyeono.net/chapter-5-2.html)라는 뜻이다.
   1. [mutable sequence type - list](https://docs.python.org/ko/3/library/stdtypes.html#lists)
         - `days = ["mon", "tue", "wed"]`
         - 대괄호('[]')로 감싸주고 안에 요소들은 콤마(',')로 구분한다.
         - `mutable`은 내부의 값을 바꿀 수 있다는 뜻이다. `append`, `pop`, `remove` 등의 함수로 값을 조작할 수 있다.
   2. [immutable sequence type - tuple](https://docs.python.org/ko/3/library/stdtypes.html#tuples)
         - `days = ("mon", "tue", "wed")`
         - 소괄호('()')로 값들을 감싸주면 튜플이 된다.
         - 튜플은 내부의 값을 바꿀 수 없다.
   3. [mapping types - dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
         - 중괄호로 감싸준다. 하나의 요소는 key와 value가 콜론(':')으로 연결되어 있고 요소는 콤마로 구분한다.
            ```python
            leesche = {
            "name" : "leesh",
            "age" : 26,
            "fav_food" : ["Chicken", "Sushi"]
            }
            ```
         - dict 타입 데이터에서 특정 요소만 검색하여 출력할 수 있다. 요소를 추가할 수도 있다.
   4. [빌트인 함수들](https://docs.python.org/3/library/functions.html)
   5. 함수 정의와 인자
         - 파이썬에서는 아래와 같이 함수를 정의(`def`)할 수 있고 함수 인자의 default를 값을 `=`을 사용해 정해줄 수 있다.      
            ```python
            def plus(a, b=0):
                  print(a+b)

            plus(2, 5)
            plus(2)
            ```
         - 함수 자체에 함수의 실행 결과를 저장하고 싶다면 `return`을 사용하자. 리턴은 하나의 함수에 한 번밖에 할 수 없다.
         - Keyworded Arguments
             - 함수 인자 이름을 매개변수에 직접 써서 값을 대입하면 함수 인자의 순서대로 전달되는 것이 아니라, 함수 인자 이름으로 매개변수가 전달된다.
            ```python
            def minus(a, b):
                  return a - b

            result = minus(b=2, a=5)
            print(result)
            ```
   6. 조건문
      ```python
      def plus(a, b):
            if type(b) is int or type(b) is float:
                  return None
            else
                  return a+b
      ```
      - `elif`를 else if의 의미로 사용할 수 있다.
   7. 반복문
      ```python
      days = ("Mon", "Tue", "Wed")
      for any_name in days:
            if any_name is "Wed":
                  break
            else:
                  print(day)
      ```
      - 문자열도 하나의 시퀀스 데이터 타입이므로 반복문으로 하나씩 출력할 수 있다.