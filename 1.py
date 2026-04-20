# 模拟 YOLOv8 验证输出结果
def print_detection_results():
    print(f"{'Class':<15} {'Images':<10} {'Instances':<10} {'Box(P':<10} {'R':<10} {'mAP50':<10} {'mAP50-95)':<10}")
    
    # 模拟汇总行
    print(f"{'all':<15} {'2535':<10} {'6898':<10} {'0.832':<10} {'0.788':<10} {'0.847':<10} {'0.532':<10}")
    
    # 修改后的病害类别行
    results = [
        ["Vertical_crack", "223", "234", "0.676", "0.651", "0.679", "0.259"],
        ["Horizontal_crack", "2519", "4542", "0.868", "0.797", "0.891", "0.581"],
        ["Diagonal_crack", "1278", "1339", "0.788", "0.786", "0.846", "0.507"],
        ["Pothole", "783", "783", "0.997", "0.917", "0.973", "0.782"]
    ]
    
    for row in results:
        print(f"{row[0]:<15} {row[1]:<10} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[6]:<10}")

    print("\nSpeed: 0.1ms preprocess, 1.1ms inference, 0.0ms loss, 0.7ms postprocess per image")

if __name__ == "__main__":
    print_detection_results()