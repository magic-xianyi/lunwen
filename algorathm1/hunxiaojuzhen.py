import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from matplotlib.backends.backend_svg import FigureCanvasSVG
import seaborn as sns
plt.rcParams["font.sans-serif"] = ["Times New Roman"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
if __name__ == '__main__':
    total = 449919 - 12
    TP = 42946 # 真阳
    precision = 0.9267
    recall = 0.7771
    FP = int(round((1 - precision) * TP / precision))  # 假阴
    FN = int(round((1 - recall) * TP / recall))  # 假阳
    TN = total - TP - FP - FN  # 真阴
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1_score = 2 * precision * recall / (precision + recall)
    print("total: {} \nprecision: {} \nrecall: {} \nf1_score: {}".format(total, precision, recall, f1_score))
    print("TP: {} \nFP: {} \nTN: {} \nFN: {}".format(TP, FP, TN, FN))

    #对比实验的数据表的数据
    f1_score = np.copy([0.8321, 0.8077, 0.8254, 0.8453])
    precision = np.copy([0.9097, 0.9255, 0.9223, 0.9267])
    recall = np.empty(4)
    for i in range(4):
        recall[i] = f1_score[i] * precision[i] / (2 * precision[i] - f1_score[i])

    print("recall: {} \nprecision: {} \nf1_score: {}".format(recall, precision, f1_score))
    # 创建混淆矩阵
    confusion_matrix = np.array([[TN, FP],
                                 [FN, TP]])
    # 创建一个图像
    fig = plt.figure()
    # 使用seaborn绘制混淆矩阵热图
    sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['正常', '异常'],
                yticklabels=['正常', '异常'], annot_kws={"size": 12})
    plt.xlabel('预测标签', fontsize=13, fontfamily='SimSun')
    plt.ylabel('真实标签', fontsize=13, fontfamily='SimSun')
    plt.xticks(fontsize=12, fontfamily='SimSun')
    plt.yticks(fontsize=12, fontfamily='SimSun')
    plt.show()
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('C:\\Users\\helloworld\\Desktop\\svg\\算法1\\混淆矩阵.svg')

