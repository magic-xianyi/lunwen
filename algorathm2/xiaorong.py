import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
if __name__ == '__main__':
    precision = np.copy([0.9267, 0.9186, 0.9231, 0.8912]) - (0.9267 - 0.9495)
    f1_socre = np.copy([0.8414, 0.8331, 0.8312, 0.8135]) - (0.8414 - 0.8571)
    recall = np.empty(4)
    for i in range(4):
        precision[i] = format(precision[i], '.4f')
        f1_socre[i] = format(f1_socre[i], '.4f')
        recall[i] = format(f1_socre[i] * precision[i] / (2 * precision[i] - f1_socre[i]), '.4f')
    data = [recall, precision, f1_socre]
    columns = ('完整模型', '去除注意力机制', '去除相关性矩阵', '去除集成网络机制')
    rows = ['Recall', 'Precision', 'F1_Score']
    pltPD = pd.DataFrame(data, columns=columns, index=rows)
    # 按照model来进行汇总, 这里共有5个model
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(1, 1, 1)
    # 自定义颜色
    # colors = plt.cm.BuPu(np.linspace(0, 0.5, len(pltPD.index.values)))
    colors = ['gainsboro', 'wheat','lightsteelblue']
    n_rows = len(pltPD.index.values)
    # 设置barchart的x轴
    w = 0.3
    index = np.arange(len(pltPD.columns.values)) * n_rows * w * 1.5  # 5个model, 所以是5
    # 首先绘制柱状图
    for row in range(n_rows):
        plt.bar(index + row * w, pltPD.values[row], width=w, align='center', color=colors[row],
                label=pltPD.index.values[row])
    # 添加图例
    ax.legend(fontsize=16)
    cellColours = [['gainsboro', 'white', 'gainsboro', 'white'],
                   ['white', 'wheat', 'white', 'wheat'],
                   ['lightsteelblue', 'white', 'lightsteelblue', 'white']]
    # 添加一个表格在底部
    the_table = plt.table(cellText=pltPD.values,
                          cellColours=cellColours,
                          rowLabels=pltPD.index.values,
                          rowColours=colors,  # 每一列的颜色
                          colLabels=pltPD.columns.values,
                          loc='bottom',
                          cellLoc='center')
    the_table.set_fontsize(15)
    the_table.scale(1, 2.5)  # may help
    plt.xticks([])
    plt.yticks(fontsize=15)
    plt.ylim(0.4, 1.1)
    plt.ylabel("数值", fontsize=18)
    plt.show()