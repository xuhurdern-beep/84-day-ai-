import requests
import pandas as pd
import numpy as np

def fetch_and_analyze_data(url, save_path="day6_pip/data_analysis.csv"):
    """
    工具功能：
    1. 用requests获取网页数据（示例用公开API）
    2. 用pandas处理数据，numpy统计分析
    3. 保存结果到csv文件
    """
    try:
        # 1. 用requests获取数据（示例：获取公开的用户数据API）
        print("正在获取数据...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功（状态码200）
        data = response.json()  # 解析JSON数据

        # 2. 用pandas转换为表格数据
        df = pd.DataFrame(data)
        print("数据获取成功，共", len(df), "条记录")

        # 3. 用numpy进行统计分析（以用户ID为例）
        if "id" in df.columns:
            id_array = np.array(df["id"])
            print("\n=== 数据统计分析 ===")
            print("ID最小值：", np.min(id_array))
            print("ID最大值：", np.max(id_array))
            print("ID平均值：", np.mean(id_array))

        # 4. 用pandas保存数据到csv文件
        df.to_csv(save_path, index=False, encoding="utf-8")
        print(f"\n数据已保存到：{save_path}")
        print("工具执行完成！")

    except requests.exceptions.RequestException as e:
        print(f"网络请求错误：{e}")
    except Exception as e:
        print(f"未知错误：{e}")

if __name__ == "__main__":
    # 示例：调用公开的JSONPlaceholder API
    API_URL = "https://jsonplaceholder.typicode.com/users"
    fetch_and_analyze_data(API_URL)