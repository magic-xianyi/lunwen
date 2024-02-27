import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':
    name = ['TranAD', 'THOC', 'USAD', 'ISBGAT']
    f1_score = [0.8254, 0.8421, 0.8452, 0.8571]
    auc = [0.8315, 0.8821, 0.8948, 0.9122]
    # 1.将x轴转换为数值
    x = np.arange(len(name))
    # 2.设置图形的宽度
    width = 0.2
    # _______________确定x起始位置
    # f1起始位置
    f1 = x
    # auc的起始位置
    ac = x + width
    # 金牌图形
    plt.bar(f1, f1_score, width=width, color='powderblue', label='F1_Score')
    # 银牌图形
    plt.bar(ac, auc, width=width, color='lightsteelblue', label='AUC')
    plt.xticks(x + width, labels=name)
    plt.legend()
    plt.ylim(0.8, 1)
    plt.show()