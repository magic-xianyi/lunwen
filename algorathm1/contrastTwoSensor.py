import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':

    name = ['THOC', 'USAD', 'TranAD', 'AGAE']
    f1_score1 = np.copy([0.8421, 0.8077, 0.8254, 0.8571])
    f1_score2 = np.copy([0.7952, 0.7665, 0.7787, 0.84])
    # 1.将x轴转换为数值
    x = np.arange(len(name))
    # 2.设置图形的宽度
    width = 0.2
    # _______________确定x起始位置
    pr = x
    # auc的起始位置
    re = x + width
    f1 = x + 2 * width
    plt.bar(re, f1_score1, width=width, color='lightsteelblue', label='AIT504')
    plt.bar(f1, f1_score2, width=width, color='wheat', label='PIT503')
    plt.xticks(x + 1.5*width, labels=name)
    plt.xlabel('模型', fontsize=12)
    plt.ylabel('F1_Score', fontsize=12)
    plt.legend()
    plt.ylim(0.4, 1.2)
    plt.show()