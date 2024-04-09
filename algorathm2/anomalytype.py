import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["Times New Roman"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':
    # 原始数据
    y1 = [4, 5, 4, 5, 4, 5, 10, 4, 5, 4, 5, 4, 5, 4, 1, 5, 4, 5, 4]
    y2 = [4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5]
    y3 = [5, 5.2, 6, 6.3, 6.5, 7, 7.2, 7.5, 7.7, 8, 8.1, 7.9, 8.2, 8.5]
    y4 = [6.2, 6.5, 6.7, 7, 7.1, 6.9, 7.2, 7.5]
    y5 = [4, 4.2, 5, 5.3, 5.5, 6, 6.2, 6, 5.4, 5.1, 4.2, 4, 3.8, 3.6]

    # 设置子图布局
    fig = plt.figure(figsize=(8, 6))

    plt.subplot(3, 1, 1)
    plt.plot(list(range(len(y1))), y1, label='整体数据变化')
    plt.xlabel('时间', fontfamily='SimSun', fontsize=10)
    plt.ylabel('数值', fontfamily='SimSun', fontsize=10)
    legend_props = {'family': 'SimSun', 'size': 8}
    # 添加图例并设置字体属性
    plt.legend(prop=legend_props)
    plt.xticks(list(range(len(y1))))
    plt.text(0.5, -0.6, '(a) 数据点跃变异常', ha='center', va='center', transform=plt.gca().transAxes, fontsize=12, fontfamily='SimSun')
    # 第二个子图
    plt.subplot(3, 1, 2)
    plt.plot(y2, label='整体数据变化')
    plt.xlabel('时间', fontfamily='SimSun', fontsize=10)
    plt.ylabel('数值', fontfamily='SimSun', fontsize=10)
    legend_props = {'family': 'SimSun', 'size': 8}
    # 添加图例并设置字体属性
    plt.legend(prop=legend_props)
    plt.xticks(list(range(len(y2))))
    plt.text(0.5, -0.6, '(b) 数据变化模式异常', ha='center', va='center', transform=plt.gca().transAxes, fontsize=12, fontfamily='SimSun')

    # 第三个子图
    plt.subplot(3, 1, 3)
    plt.plot(y3, label='维度1值')
    plt.plot([6,7,8,9,10,11,12,13],y4, '--', color='gray', label='维度2预期值')
    plt.plot(y5, label='维度2实际值')
    plt.xlabel('时间', fontfamily='SimSun', fontsize=10)
    plt.ylabel('数值', fontfamily='SimSun', fontsize=10)
    plt.xticks(list(range(len(y3))))
    legend_props = {'family': 'SimSun', 'size': 8}
    # 添加图例并设置字体属性
    plt.legend(prop=legend_props)
    plt.text(0.5, -0.6, '(c) 维度关系异常', ha='center', va='center', transform=plt.gca().transAxes, fontsize=12, fontfamily='SimSun')
    # 调整子图之间的间距
    plt.tight_layout()
    # 显示图形
    plt.show()
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('D:\\桌面\\svg\\算法2\\异常类型.svg')