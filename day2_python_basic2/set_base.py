# 1. 创建字典
student = {"name": "Bob", "age": 22, "major": "Computer Science"}

# 2. 增：添加新键值对
student["gender"] = "male"
student["score"] = 90

# 3. 改：修改已有键的值
student["age"] = 23
student["score"] = 95

# 4. 查：访问值、判断键是否存在
print("=== 字典查询结果 ===")
print("姓名：" + student["name"])
print("年龄：", student.get("age", "未知"))  # get()避免键不存在时报错
print("是否包含major键:", "major" in student)

# 5. 删：删除键值对
student.pop("gender")  # 删除指定键
# student.clear()  # 清空整个字典（按需使用）

# 6. 遍历字典
print("\n=== 遍历字典所有键值对 ===")
for key, value in student.items():
    print(f"{key}: {value}")

# 7. 合并两个字典
other_info = {"school": "XYZ University", "grade": "Junior"}
student.update(other_info)
print("\n=== 合并后字典 ===")
print(student)