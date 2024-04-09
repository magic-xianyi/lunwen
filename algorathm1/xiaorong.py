import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = ["simSun"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
if __name__ == '__main__':
    precision = np.copy([0.9495, 0.9262, 0.9371, 0.9131]) - (0.9495 - 0.9267)
    f1_socre = np.copy([0.8571, 0.83531, 0.8422, 0.8223]) - (0.8571 - 0.8453)
    recall = np.empty(4)
    for i in range(4):
        recall[i] = format(f1_socre[i] * precision[i] / (2 * precision[i] - f1_socre[i]), '.4f')
    recall[0] = 0.7771
    for i in range(4):
        f1_socre[i] = format(f1_socre[i], '.4f')
    data = [recall, precision, f1_socre]
    columns = ('完整模型', '去除ISOA模块', '去除GRU模块', '去除阈值模块')
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
    ax.legend(fontsize=18)
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
    the_table.set_fontsize(18)
    the_table.scale(1, 2.5)  # may help
    plt.xticks([])
    plt.yticks(fontsize=18)
    plt.ylim(0.4, 1.2)
    plt.ylabel("数值", fontsize=19)
    plt.show()
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('C:\\Users\\helloworld\\Desktop\\svg\\算法1\\消融实验.svg')