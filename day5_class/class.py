# ------------------------------
# 1. 学生类（基础版）
# ------------------------------
class Student:
    # 构造方法：初始化学生的属性
    def __init__(self, name, student_id, age, major):
        self.name = name          # 姓名
        self.student_id = student_id  # 学号
        self.age = age            # 年龄
        self.major = major        # 专业
        self.score = 0            # 成绩，默认初始为0

    # 方法：学习行为
    def study(self, course):
        print(f"学生{self.name}正在学习{course}课程...")

    # 方法：考试行为，修改成绩
    def take_exam(self, course, score):
        self.score = score
        print(f"学生{self.name}参加了{course}考试，成绩为{self.score}分")

    # 方法：自我介绍
    def introduce(self):
        print(f"大家好，我叫{self.name}，今年{self.age}岁，学号是{self.student_id}，专业是{self.major}")


# ------------------------------
# 2. 机器人类（带继承版，复用设备父类）
# ------------------------------
# 父类：通用设备类
class Device:
    def __init__(self, model, power=100):
        self.model = model  # 设备型号
        self.power = power  # 设备电量，默认100%

    # 通用方法：充电
    def charge(self):
        self.power = 100
        print(f"{self.model}设备已充满电，当前电量：{self.power}%")

# 子类：机器人，继承Device父类
class Robot(Device):
    def __init__(self, model, task, power=100):
        # 调用父类的构造方法，复用model和power属性
        super().__init__(model, power)
        self.task = task  # 机器人的任务，自己扩展的属性

    # 方法：工作行为，消耗电量
    def work(self):
        if self.power <= 0:
            print(f"{self.model}电量不足，无法工作，请先充电！")
            return
        self.power -= 20
        print(f"{self.model}正在执行{self.task}任务，剩余电量：{self.power}%")

    # 方法：自我介绍
    def introduce(self):
        print(f"我是{self.model}机器人，我的任务是{self.task}，当前电量：{self.power}%")


# ------------------------------
# 主入口：测试代码（只有直接运行文件时执行）
# ------------------------------
if __name__ == "__main__":
    print("=== 测试学生类 ===")
    # 创建学生对象
    student1 = Student(name="张三", student_id="2023001", age=19, major="计算机科学")
    # 调用学生方法
    student1.introduce()
    student1.study("Python编程")
    student1.take_exam("Python编程", 95)

    print("\n=== 测试机器人类 ===")
    # 创建机器人对象
    robot1 = Robot(model="R2-D2", task="打扫卫生", power=60)
    # 调用机器人方法
    robot1.introduce()
    robot1.work()
    robot1.work()
    robot1.work()
    robot1.charge()  # 调用父类的充电方法
    robot1.work()