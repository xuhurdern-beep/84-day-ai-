# 方式1：一次性读取全部（适合小文件）
with open("day4_csv_txt/test.txt", "r", encoding="utf-8") as f:
    content = f.read()  # 整个文件读成一个大字符串
    print(content)

# 方式2：按行读取（适合统计行数，节省内存）
with open("day4_csv_txt/test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 每一行是列表的一个元素，带换行符\n
    for line in lines:
        print(line.strip())  # strip() 去除首尾空白（换行、空格、制表符）

