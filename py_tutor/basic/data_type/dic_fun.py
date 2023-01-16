#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: dic_fun.py
@time: 2023/1/8 13:48
"""

from colorama import Fore,Back
def main():
    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
    }
    for key, value in user_0.items():
        print("\nKey: " + key)
        print("Value: " + value)
    for key in user_0.keys():
        print(f"key=>{key}")
    print(f"{Fore.CYAN}--------------------下面是排序sorted-------------------------")
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for name in sorted(favorite_languages.keys()):
        print(name.title() + ", thank you for taking the poll.")

    print("The following languages have been mentioned:")
    for language in set(favorite_languages.values()):
        print(language.title())
    print(f"{Fore.YELLOW}--------------------下面是字典列表-------------------------")
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}
    aliens = [alien_0, alien_1, alien_2]
    for alien in aliens:
        print(alien)

def slice_fun():
    name = 'My name is Mike'
    print(name[0])
    'M'
    print(name[-4])
    'M'
    print(name[11:14])  # from 11th to 14th, 14th one is excluded
    'Mik'
    print(name[11:15])  # from 11th to 15th, 15th one is excluded
    'Mike'
    print(name[5:])
    'me is Mike'
    print(name[:5])
    for i in range(1, 10):
        for j in range(1, 10):
            print('{} X {} = {}'.format(i, j, i * j))


def write_file(name, msg):
    desktop_path = 'D:/tmp/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


def list_operate():
    a = []
    for i in range(1, 11):
        a.append(i)
    # 等同于
    b = [i for i in range(1, 11)]
    a = [i ** 2 for i in range(1, 10)]
    c = [j + 1 for j in range(1, 10)]
    k = [n for n in range(1, 10) if n % 2 == 0]
    z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
    # 字典推导式
    d = {i: i + 1 for i in range(4)}
    g = {i: j for i, j in zip(range(1, 6), 'abcde')}
    g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}
    print(z)


def dict_enum():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for num, letter in enumerate(letters):
        print(letter, 'is', num + 1)
if __name__ == "__main__":
    main()
