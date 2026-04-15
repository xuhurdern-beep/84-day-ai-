# 简易计算器
print("=== 简易计算器 ===")
print("支持运算：+ 加、- 减、* 乘、/ 除")

# 1. 获取两个数字
try:
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    op = input("请输入运算符(+ - * /):")

    # 2. 根据运算符计算
    if op == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif op == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif op == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif op == "/":
        if num2 == 0:
            print("错误!除数不能为0")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("输入错误！请输入正确的运算符(+ - * /)")
except ValueError:
    print("输入错误！请输入有效的数字")