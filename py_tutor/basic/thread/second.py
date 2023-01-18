#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: deal_csv.py
@time: 2022/7/21 21:15
"""
import os
import threading
import time

total = 1000
folder = 'e:/tmp/py'


def action(num: int):

    with open(folder+os.path.sep + str(num) + ".txt", 'wb') as f:
        f.write("num".encode())

    # time.sleep(1)


def main():
    vehicles = []  # 新建车辆组
    for num in range(total):
        vehicle = threading.Thread(target=action, args=(num,))  # 新建车辆
        vehicles.append(vehicle)  # 添加车辆到车辆组中

    for vehicle in vehicles:
        vehicle.daemon = True
        vehicle.start()  # 分别启动车辆

        # vehicle.join()  # 分别检查到站车辆


def single():
    for num in range(total):
        action(num)


if __name__ == "__main__":
    if not os.path.exists(folder):
        os.mkdir(folder)
    main_time = time.time()
    main()
    main_end = time.time()
    print("Duration time: %0.3f" % (main_end - main_time))
    single_time = time.time()
    single()
    single_end = time.time()
    print("duration time: %0.3f" % (single_end - single_time))
    if   os.path.exists(folder):
        os.remove(folder)
