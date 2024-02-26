import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from matplotlib.font_manager import FontProperties

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
# 解析数据-曲线图
data1 = "(-1.5,0),(-3,100),(-3.1,110),(-3.15,120),(-3.14,130),(-3.12,140),(-3.15,150),(-5,200),(-6,300),(-7.5,400),(-8.5,500)"
data2 = "(-1,0),(-5,100),(-8.5,200),(-8.7,250),(-9,300),(-9.3,350),(-9.5,400),(-10.536,500)"
# 柱状图

def parse_data(data):
    points = data.strip("()").split("),(")
    x_values = []
    y_values = []
    for point in points:
        y, x = map(float, point.split(","))
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values
#画曲线图
def drawLine():
    x1, y1 = parse_data(data1)
    x2, y2 = parse_data(data2)

    # 进行样条插值
    cs1 = CubicSpline(x1, y1)
    cs2 = CubicSpline(x2, y2)

    # 生成平滑曲线上的点
    smooth_x1 = np.linspace(min(x1), max(x1), 100)
    smooth_y1 = cs1(smooth_x1)
    smooth_x2 = np.linspace(min(x2), max(x2), 100)
    smooth_y2 = cs2(smooth_x2)

    # 绘制平滑曲线图，设置为虚线
    plt.plot(smooth_x1, smooth_y1, label='original SOA', linestyle='--', dashes=(1, 1))
    plt.plot(smooth_x2, smooth_y2, label='improved SOA', linestyle='--')

    # 添加数据点图
    #plt.scatter(x1, y1, color='blue')
    #plt.scatter(x2, y2, color='red')
    plt.xlabel('迭代轮次')
    plt.ylabel('适应度函数值')
    plt.title('平均收敛曲线')
    plt.legend()
    # 设置横坐标范围从0开始
    plt.xlim(0, max(max(x1), max(x2)))

    plt.grid(True, linestyle='--') #网格线
    plt.show()
#画柱状图
def draw_histogram_line():
    # 提供的数据
    labels = ['最优值差', '均值差', '标准差', '运行时间']
    data1 = [0.5, 0.9, 1.2, 0.61]
    data2 = [0.03, 0.2, 0.6, 0.655]
    # 设置柱状图的宽度
    bar_width = 0.2
    # 设置横坐标的位置
    bar_positions1 = range(len(labels))
    bar_positions2 = [pos + bar_width for pos in bar_positions1]
    # 绘制柱状图
    plt.bar(bar_positions1, data1, width=bar_width, label='original SOA')
    plt.bar(bar_positions2, data2, width=bar_width, label='improved SOA')
    # 添加标签和标题
    plt.xlabel('指标')
    plt.ylabel('数值')
    plt.title('寻优结果')
    # 设置横坐标刻度及标签
    plt.xticks([pos + bar_width / 2 for pos in bar_positions1], labels)
    # 添加图例
    plt.legend()
    # 显示柱状图
    plt.show()

if __name__ == '__main__':
    draw_histogram_line()
    drawLine()