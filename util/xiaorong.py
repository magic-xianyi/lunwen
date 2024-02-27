import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
if __name__ == '__main__':
    data = [[66386, 174296, 75131, 577908, 32015],
            [58230, 381139, 78045, 99308, 160454],
            [89135, 80552, 152558, 497981, 603535],
            [78415, 81858, 150656, 193263, 69638]]
    columns = ('Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5')
    rows = ['Metric %d' % x for x in (1, 2, 3, 4)]
    pltPD = pd.DataFrame(data, columns=columns, index=rows)
    # 按照model来进行汇总, 这里共有5个model
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    # 自定义颜色
    # colors = plt.cm.BuPu(np.linspace(0, 0.5, len(pltPD.index.values)))
    colors = plt.cm.rainbow(np.linspace(0, 1, len(pltPD.index.values)))  # plasma, rainbow, jet
    n_rows = len(pltPD.index.values)
    # 设置barchart的x轴
    w = 0.3
    index = np.arange(len(pltPD.columns.values)) * n_rows * w * 1.5  # 5个model, 所以是5
    # 首先绘制柱状图
    for row in range(n_rows):
        plt.bar(index + row * w, pltPD.values[row], width=w, align='center', color=colors[row],
                label=pltPD.index.values[row])
    # 添加图例
    ax.legend(fontsize=12)
    # 矩阵的颜色高亮
    # norm = plt.Normalize(0, 1)
    # cellColours = plt.cm.Blues(norm(pltPD.values))
    # 使用最大最小标准化, 使得颜色区分更大
    minmax = (pltPD.values - pltPD.values.min(1, keepdims=True)) / (
                pltPD.values.max(1, keepdims=True) - pltPD.values.min(1, keepdims=True))
    cellColours = plt.cm.Blues(minmax)
    # 添加一个表格在底部
    the_table = plt.table(cellText=pltPD.values,
                          cellColours=cellColours,
                          rowLabels=pltPD.index.values,
                          rowColours=colors,  # 每一列的颜色
                          colLabels=pltPD.columns.values,
                          loc='bottom',
                          cellLoc='center')
    the_table.set_fontsize(14)
    the_table.scale(1.0, 1.7)  # may help
    # 调整table的布局
    # plt.subplots_adjust(left=0.2, bottom=0.1)
    # label和ticks的设置
    # minN, maxN = pltPD.values.flatten().min(), pltPD.values.flatten().max()
    # plt.yticks(np.arange(minN, maxN, (maxN-minN)/5), fontsize=14)
    plt.yticks(np.arange(0, 1.1, 0.2), fontsize=14)
    plt.xticks([])
    plt.title('Comparison between Different Models', fontsize=14)
    plt.show()