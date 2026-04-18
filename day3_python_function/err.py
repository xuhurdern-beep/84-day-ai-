def max_num(list1):
    try:
        if not list1:
            raise ValueError("列表不能为空")
        # ... 找最大值逻辑
    except ValueError as e:
        print(1)
          # 重新抛出异常，让上层代码处理 

if __name__ == "__main__":
    list1 = []
    print(max_num(list1))
