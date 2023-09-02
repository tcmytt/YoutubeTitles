# Đọc nội dung từ file a.txt
with open('video_titles.txt', 'r', encoding='utf-8') as file_a:
    lines = file_a.readlines()

# Đảo ngược danh sách các dòng
reversed_lines = reversed(lines)

# Ghi danh sách các dòng đã đảo ngược vào file b.txt
with open('video_titles_reversed.txt', 'w', encoding='utf-8') as file_b:
    file_b.writelines(reversed_lines)
