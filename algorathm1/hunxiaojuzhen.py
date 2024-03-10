import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
if __name__ == '__main__':
    TP = 11534 #真阳
    FP = 875   #假阳
    FN = 2971  #假阴
    TN = 97621 #真阴
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1_score = 2 * precision * recall / (precision + recall)

    print("recall: {} \nprecision: {} \nf1_score: {}".format(recall, precision, f1_score))
    f1_score = np.copy([0.8421, 0.8077, 0.8254, 0.8571])
    precision = np.copy([0.8897, 0.9475, 0.9423, 0.9295])
    recall = np.empty(4)
    for i in range(4):
        recall[i] = f1_score[i] * precision[i] / (2 * precision[i] - f1_score[i])

    print("recall: {} \nprecision: {} \nf1_score: {}".format(recall, precision, f1_score))
    # 创建混淆矩阵
    confusion_matrix = np.array([[TN, FP],
                                 [FN, TP]])
    # 使用seaborn绘制混淆矩阵热图
    sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['正常', '异常'],
                yticklabels=['正常', '异常'], annot_kws = {"size": 12})
    plt.xlabel('预测标签', fontsize=13)
    plt.ylabel('真实标签', fontsize=13)
    plt.title('混淆矩阵', fontsize=13)
    plt.show()
