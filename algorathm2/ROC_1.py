import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["Times New Roman"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':
    x = [0, 0.03,0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.85, 0.9, 0.93, 0.94,1]
    y = [0.78, 0.81,0.825, 0.84, 0.86, 0.88, 0.91, 0.915,0.92, 0.95, 0.955, 0.96,1]

    # 线性插值
    f = interp1d(x, y, kind='cubic')

    # 生成更多的点以获得平滑的曲线
    x_smooth = np.linspace(0, 1, 1000)
    y_smooth = f(x_smooth)
    x_smooth = np.insert(x_smooth, 0, 0)
    y_smooth = np.insert(y_smooth, 0, 0)
    # 绘制原始数据和平滑曲线
    fig = plt.figure()
    plt.plot(x_smooth, y_smooth, label='AUC=0.9122')
    plt.plot([0, 1], [1, 0], linestyle='dotted', color='r')
    plt.plot(0.156, 0.844, 'ro', markersize=5)  # 'ro'表示红色圆点
    plt.xlabel('假阳率', fontsize=13, fontfamily='SimSun')
    plt.ylabel('真阳率', fontsize=13, fontfamily='SimSun')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('D:\\桌面\\svg\\算法2\\ROC.svg')