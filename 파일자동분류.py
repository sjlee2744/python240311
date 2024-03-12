import os
import shutil

# 다운로드된 폴더 경로
download_folder = "C:/Users/student/Downloads"

# 이동할 폴더들
folders = {
    "images": "C:/Users/student/Downloads/images",
    "data": "C:/Users/student/Downloads/data",
    "docs": "C:/Users/student/Downloads/docs",
    "archive": "C:/Users/student/Downloads/archive"
}

# 폴더 생성 또는 확인
for folder in folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# 파일 이동
for filename in os.listdir(download_folder):
    if filename.lower().endswith((".jpg", ".jpeg")):
        shutil.move(os.path.join(download_folder, filename), folders["images"])
    elif filename.lower().endswith((".csv", ".xlsx")):
        shutil.move(os.path.join(download_folder, filename), folders["data"])
    elif filename.lower().endswith((".txt", ".doc", ".pdf")):
        shutil.move(os.path.join(download_folder, filename), folders["docs"])
    elif filename.lower().endswith(".zip"):
        shutil.move(os.path.join(download_folder, filename), folders["archive"])

print("파일 이동이 완료되었습니다.")
