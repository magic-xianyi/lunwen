import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from matplotlib.font_manager import FontProperties

plt.rcParams["font.sans-serif"] = ["Times New Roman"]  # 设置字体中文乱码问题
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

if __name__ == '__main__':

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
    # 绘制原始信号、逆变换结果和频谱图
    fig = plt.figure(figsize=(12, 6))
    # 创建画布和子图
    plt.subplot(1, 2, 2)
    # 绘制平滑曲线图，设置为虚线
    plt.plot(smooth_x1, smooth_y1, label='原始SOA', linestyle='--', dashes=(1, 1))
    plt.plot(smooth_x2, smooth_y2, label='双力多因子SOA', linestyle='--')
    plt.xlabel('迭代轮次', fontsize=14, fontfamily='SimSun')
    plt.ylabel('适应度函数值', fontsize=14, fontfamily='SimSun')
    plt.title('平均收敛曲线', fontsize=14, fontfamily='SimSun')
    legend_props = {'family': 'SimSun', 'size': 12}
    # 添加图例并设置字体属性
    plt.legend(prop=legend_props)
    # 设置横坐标范围从0开始
    plt.xlim(0, max(max(x1), max(x2)))
    plt.grid(True, linestyle='--')  # 网格线
    plt.text(0.5, -0.16, '(b)', ha='center', va='center', transform=plt.gca().transAxes, fontsize=16)
    plt.subplot(1, 2, 1)
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
    plt.bar(bar_positions1, data1, width=bar_width, label='原始SOA')
    plt.bar(bar_positions2, data2, width=bar_width, label='双力多因子SOA')
    # 添加标签和标题
    plt.xlabel('指标', fontsize=14, fontfamily='SimSun')
    plt.ylabel('数值', fontsize=14, fontfamily='SimSun')
    plt.title('寻优结果', fontsize=14, fontfamily='SimSun')
    # 设置横坐标刻度及标签
    plt.xticks([pos + bar_width / 2 for pos in bar_positions1], labels, fontsize=12, fontfamily='SimSun')
    # 添加图例
    plt.legend(prop=legend_props)
    plt.text(0.5, -0.16, '(a)', ha='center', va='center', transform=plt.gca().transAxes, fontsize=16)
    # 调整布局
    plt.tight_layout()
    # 显示柱状图
    plt.show()
    # 调整布局
    plt.tight_layout()
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('C:\\Users\\helloworld\\Desktop\\svg\\算法1\\SOA.svg')
