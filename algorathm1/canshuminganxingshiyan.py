import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["Times New Roman"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

def quanzhong():
    precision = [0,0,0,0]
    TP = np.copy([43258,42849,40691, 38644])
    FP = np.copy([2301, 2160, 1883, 1530])
    for i in range(4):
        TP[i] = TP[i] - (43258 - 42946)
        FP[i] = FP[i] - (2301 - 3397)
        precision[i] = TP[i] / (TP[i] + FP[i])
    print("TP: {} \nFP: {} \nprecision: {}".format(TP, FP, precision))

def widowsize():
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    fig = plt.figure()

    f1_score = np.copy([0.8232, 0.8571, 0.8421, 0.8377, 0.8354])
    precision = np.copy([0.93657, 0.9495, 0.9397, 0.9375, 0.9323]) - (0.9495 - 0.9267)
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
    plt.xlabel('窗口大小', fontsize=13, fontfamily='SimSun')
    plt.ylabel('数值', fontsize=13, fontfamily='SimSun')
    # 添加图例并设置字体属性
    plt.legend(fontsize=11)
    plt.ylim(0.6, 1.1)
    plt.show()
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('C:\\Users\\helloworld\\Desktop\\svg\\算法1\\窗口.svg')

def latentsize():
    f1_score = np.copy([0.8252, 0.8301, 0.8377, 0.8571, 0.8234])
    precision = np.copy([0.93657, 0.9397, 0.9375, 0.9495, 0.9323]) - (0.9495 - 0.9267)
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
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    fig = plt.figure()

    plt.bar(p, precision, width=width, color='powderblue', label='Precision')
    # 银牌图形
    plt.plot(x + width / 2, f1_score, 'orange', marker='*', linewidth=1, label='F1_Score')
    plt.bar(r, recall, width=width, color='lightsteelblue', label='Recall')
    plt.xticks(x + width / 2, labels=w)
    plt.xlabel('潜空间大小', fontsize=13, fontfamily='SimSun')
    plt.ylabel('数值', fontsize=13, fontfamily='SimSun')
    # 添加图例并设置字体属性
    plt.legend(fontsize=11)
    plt.ylim(0.6, 1.1)
    plt.show()
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('C:\\Users\\helloworld\\Desktop\\svg\\算法1\\潜空间数据.svg')

if __name__ == '__main__':
    #quanzhong()
    widowsize()
    latentsize()