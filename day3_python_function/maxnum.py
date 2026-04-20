from fibonacci import fibonacci 
def max_num(list1):

    if not list1:  # 处理空列表异常
        raise ValueError("列表不能为空")
    
    max1=float('-inf')  
    for i in list1:
        if i>max1:
            max1=i
    return max1

list1=[1,3,2,4,5]
print(f"斐波那契数列前10项：{fibonacci(10)}")
print(max_num(list1))