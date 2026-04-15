# break示例：遇到3就终止循环
for i in range(5):
    if i == 3:
        break
    print(i)  # 输出：0,1,2

# continue示例：跳过3，继续后续循环
for i in range(5):
    if i == 3:
        continue
    print(i)  # 输出：0,1,2,4