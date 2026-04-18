import csv  # 导入csv模块，处理csv文件

def count_file_lines(file_path, encoding="utf-8"):
    """
    读取文件（支持txt/csv），统计总行数和有效行数，处理所有异常
    :param file_path: 文件路径（相对/绝对）
    :param encoding: 文件编码，默认utf-8
    :return: 有效行数，出错返回None
    """
    try:
        # 1. 用with打开文件，自动管理生命周期
        with open(file_path, "r", encoding=encoding) as f:
            # 2. 读取所有行，返回列表（每个元素是一行，带\n）
            all_lines = f.readlines()
            # 3. 统计总行数：直接取列表长度
            total_lines = len(all_lines)
            # 4. 统计有效行数：过滤空行（strip后为空的行）
            valid_lines = [line for line in all_lines if line.strip()]
            valid_count = len(valid_lines)

            # 5. 打印结果
            print(f"✅ 文件 {file_path} 读取成功！")
            print(f"📊 总行数（含空行）：{total_lines}")
            print(f"📊 有效行数（去除空行）：{valid_count}")
            return valid_count

    # 捕获对应异常，给出明确提示
    except FileNotFoundError:
        print(f"❌ 错误：文件 {file_path} 不存在，请检查路径！")
    except PermissionError:
        print(f"❌ 错误：无 {file_path} 的读写权限！")
    except UnicodeDecodeError:
        print(f"❌ 错误：文件编码不是 {encoding}，请检查编码格式！")
    except IsADirectoryError:
        print(f"❌ 错误：{file_path} 是文件夹，不是文件！")
    except Exception as e:
        print(f"❌ 未知错误：{str(e)}")

    return None


# CSV专用统计函数（针对表格数据优化，可选）
def count_csv_lines(file_path, encoding="utf-8", skip_header=False):
    """
    统计CSV文件行数，支持跳过表头
    :param skip_header: 是否跳过表头行，默认False
    """
    try:
        with open(file_path, "r", encoding=encoding, newline="") as f:
            reader = csv.reader(f)
            all_rows = list(reader)
            total_rows = len(all_rows)
            # 过滤空行（行内无有效内容）
            valid_rows = [row for row in all_rows if any(cell.strip() for cell in row)]
            valid_count = len(valid_rows)

            # 若跳过表头，有效行数-1
            if skip_header and valid_count > 0:
                valid_count -= 1

            print(f"✅ CSV文件 {file_path} 读取成功！")
            print(f"📊 总行数（含表头/空行）：{total_rows}")
            print(f"📊 有效数据行数（去除空行）：{valid_count}")
            return valid_count

    except FileNotFoundError:
        print(f"❌ 错误：CSV文件 {file_path} 不存在！")
    except Exception as e:
        print(f"❌ 错误：{str(e)}")
    return None


# 主入口：测试代码（只有直接运行文件时执行，延续Day3的__name__知识）
if __name__ == "__main__":
    # 测试1：正常txt文件（提前在同文件夹建test.txt，加几个空行）
    print("=== 测试TXT文件 ===")
    count_file_lines(r"day4_csv_txt\test.txt")

    # 测试2：不存在的文件（验证异常处理）
    print("\n=== 测试不存在的文件 ===")
    count_file_lines(r"day4_csv_txt\not_exist.txt")

    # 测试3：正常CSV文件（提前建data.csv）
    print("\n=== 测试CSV文件 ===")
    count_csv_lines(r"day4_csv_txt\data.csv", skip_header=True)