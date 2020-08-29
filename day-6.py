import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

# �Է� ���� ó��
def input_country_number():
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
  return input_number

def input_amount_money():
  while True:
    input_number = input("Amount: ")
    if input_number.isalpha():
      print("Your input data is not a number.\nPlease, re-input your amount of money to change")
    elif input_number.isdigit():
      break
  return int(input_number)



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

print("WELECOME TO CURRENCY CONVERT PROGRAM")

# ���� ����Ʈ ���
for country_index in range(0, len(name_countries)):
  print(f"# {country_index} {name_countries[country_index]}")


print("WHERE ARE YOU FROM? TYPE A COUNTRY BY NUMBER")
country_from = input_country_number()
print(f"{name_countries[country_from]}")

print("CHOOSE ANOTHER COUNTRY BY NUMBER")
country_to = input_country_number()
print(f"{name_countries[country_to]}")

print(f"HOW MANY <<{currency_codes[int(country_from)]}>> DO YOU WANT TO CONVERT TO <<{currency_codes[int(country_to)]}>> ?")

# �ݾ� �Է� �� ���� ó��
amount_money = input_amount_money()

# ȯ��
URL_CONVERT = f"https://transferwise.com/gb/currency-converter/{currency_codes[int(country_from)]}-to-{currency_codes[int(country_to)]}-rate?amount={amount_money}"
convert_result = requests.get(URL_CONVERT)
convert_soup = BeautifulSoup(convert_result.text, "html.parser")
convert_rate = float(convert_soup.find("span", {"class":"text-success"}).string)
converted_money = amount_money * convert_rate

# ȯ�� ��� ���
print(format_currency(amount_money, f"{currency_codes[int(country_from)]}", locale="ko_KR")+"  is  "+ format_currency(converted_money, f"{currency_codes[int(country_to)]}", locale="ko_KR"))
