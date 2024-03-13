# web1.py
#웹 크롤링

from bs4 import BeautifulSoup

#페이지를 로딩

page = open("test01.html" , "rt", encoding = "utf-8").read()

soup = BeautifulSoup(page, "html.parser")

#print(soup.prettify())

#문서의 P 태그 전체 검색

#print(soup.find_all("p"))

# print(soup.find_all("a"))
# print(soup.find("p"))
# 조건이 있는 경우 :<p class='outer-text'>
#print(soup.find_all("p", class_="outer-text"))
#attrs를 사용
#print(soup.find_all("p", attrs={"class":"outer-text"}))

# 태그 내부의 문자열만 가지고 오기

# for tag in soup.find_all("p"):
#     title = tag.text.strip()
#     title = title.replace("\n", "")
#     print(title)

print(soup.find(id="first"))
