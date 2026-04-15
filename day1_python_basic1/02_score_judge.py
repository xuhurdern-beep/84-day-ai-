print("===成绩判断系统===")
score=int(input("请输入成绩："))
level=""
if score>=100 or score<0:
    print("输入成绩有误！")
elif score>=90:
    level="优秀"
elif score>=80:
    level="良好"
elif score>=60:
    level="及格"
else:
    level="不及格!"
print("===成绩判断结束===")
print(f"输入的成绩是：{score},{level}")