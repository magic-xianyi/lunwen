import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
if __name__ == '__main__':
    #去除gru模块各各参数均有下降，有效但不是最重要因素。
    #去除ISOA模块precision下降最多，因为无关变量的影响大了，导致检测误报率变高了
    #阈值模块这里使用普通的阈值方式，即使用训练经验得到的固定阈值，去除阈值模块后各指标都是最低，因为参考单一并且没有动态阈值
    precision = np.copy([0.9295, 0.8862, 0.9171, 0.8931])
    f1_socre = np.copy([0.8571, 0.82531, 0.8322, 0.8123])
    recall = np.empty(4)
    for i in range(4):
        recall[i] = format(f1_socre[i] * precision[i] / (2 * precision[i] - f1_socre[i]), '.4f')
    data = [recall, precision, f1_socre]
    columns = ('本章模型', '去除ISOA模块', '去除GRU模块', '去除阈值模块')
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
    plt.ylim(0.4, 1.2)
    plt.title('ISBGAT消融测试数据', fontsize=18)
    plt.show()