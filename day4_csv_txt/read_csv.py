import csv  # 内置模块，直接用，无需安装

# 读取CSV
with open("day4_csv_txt\data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # 每一行是一个列表，对应表格的一行，如["姓名","年龄","专业"]

# 写入CSV（注意newline=""，Windows必加，避免多余空行）
data = [
    ["姓名", "年龄", "专业"],  # 表头
    ["张三", "20", "计算机"],
    ["李四", "21", "自动化"]
]
with open("day4_csv_txt\data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)  # 一次性写多行，writerow()写单行