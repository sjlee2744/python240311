import requests
from bs4 import BeautifulSoup

def naver_blog_crawler(search_keyword):
    # 네이버 블로그 검색 URL 생성
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"

    # HTTP GET 요청 보내고 응답 받기
    response = requests.get(url)
    
    # 응답이 성공적인지 확인
    if response.status_code == 200:
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')
        a
        # 블로그 검색 결과 목록 가져오기
        blog_list = soup.find_all('li', class_='bx')

        # 결과 출력
        for blog in blog_list:
            # 블로그명
            blog_name = blog.find('a', class_='sub_thumb').find('img')['alt']
            # 블로그 글 제목
            blog_title = blog.find('a', class_='api_txt_lines total_tit').text
            # 날짜
            blog_date = blog.find('span', class_='sub_time').text

            print("블로그명:", blog_name)
            print("글 제목:", blog_title)
            print("날짜:", blog_date)
            print()

    else:
        print("HTTP 요청이 실패하였습니다.")

# 키워드 입력
search_keyword = input("검색할 키워드를 입력하세요: ")

# 크롤링 실행
naver_blog_crawler(search_keyword)
