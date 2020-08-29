import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

# 입력 예외 처리
def input_country_number():
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

print("WELECOME TO CURRENCY CONVERT PROGRAM")

# 국가 리스트 출력
for country_index in range(0, len(name_countries)):
  print(f"# {country_index} {name_countries[country_index]}")


print("WHERE ARE YOU FROM? TYPE A COUNTRY BY NUMBER")
country_from = input_country_number()
print(f"{name_countries[country_from]}")

print("CHOOSE ANOTHER COUNTRY BY NUMBER")
country_to = input_country_number()
print(f"{name_countries[country_to]}")

print(f"HOW MANY <<{currency_codes[int(country_from)]}>> DO YOU WANT TO CONVERT TO <<{currency_codes[int(country_to)]}>> ?")

# 금액 입력 및 예외 처리
amount_money = input_amount_money()

# 환전
URL_CONVERT = f"https://transferwise.com/gb/currency-converter/{currency_codes[int(country_from)]}-to-{currency_codes[int(country_to)]}-rate?amount={amount_money}"
convert_result = requests.get(URL_CONVERT)
convert_soup = BeautifulSoup(convert_result.text, "html.parser")
convert_rate = float(convert_soup.find("span", {"class":"text-success"}).string)
converted_money = amount_money * convert_rate

# 환전 결과 출력
print(format_currency(amount_money, f"{currency_codes[int(country_from)]}", locale="ko_KR")+"  is  "+ format_currency(converted_money, f"{currency_codes[int(country_to)]}", locale="ko_KR"))
