import matplotlib.pyplot as plt
import numpy as np


#文献量
def draw_histogram_line():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 创建数据
    x = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
         '2021', '2022', '2023']
    y1 = [407, 541, 554, 629, 748, 978, 1196, 1413, 1714, 1880, 2334, 2395]
    # y2 = [407, 541, 554, 629, 748, 978, 1196, 1413, 1714, 1880, 2334, 2395]
    # 绘制柱状图
    plt.bar(x, y1, label='文献数量')
    plt.xlabel('年份', fontsize=13)  # 横轴标签
    plt.ylabel('文献数量', fontsize=13)  # 纵轴标签
    # 绘制折线
    # plt.plot(x, y2, 'r-', label='line')
    # # 添加标签
    # for a, b in zip(x, y1):
    #     plt.text(a, b + 0.5, '%d' % b, ha='center', va='bottom')
    # for a, b in zip(x, y2):
    #     plt.text(a, b - 1.5, '%d' % b, ha='center', va='bottom')
    # 设置坐标轴范围
    plt.ylim(0, 3000)
    # 添加图例
    # plt.legend()
    # 显示图形
    plt.show()

if __name__ == '__main__':
    draw_histogram_line()
