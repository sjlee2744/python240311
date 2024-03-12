text_file_path = 'sample.txt'
new_text_content = ''
target_word = '에러'
new_word = 'error'
with open(text_file_path,'r', encoding="utf-8") as f:
    lines = f.readlines() ## 기존 텍스트파일에 대한 내용을 모두 읽는다.
    for i, l in enumerate(lines):
        new_string = l.strip().replace(target_word,new_word)
        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'
                
with open(text_file_path,'w', encoding="utf-8") as f:
    f.write(new_text_content)
