# For Scrapper Online
## Flask
```python
from flask import Flask
app = Flash("SuperScrapper")
@app.route("/")
def home():
    return "Hello! Welcome to my house!"

@app.route("/contact") # 데코레이터(@)는 바로 아래 있는 '함수'를 실행시킨다.
def contact_or_whatever(): #라우트와 함수이름이 같을 필요 없다.
     return "Contact me!"

app.run(host="0.0.0.0")
```