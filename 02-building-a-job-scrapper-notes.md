# Building a < something on the web > scrapper
## Main function of this scrapper is ... 
> ���� ���� �������� Ư�� �˻� ��� ����Ʈ�� ���� ���������Ʈ�� �ϳ��ϳ� �����Ͽ� �����Ѵ�.

### Flow
1. ������Ʈ html ���� BeautifulSoup�� ���� �����´�.
2. ������ html���� ���ϴ� ����(���� �̸�, ȸ�� �̸�, ���ϴ� ���, ���� ��ũ)�� �����Ͽ� ��ųʸ��� ������ش�.
3. csv ������ �����Ͽ� ������ �����͸� �Է��Ѵ�.

### ����, �̷�
1. CSV (Comma Seperated Values)
   - �޸��� �������� ��� ���� ������.
2. CSV ����� ����� �� �ִ� ���̽� ���, `import csv`
   - ������ �� �� ��� ���� `file = open("jobs.csv", mode="???")`
     - ���� ��� `mode = "w"` �� ����� ������ csv ������ �� ���·� ���� ���� ���� �����Ѵ�.
     - `writer()`
        ```python
        file = open("jobs.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow("title", "company", "location", "link")
        return 
        ```
     -  

### Tips
1. ��� ��Ҹ� ã����, ���� �������� ã���� �ʰ� ���ִ� �޼���, �Ӽ� `recursive = False`
2. ����Ʈ�� ���� ���� �� ������ �������� �˰� �ִٸ� `unpacking value`�� �Ẹ��. ������ ��ǥ�� �� �� �����Ͽ� �ٷ� ������ �� �ִ�.
3. `\r`�� `\n`ó�� ���ο� ���� ����� �����̴�.
4. `��ųʸ�Ÿ���̸�.values()` �� ��ųʸ��� value ���鸸 �����´�. ������ �̴�� �������� ������ Ÿ���� `dict_values`�� �ȴ�. �̰��� ����Ʈ�� ������ַ��� `list(��ųʸ�Ÿ���̸�.values()))` �� �����ؾ� �Ѵ�.

```python
def extract_jobs(html):
    company, location = html.find("div", {"class": "-title"}).find("h2").find("a")["title"]
    company_row = html.find("div" , {"class": "-company"}).find_all("span", recursive = False)

    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\r").strip("\n")
    return {"title": title, 'company': company, 'location': location}
```
