# Building a < something on the web > scrapper
## Main function of this scrapper is ... 
> 복수 개의 페이지의 특정 검색 결과 리스트를 엑셀 스프레드시트에 하나하나 수집하여 나열한다.

### Flow
1. 웹사이트 html 정보 BeautifulSoup를 통해 가져온다.
2. 가져온 html에서 원하는 정보(직무 이름, 회사 이름, 일하는 장소, 지원 링크)를 추출하여 딕셔너리로 만들어준다.
3. csv 파일을 생성하여 추출한 데이터를 입력한다.

### 지식, 이론
1. CSV (Comma Seperated Values)
   - 콤마와 개행으로 행과 열을 구분함.
2. CSV 기능을 사용할 수 있는 파이썬 모듈, `import csv`
   - 파일을 열 때 모드 설정 `file = open("jobs.csv", mode="???")`
     - 쓰기 모드 `mode = "w"` 는 실행될 때마다 csv 파일을 빈 상태로 만든 다음 쓰기 시작한다.
     - `writer()`
        ```python
        file = open("jobs.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow("title", "company", "location", "link")
        return 
        ```
     -  

### Tips
1. 모든 요소를 찾지만, 깊이 들어가서까지 찾지는 않게 해주는 메서드, 속성 `recursive = False`
2. 리스트의 안의 값이 몇 개인지 무엇인지 알고 있다면 `unpacking value`를 써보자. 변수를 쉼표로 두 개 선언하여 바로 대입할 수 있다.
3. `\r`도 `\n`처럼 새로운 줄을 만드는 문자이다.
4. `딕셔너리타입이름.values()` 는 딕셔너리의 value 값들만 가져온다. 하지만 이대로 가져오면 데이터 타입이 `dict_values`가 된다. 이것을 리스트로 만들어주려면 `list(딕셔너리타입이름.values()))` 로 수정해야 한다.

```python
def extract_jobs(html):
    company, location = html.find("div", {"class": "-title"}).find("h2").find("a")["title"]
    company_row = html.find("div" , {"class": "-company"}).find_all("span", recursive = False)

    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\r").strip("\n")
    return {"title": title, 'company': company, 'location': location}
```
