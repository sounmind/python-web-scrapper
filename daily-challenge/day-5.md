# python web scrapper challenge for 2 weeks
## day 5
1. 과제 목표:

2. 조건:

3. 구현
   - 구현 영상을 보면,
        1. 국가 인덱스(0부터 시작)와  국가 목록(A부터 시작, 화폐가 없으면 제거된)이 출력된다.
        2. 국가 인덱스를 입력하면 그 국가가 사용하는 화폐의 alpha-3 코드를 출력해주면 된다.
   - 구현 포인트
       - **table**에서 여러가지 요소(국가 이름과 화폐 코드)를 **어떻게** 가져와서 저장하느냐, 이다.
       - key와 value가 있는 dictonary로 국가 이름과 화폐 코드를 저장해야 좋겠다.
    ```python
    import os
    import requests
    from bs4 import BeautifulSoup

    os.system("clear")
    URL = "https://www.iban.com/currency-codes"
    iban_result = requests.get(URL)
    iban_soup = BeautifulSoup(iban_result.text, "html.parser")
    table = iban_soup.find("tbody") # 테이블
    table_rows = table.findAll("td") # 테이블 데이터

    # 국가 이름과 화폐 코드를 순서대로 저장할 빈 리스트 만들기
    name_countries = [];
    currency_codes = [];

    for name_country_index in range(0, len(table_rows), 4): # 나열된 td 중 0, 4, 8 ... 번째 값들이 국가 이름
    if table_rows[name_country_index+2].text == '': # 화폐가 비어있으면 리스트에 입력 하지 않음
        continue
    name_countries.append(table_rows[name_country_index].text.capitalize()) # 문자열로 변환(text), 첫문자가 대문자로 변환(capitalize())

    for currency_codes_index in range(2, len(table_rows), 4): # 나열된 td 중 2, 6, 10 ... 번째 값들이 국가 이름
    if table_rows[currency_codes_index].text == '': # 화폐가 비어있으면 리스트에 입력 하지 않음
        continue
    currency_codes.append(table_rows[currency_codes_index].text)

    print("Hello, I guess you want to know a currency code of the country you selected by number.\n Please, type a number of the country you want to know.")

    # 국가 리스트 출력
    for country_index in range(0, len(name_countries)):
    print(f"# {country_index} {name_countries[country_index]}")

    # 입력 예외 처리
    while True: 
    input_number = input("# ")
    if input_number.isalpha(): # 문자열이면
        print("Your input data is not a number.\nPlease, re-input your number in the country index")
    elif input_number.isdigit(): # 숫자이면
        input_number = int(input_number) # 입력값 숫자로 변환
        if len(name_countries) < input_number or input_number < 0 : # 숫자가 국가 리스트 범위 밖이면
        print("Yout input data is not in range of the country index.\nPlease, re-input your number in the country index")
        else: # 입력값이 숫자이고, 유효 범위 안이면
        break

    # 최종 결과(화폐 코드) 출력
    print(f"{name_countries[int(input_number)]}'s currency code is {currency_codes[int(input_number)]}")

    ```

4. 정답

5. 참고
    - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautiful-soup-documentation)
    - [find_next_siblings() and find_next_sibling()](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-next-siblings-and-find-next-sibling) -> 이거 안 썼다! 두둥?!
    - [스트링 첫글자만 대문자, 나머지는 소문자로 바꾸기](https://hashcode.co.kr/questions/695/%EC%8A%A4%ED%8A%B8%EB%A7%81%EC%97%90-%EB%8B%A8%EC%96%B4-%EC%B2%AB-%EA%B8%80%EC%9E%90%EB%A5%BC-%EB%8C%80%EB%AC%B8%EC%9E%90%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EA%B3%A0%EC%8B%B6%EC%8A%B5%EB%8B%88%EB%8B%A4)
    - [파이썬 while문](https://wikidocs.net/21)
    - [파이썬 문자열 체크 - isalpha, isdigit](https://m.blog.naver.com/PostView.nhn?blogId=lee95292&logNo=221201880034&proxyReferer=https:%2F%2Fwww.google.com%2F)
    - [파이썬 문자열을 숫자로 변환](http://mwultong.blogspot.com/2007/01/python-int-long-float-string-to-number.html)
    - [과제에 사용된 국가 - 화폐 코드 사이트](https://www.iban.com/currency-codes)
