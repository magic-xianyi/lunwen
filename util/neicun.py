import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':

    name = ['THOC', 'USAD', 'TranAD', 'ISBGAT']
    num = [6.25392, 1.40497, 3.89652, 3.09093]
    size = [2.43846, 0.54781, 1.51929, 1.20518]
    # 1.将x轴转换为数值
    x = np.arange(len(name))
    # 2.设置图形的宽度
    width = 0.2
    # _______________确定x起始位置
    # f1起始位置
    n = x
    # auc的起始位置
    ac = x + width
    # 金牌图形
    plt.bar(n, num, width=width, color='powderblue', label='参数量')
    # 银牌图形
    plt.bar(ac, size, width=width, color='lightsteelblue', label='内存消耗')
    plt.xticks(x + width, labels=name)
    plt.xlabel('模型', fontsize=11)
    plt.ylabel('数值', fontsize=11)
    plt.legend()
    #plt.ylim(0.8, 1)
    plt.show()