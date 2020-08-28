# python web scrapper challenge for 2 weeks
## day 4
1. ���� ����:
2. ����:
3. ����
```python
import requests

def handle_url(url=""):
  url = url.strip()
  if url == "":
    return 1 # empty url
  elif ".com" not in url:
    return 2 # invalid url
  elif url.find("https://") == 0: # check https://
    return url
  elif  "https://" not in url:
    return ("https://" + url) 
  else:
    return 2 # invalid url

def answer_check():
  while(True):
    answer = input("Do you want to do this again? y/n  ")
    if answer == "n":
      print("program terminated")
      return 0
    elif answer == "y":
      return 1
    else:
      print("invalid answer, again please")

# main starts
print("Welcome to IsItDown.py!")
print("Please write a URL you want to check. (Separated by comma")
while(True):
  urls = input().split(",")
  for url in urls:
    url_input = url.strip()
    url = handle_url(url)
    if url == 1:
      print("empty url")
    elif url == 2:
      print(f"{url_input} is invalid url")
    else:
      try:
        if requests.get(url).status_code == 200:
          print(f"{url} is ONLINE")
      except: # when page is down  
        print(f"{url} is OFFLINE")
  answer = answer_check()
  if answer == 0:
    break
```

4. ����
- ���� ��ģ ��
  - ����� �κп��� �Է��� ��� lower()�� �ҹ���ȭ �ϴ� ��.
  - ��ȿ url Ȯ���� �� ���忡 '.'�� ������ �ȴٰ� �� ��. (��� ���� .com ���� ������ �ʴ´�) 
  - main()�� ����ϱ�

5. ����
   - [���Ϸ��÷���Ʈ(Bolilerplate code)?](https://en.wikipedia.org/wiki/Boilerplate_code)
   - [���� �� ����� �Է� ó��](https://gosmcom.tistory.com/108)
   - [���̽� ���� ó��](https://wikidocs.net/30)
   - [Requests Module - Response Status Codes](https://requests.readthedocs.io/en/master/user/quickstart/#response-status-codes)
   - [���̽㿡�� do/while ������ ����](https://woogyun.tistory.com/519)
   - [���̽㿡�� Ư�� ���� ã��](https://dpdpwl.tistory.com/119)
   - [���̽㿡�� ���ڿ� ���� �����ϱ�](https://c10106.tistory.com/3742)
