#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: deal_xls.py
@time: 2019/7/3 13:09
"""
import xlrd
import xlwt
from xlutils.copy import copy


def createxls():
    # 创建一个workbook 设置编码
    wbk = xlwt.Workbook(encoding='utf-8')
    # 添加一个sheet对象
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)  # 第二个参数用于确认同一个cell单元是否可以重设值
    sheet.write(0, 0, 'sometext')  # 往指定单元格写入数据
    sheet.write(0, 0, 'overwrite')  # 覆盖写入，需要cell_overwrite_ok=True
    # 设定单元格风格，指定字体格式等
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = True
    font.height = 356
    style.font = font
    borders = xlwt.Borders()
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN

    alignemtn = xlwt.Alignment()
    alignemtn.horz = xlwt.Alignment.HORZ_CENTER
    alignemtn.horz = xlwt.Alignment.VERT_CENTER
    style.alignment = alignemtn
    # 保存
    sheet.write(0, 1, 'text', style)
    wbk.save('../dist/Excel_test.xls')


def readxls():
    # 打开Excel文件读取数据

    workbook = xlrd.open_workbook('../dist/Excel_test.xls')
    # 打印所有的sheet列出所有的sheet名字
    print(workbook.sheet_names())
    # 根据sheet索引或者名称获取sheet内容
    Data_sheet = workbook.sheets()[0]
    # Data_sheet = workbook.sheet_by_index(1)
    # Data_sheet = workbook.sheet_by_name(u'Charts')
    # 获取sheet名称、行数和列数
    print(Data_sheet.name, Data_sheet.nrows, Data_sheet.ncols)
    # 获取整行和整列的值（列表）
    rows = Data_sheet.row_values(0)  # 获取第一行内容
    cols = Data_sheet.col_values(1)  # 获取第二列内容
    print(rows)
    print(cols)
    # 获取单元格内容的数据类型
    # 相当于在一个二维矩阵中取值
    # （row,col）-->(行,列)
    cell_A1 = Data_sheet.cell(0, 0).value  # 第一行第一列坐标A1的单元格数据

    # cell_C1 = Data_sheet.cell(0,2).value # 第一行第三列坐标C1的单元格数据

    # cell_B1 = Data_sheet.row(0)[1].value # 第1行第2列

    # cell_D2 = Data_sheet.col(3)[1].value # 第4列第2行

    # 检查单元格的数据类型

    # ctype的取值含义

    # ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

    print(Data_sheet.cell(4, 0).ctype)

    # 读取excel中单元格内容为日期的方式

    date_value = xlrd.xldate_as_tuple(Data_sheet.cell_value(4, 0), workbook.datemode)

    print(date_value)  # -->(2017, 9, 6, 0, 0, 0)

    print('%d:%d:%d' % (date_value[3:]))  # 打印时间

    print('%d/%02d/%02d' % (date_value[0:3]))  # 打印日期


def writeData():
    xls = xlrd.open_workbook('../dist/change.xls')
    table = xls.sheet_by_index(0)
    all_data = []
    for n in range(1, table.nrows):
        comp = table.cell(n, 1).value
        price = table.cell(n, 3).value
        weight = table.cell(n, 4).value
        data = {'camp': comp, 'weight': weight, "price": price}
        all_data.append(data)


def changexls():
    newbook = xlwt.Workbook()
    worksheet = newbook.add_sheet('newsheet')
    worksheet.write(0, 0, 'test')
    newbook.save("../dist/change.xls")


def userstyles():
    testwork = xlrd.open_workbook("../dist/change.xls", formatting_info=True)
    tee = testwork.sheet_by_index(0)
    newexls = copy(tee)
    newsheet = newexls.get_sheet(0)
    newexls.write(1, 2, 12)
    newexls.write(1, 2, 12)
    newexls.write(1, 2, 12)
    newexls.write(1, 2, 12)
    newexls.write(1, 2, 12)
    newexls.save("../dist/userstylees.xls")


if __name__ == '__main__':
    createxls()
    # readxls()
    # changexls()
    # userstyles()
