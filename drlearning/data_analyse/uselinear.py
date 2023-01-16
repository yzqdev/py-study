from sklearn.linear_model import LassoCV
from sklearn.linear_model import Lasso
import csv
import numpy as np
import matplotlib.pyplot as plt
# 读
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split

with open("data/alldatainit.csv", "r", encoding="utf-8") as f:
    pattern = {
        '东风': '0',
        '东北风': '1',
        '北风': '2',
        '西北风': '3',
        '西风': '4',
        '西南风': '5',
        '南风': '6',
        '严重污染': '8',
        '东南风': '7',
        '重度污染': '5',
        '中度污染': '4',
        '轻度污染': '3',
        '中': '2',
        '良': '1',
        '优': '0',
        '微风': '0',
        '1级': '1',
        '2级': '2',
        '3级': '3',
        '4级': '4',
        '5级': '5',
        '晴': '0',
        '阴': '1',
        '多云': '2',
        '小雨': '3',
        '中雨': '4',
        '大雨': '5',
        '暴雨': '6',
        '小雪': '3',
        '大雪': '5',
        '中雪': '4',
        '雷阵雨': '7',

        '雾': '3'
    }
    y = []
    reader = csv.reader(f)
    x = []
    i = 0
    for row in reader:
        # rep = [pattern[x] if x in pattern else x for x in row]
        # ro = np.array(rep)
        # data.append(rep)

        # row=np.array(row)
        if i < 1500:
            i = i + 1
            print('第%d组数' % i)
            print(row)
            x.append(row)

            labae = row[2]
            y.append(labae)

x = np.array(x, dtype="float32")
print('下面是训练集')

# 标签值
y = []
j = 0
ycsv = csv.reader(open('data/noy.csv', "r", encoding="utf-8"))
for yrow in ycsv:
    if j < 1500:
        j = j + 1
        y.append(yrow)
print(y)
y = np.array(y, dtype="float32")
clf = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=0)

# 训练集
clf.fit(x_train, y_train)

predictions = clf.predict(x_test)

for i, prediction in enumerate(predictions):
    print('预测值: %s, 实际值: %s' % (prediction, y_test[i]))
    # 这里需要实际值

print("训练集的结果是")

print(predictions)
print(predictions.data.shape)
print("输入")
print(str(x_test))

print(x_train.data.shape)
print(y_train.data.shape)
print('系数: \n', clf.coef_)
# print(cross_val_score(clf, x_train, y_train, cv=10))
print("均方误差: %.32f" % mean_squared_error(y_test, predictions))
# Explained variance score: 1 is perfect prediction
print('可释方差得分: %.32f' % r2_score(y_test, predictions))

print('拟合度值: %.32f' % clf.score(x, y))
# plt.scatter(x_test, y_test, color='black')
plt.scatter(y_test, predictions, color='blue', linewidth=0.5,label='test and predict')
plt.title('y_true and y_prediction')
plt.xlabel("y_true")
plt.ylabel("y_prediction")
plt.axis([0, 250, 0, 250])
plt.xticks(())
plt.yticks(())

plt.show()
