#!/usr/bin/python
# -*-coding:utf-8-*-



from tempfile import *
def main():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='  ')
        print()
if __name__ == '__main__':
    main()