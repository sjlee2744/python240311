import re

def check_email(email):
    # 이메일 주소를 체크하는 정규식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 데이터
emails = [
    "user@example.com",
    "user123@gmail.com",
    "user.name@domain.co.kr",
    "user123_456@sub.domain.com",
    "123user@example.com",
    "user@123.com",
    "user@domain",
    "user@domain.",
    "user@-domain.com",
    "user@domain-.com"
]

# 샘플 데이터를 이용하여 이메일 주소를 체크하고 결과 출력
for email in emails:
    if check_email(email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")