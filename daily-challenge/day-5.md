# python web scrapper challenge for 2 weeks
## day 5
1. ���� ��ǥ:

2. ����:

3. ����
   - ���� ������ ����,
        1. ���� �ε���(0���� ����)��  ���� ���(A���� ����, ȭ�� ������ ���ŵ�)�� ��µȴ�.
        2. ���� �ε����� �Է��ϸ� �� ������ ����ϴ� ȭ���� alpha-3 �ڵ带 ������ָ� �ȴ�.
   - ���� ����Ʈ
       - **table**���� �������� ���(���� �̸��� ȭ�� �ڵ�)�� **���** �����ͼ� �����ϴ���, �̴�.
       - key�� value�� �ִ� dictonary�� ���� �̸��� ȭ�� �ڵ带 �����ؾ� ���ڴ�.
    ```python
    import os
    import requests
    from bs4 import BeautifulSoup

    os.system("clear")
    URL = "https://www.iban.com/currency-codes"
    iban_result = requests.get(URL)
    iban_soup = BeautifulSoup(iban_result.text, "html.parser")
    table = iban_soup.find("tbody") # ���̺�
    table_rows = table.findAll("td") # ���̺� ������

    # ���� �̸��� ȭ�� �ڵ带 ������� ������ �� ����Ʈ �����
    name_countries = [];
    currency_codes = [];

    for name_country_index in range(0, len(table_rows), 4): # ������ td �� 0, 4, 8 ... ��° ������ ���� �̸�
    if table_rows[name_country_index+2].text == '': # ȭ�� ��������� ����Ʈ�� �Է� ���� ����
        continue
    name_countries.append(table_rows[name_country_index].text.capitalize()) # ���ڿ��� ��ȯ(text), ù���ڰ� �빮�ڷ� ��ȯ(capitalize())

    for currency_codes_index in range(2, len(table_rows), 4): # ������ td �� 2, 6, 10 ... ��° ������ ���� �̸�
    if table_rows[currency_codes_index].text == '': # ȭ�� ��������� ����Ʈ�� �Է� ���� ����
        continue
    currency_codes.append(table_rows[currency_codes_index].text)

    print("Hello, I guess you want to know a currency code of the country you selected by number.\n Please, type a number of the country you want to know.")

    # ���� ����Ʈ ���
    for country_index in range(0, len(name_countries)):
    print(f"# {country_index} {name_countries[country_index]}")

    # �Է� ���� ó��
    while True: 
    input_number = input("# ")
    if input_number.isalpha(): # ���ڿ��̸�
        print("Your input data is not a number.\nPlease, re-input your number in the country index")
    elif input_number.isdigit(): # �����̸�
        input_number = int(input_number) # �Է°� ���ڷ� ��ȯ
        if len(name_countries) < input_number or input_number < 0 : # ���ڰ� ���� ����Ʈ ���� ���̸�
        print("Yout input data is not in range of the country index.\nPlease, re-input your number in the country index")
        else: # �Է°��� �����̰�, ��ȿ ���� ���̸�
        break

    # ���� ���(ȭ�� �ڵ�) ���
    print(f"{name_countries[int(input_number)]}'s currency code is {currency_codes[int(input_number)]}")

    ```

4. ����

5. ����
    - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautiful-soup-documentation)
    - [find_next_siblings() and find_next_sibling()](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-next-siblings-and-find-next-sibling) -> �̰� �� ���! �ε�?!
    - [��Ʈ�� ù���ڸ� �빮��, �������� �ҹ��ڷ� �ٲٱ�](https://hashcode.co.kr/questions/695/%EC%8A%A4%ED%8A%B8%EB%A7%81%EC%97%90-%EB%8B%A8%EC%96%B4-%EC%B2%AB-%EA%B8%80%EC%9E%90%EB%A5%BC-%EB%8C%80%EB%AC%B8%EC%9E%90%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EA%B3%A0%EC%8B%B6%EC%8A%B5%EB%8B%88%EB%8B%A4)
    - [���̽� while��](https://wikidocs.net/21)
    - [���̽� ���ڿ� üũ - isalpha, isdigit](https://m.blog.naver.com/PostView.nhn?blogId=lee95292&logNo=221201880034&proxyReferer=https:%2F%2Fwww.google.com%2F)
    - [���̽� ���ڿ��� ���ڷ� ��ȯ](http://mwultong.blogspot.com/2007/01/python-int-long-float-string-to-number.html)
    - [������ ���� ���� - ȭ�� �ڵ� ����Ʈ](https://www.iban.com/currency-codes)
