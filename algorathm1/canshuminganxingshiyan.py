import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':
    f1_score = np.copy([0.8232, 0.8571, 0.8421, 0.8377, 0.8354])
    precision = np.copy([0.90657, 0.9295, 0.9197, 0.9175, 0.9023])
    recall = np.empty(5)
    for i in range(5):
        recall[i] = f1_score[i] * precision[i] / (2 * precision[i] - f1_score[i])
    w = [5, 12, 20, 30, 50]



    x = np.arange(len(w))
    width = 0.2
    # _______________确定x起始位置
    # f1起始位置
    p = x
    # auc的起始位置
    r = x + width#[5 + width, 12 + width, 20 + width, 30 + width, 50 + width]
    # 金牌图形
    plt.bar(p, precision, width=width, color='powderblue', label='Precision')
    # 银牌图形
    plt.plot(x+width/2, f1_score, 'orange', marker='*', linewidth=1, label='F1_Score')
    plt.bar(r, recall, width=width, color='lightsteelblue', label='Recall')
    plt.xticks(x+width/2, labels=w)
    plt.xlabel('窗口大小', fontsize=11)
    plt.ylabel('数值', fontsize=11)
    plt.legend(fontsize=9)
    plt.ylim(0.6, 1)
    plt.show()