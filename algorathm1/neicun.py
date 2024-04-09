import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["Times New Roman"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    fig = plt.figure()

    name = ['THOC', 'USAD', 'TranAD', 'AGAE']
    num = [40.25392, 16.40497, 30.89652, 30.09093]
    size = [24.3846, 8.4781, 15.1929, 11.0518]
    # 1.将x轴转换为数值
    x = np.arange(len(name))
    # 2.设置图形的宽度
    width = 0.2
    # _______________确定x起始位置
    # f1起始位置
    n = x
    # auc的起始位置
    ac = x + width
    # 金牌图形
    plt.bar(n, num, width=width, color='powderblue', label='参数规模（万）')
    # 银牌图形
    plt.bar(ac, size, width=width, color='lightsteelblue', label='内存消耗（MB）')
    plt.xticks(x + width, labels=name)
    plt.xlabel('模型', fontfamily='SimSun', fontsize=13)
    plt.ylabel('数值', fontfamily='SimSun', fontsize=13)
    legend_props = {'family': 'SimSun', 'size': 10}
    # 添加图例并设置字体属性
    plt.legend(prop=legend_props)
    #plt.ylim(0.8, 1)
    plt.show()
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('C:\\Users\\helloworld\\Desktop\\svg\\算法1\\内存对比.svg')
