def count_frequency(lst):
    """统计列表中元素的出现频率"""
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

# 测试代码
if __name__ == "__main__":
    test_list = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4, 3, "a", "b", "a"]
    result = count_frequency(test_list)
    print("=== 列表元素频率统计 ===")
    for element, count in result.items():
        #取出所有键值对进入元组
        print(f"{element}: {count} 次")