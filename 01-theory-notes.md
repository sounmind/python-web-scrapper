## Python Theory
1. ���̽��� ������ Ÿ��
     - string, integer, float, boolean, none �� �ִ�.
     - ���̽㿡�� �Ҹ��� Ÿ���� `True`, `False` �̷��� ����.
     - ��� ����, �������� �ʴ´�, �� ���ϴ� `None`�� �ִ�. JS���� `null`�� ������.
2. �ڵ� ��Ÿ��
      - snake_case�� ���̽��� �⺻ �ڵ� ��Ÿ���̴�.
3. [���̽��� Lists, Sequence types](https://docs.python.org/ko/3/library/stdtypes.html#sequence-types-list-tuple-range)
   - `squence type` �� [������ �ִ� ������ ����](https://python.bakyeono.net/chapter-5-2.html)��� ���̴�.
   1. [mutable sequence type - list](https://docs.python.org/ko/3/library/stdtypes.html#lists)
         - `days = ["mon", "tue", "wed"]`
         - ���ȣ('[]')�� �����ְ� �ȿ� ��ҵ��� �޸�(',')�� �����Ѵ�.
         - `mutable`�� ������ ���� �ٲ� �� �ִٴ� ���̴�. `append`, `pop`, `remove` ���� �Լ��� ���� ������ �� �ִ�.
   2. [immutable sequence type - tuple](https://docs.python.org/ko/3/library/stdtypes.html#tuples)
         - `days = ("mon", "tue", "wed")`
         - �Ұ�ȣ('()')�� ������ �����ָ� Ʃ���� �ȴ�.
         - Ʃ���� ������ ���� �ٲ� �� ����.
   3. [mapping types - dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
         - �߰�ȣ�� �����ش�. �ϳ��� ��Ҵ� key�� value�� �ݷ�(':')���� ����Ǿ� �ְ� ��Ҵ� �޸��� �����Ѵ�.
            ```python
            leesche = {
            "name" : "leesh",
            "age" : 26,
            "fav_food" : ["Chicken", "Sushi"]
            }
            ```
         - dict Ÿ�� �����Ϳ��� Ư�� ��Ҹ� �˻��Ͽ� ����� �� �ִ�. ��Ҹ� �߰��� ���� �ִ�.
   4. [��Ʈ�� �Լ���](https://docs.python.org/3/library/functions.html)
   5. �Լ� ���ǿ� ����
         - ���̽㿡���� �Ʒ��� ���� �Լ��� ����(`def`)�� �� �ְ� �Լ� ������ default�� ���� `=`�� ����� ������ �� �ִ�.      
            ```python
            def plus(a, b=0):
                  print(a+b)

            plus(2, 5)
            plus(2)
            ```
         - �Լ� ��ü�� �Լ��� ���� ����� �����ϰ� �ʹٸ� `return`�� �������. ������ �ϳ��� �Լ��� �� ���ۿ� �� �� ����.
         - Keyworded Arguments
             - �Լ� ���� �̸��� �Ű������� ���� �Ἥ ���� �����ϸ� �Լ� ������ ������� ���޵Ǵ� ���� �ƴ϶�, �Լ� ���� �̸����� �Ű������� ���޵ȴ�.
            ```python
            def minus(a, b):
                  return a - b

            result = minus(b=2, a=5)
            print(result)
            ```
   6. ���ǹ�
      ```python
      def plus(a, b):
            if type(b) is int or type(b) is float:
                  return None
            else
                  return a+b
      ```
      - `elif`�� else if�� �ǹ̷� ����� �� �ִ�.
   7. �ݺ���
      ```python
      days = ("Mon", "Tue", "Wed")
      for any_name in days:
            if any_name is "Wed":
                  break
            else:
                  print(day)
      ```
      - ���ڿ��� �ϳ��� ������ ������ Ÿ���̹Ƿ� �ݺ������� �ϳ��� ����� �� �ִ�.