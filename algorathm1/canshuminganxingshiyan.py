import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

def quanzhong():
    precision = [0,0,0,0]
    TP = [43258,45727 - (46136 - 43258),43569 - (46136 - 43258),41522 - (46136 - 43258)]
    FP = [2301,2312 - (2453 - 2301),2035- (2453 - 2301),1682- (2453 - 2301)]
    for i in range(4):
        precision[i] = TP[i] / (TP[i] + FP[i])
    print("TP: {} \nFP: {} \nprecision: {}".format(TP, FP, precision))

def widowsize():
    f1_score = np.copy([0.8232, 0.8571, 0.8421, 0.8377, 0.8354])
    precision = np.copy([0.93657, 0.9495, 0.9397, 0.9375, 0.9323])
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
    r = x + width  # [5 + width, 12 + width, 20 + width, 30 + width, 50 + width]
    # 金牌图形
    plt.bar(p, precision, width=width, color='powderblue', label='Precision')
    # 银牌图形
    plt.plot(x + width / 2, f1_score, 'orange', marker='*', linewidth=1, label='F1_Score')
    plt.bar(r, recall, width=width, color='lightsteelblue', label='Recall')
    plt.xticks(x + width / 2, labels=w)
    plt.xlabel('窗口大小', fontsize=11)
    plt.ylabel('数值', fontsize=11)
    plt.legend(fontsize=9)
    plt.ylim(0.6, 1.1)
    plt.show()

def latentsize():
    f1_score = np.copy([0.8252, 0.8301, 0.8377, 0.8571, 0.8234])
    precision = np.copy([0.93657, 0.9397, 0.9375, 0.9495, 0.9323])
    recall = np.empty(5)
    for i in range(5):
        recall[i] = f1_score[i] * precision[i] / (2 * precision[i] - f1_score[i])
    w = [5, 10, 20, 40, 100]
    x = np.arange(len(w))
    width = 0.2
    # _______________确定x起始位置
    # f1起始位置
    p = x
    # auc的起始位置
    r = x + width  # [5 + width, 12 + width, 20 + width, 30 + width, 50 + width]
    plt.bar(p, precision, width=width, color='powderblue', label='Precision')
    # 银牌图形
    plt.plot(x + width / 2, f1_score, 'orange', marker='*', linewidth=1, label='F1_Score')
    plt.bar(r, recall, width=width, color='lightsteelblue', label='Recall')
    plt.xticks(x + width / 2, labels=w)
    plt.xlabel('潜空间大小', fontsize=11)
    plt.ylabel('数值', fontsize=11)
    plt.legend(fontsize=9)
    plt.ylim(0.6, 1.1)
    plt.show()

if __name__ == '__main__':
    quanzhong()