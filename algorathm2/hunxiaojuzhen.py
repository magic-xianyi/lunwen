import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
if __name__ == '__main__':
    total = 449919 - 12
    TP = 43258 #真阳
    precision = 0.9495
    recall = 0.7811
    FP = int(round((1 - precision) * TP / precision))  # 假阴
    FN = int(round((1 - recall) * TP / recall))  #假阳
    TN = total - TP - FP - FN #真阴
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1_score = 2 * precision * recall / (precision + recall)
    print("total: {} \nprecision: {} \nrecall: {} \nf1_score: {}".format(total, precision, recall, f1_score))
    print("TP: {} \nTN: {} \nFP: {} \nFN: {}".format(TP, TN, FP, FN))
    #对比实验的数据表的数据
    f1_score = np.copy([0.8201, 0.8318, 0.8058, 0.8571])
    precision = np.copy([0.9113, 0.9288, 0.8976, 0.9495])

    recall = np.empty(4)
    for i in range(4):
        recall[i] = f1_score[i] * precision[i] / (2 * precision[i] - f1_score[i])

    print("recall: {} \nprecision: {} \nf1_score: {}".format(recall, precision, f1_score))
    # 创建混淆矩阵
    confusion_matrix = np.array([[TN, FP],
                                 [FN, TP]])
    # 使用seaborn绘制混淆矩阵热图
    fig = plt.figure()
    sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['正常', '异常'],
                yticklabels=['正常', '异常'], annot_kws = {"size": 12})
    plt.xlabel('预测标签', fontsize=13)
    plt.ylabel('真实标签', fontsize=13)
    plt.show()
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('D:\\桌面\\svg\\算法2\\混淆矩阵.svg')

