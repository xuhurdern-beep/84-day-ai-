# 列表操作
my_list = [1, 2, 3, "hello"]
my_list.append(4)  # 末尾添加元素
my_list[0] = 100   # 修改元素
print(my_list[1:3])  # 切片，输出[2, 3]
#不能取到my_list[3]

# 元组操作
my_tuple = (1, 2, 3, "hello")
print(my_tuple[0])  # 索引访问，输出1
# my_tuple[0] = 100  # 报错：元组不可修改

# 字典操作
my_dict = {"name": "Alice", "age": 20}
my_dict["gender"] = "female"  # 新增键值对
my_dict["age"] = 21           # 修改值
print(my_dict.items())        # 遍历所有键值对

# 集合操作
my_set = {1, 2, 3, 3}  # 自动去重，结果{1,2,3}
a = {1,2,3}
b = {3,4,5}
print(a & b)  # 交集{3}
print(a | b)  # 并集{1,2,3,4,5}

a=set()
print(type(a))  # 输出<class 'set'>，空集合需要使用set()创建