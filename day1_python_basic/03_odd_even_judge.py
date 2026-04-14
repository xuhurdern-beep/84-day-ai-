# 奇偶判断程序
print("=== 奇偶判断系统 ===")
# 1. 获取输入
num = int(input("请输入一个整数："))

# 2. 判断
if num % 2 == 0:
    print(f"{num} 是偶数")
else:
    print(f"{num} 是奇数")