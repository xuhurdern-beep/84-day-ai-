def max_num(list1):
    try:
        if not list1:
            raise ValueError("列表不能为空")
        # ... 找最大值逻辑
    except ValueError as e:
        print(f"记录错误日志：{e}")
        raise  # 重新抛出异常，让上层代码处理