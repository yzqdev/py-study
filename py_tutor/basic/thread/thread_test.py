import threading
import time
import unittest

start = time.time()
people = 500  # 假设有500个人


def action(num):
    global people
    while people > 0:
        people -= 50  # 每次运输50人
        print("车辆编号：%d, 当前车站人数：%d" % (num, people))
        time.sleep(1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        num = 1  # 车辆编号
        action(num)
        end = time.time()
        print("Duration time: %0.3f" % (end - start))

    def test_single_thread(self):
        num = 1  # 车辆编号
        vehicle = threading.Thread(target=action, args=(num,))  # 新建车辆
        vehicle.start()  # 启动车辆
        vehicle.join()  # 检查到站车辆

        end = time.time()
        print("Duration time: %0.3f" % (end - start))

    def test_multi_thread(self):

        vehicles = []  # 新建车辆组
        for num in range(5):
            vehicle = threading.Thread(target=action, args=(num,))  # 新建车辆
            vehicles.append(vehicle)  # 添加车辆到车辆组中

        for vehicle in vehicles:
            vehicle.start()  # 分别启动车辆

        for vehicle in vehicles:
            vehicle.join()  # 分别检查到站车辆
        end = time.time()
        print("Duration time: %0.3f" % (end - start))


if __name__ == '__main__':
    unittest.main()
