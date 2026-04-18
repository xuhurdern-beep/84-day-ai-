# 覆盖写入（w模式：不存在则新建，存在则清空重写）
with open("day4_csv_txt/test.txt", "w", encoding="utf-8") as f:
    f.write("第一行内\n")  # \n 手动换行，否则内容挤在一行
    f.write("第二行内容\n")

# 追加写入（a模式：在文件末尾添加，不覆盖原内容）
with open("day4_csv_txt/test.txt", "a", encoding="utf-8") as f:
    f.write("追加的第三行\n")