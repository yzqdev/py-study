在sklearn中包含四种评价尺度，分别为mean_squared_error、mean_absolute_error、explained_variance_score 和 r2_score。

1、均方差（mean-squared-error）

![这里写图片描述](https://img-blog.csdn.net/20160420140624059)

2、平均绝对值误差（mean_absolute_error）

![这里写图片描述](https://img-blog.csdn.net/20160420140705013)

3、可释方差得分（explained_variance_score）
explained variation measures the proportion to which a mathematical model
accounts for the variation (dispersion) of a given data set

![这里写图片描述](https://img-blog.csdn.net/20160420140735716)

4、中值绝对误差（Median absolute error）

![这里写图片描述](https://img-blog.csdn.net/20160420140810341)

此种方法非常适应含有离群点的数据集

5、R2 决定系数（拟合优度）
![这里写图片描述](https://img-blog.csdn.net/20160420140839172)

它是表征回归方程在多大程度上解释了因变量的变化，或者说方程对观测值的拟合程度如何。
因为如果单纯用残差平方和会受到你因变量和自变量绝对值大小的影响，不利于在不同模型之间进行相对比较.而用拟合优度就可以解决这个问题。例如一个模型中的因变量:10000、20000…..，而另一个模型中因变量为1、2……，这两个模型中第一个模型的残差平方和可能会很大,而另一个会很小，但是这不能说明第一个模型就别第二个模型差。