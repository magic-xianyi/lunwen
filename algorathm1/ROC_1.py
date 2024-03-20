import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':
    # 原始数据
    x = [0, 0, 0.03,0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.85, 0.9, 0.93, 0.94,1]
    y = [0, 0.78, 0.81,0.825, 0.84, 0.86, 0.88, 0.91, 0.915,0.92, 0.95, 0.955, 0.97,1]
    x_USAD = [0, 0, 0.02, 0.03,0.05, 0.1, 0.2, 0.4, 0.45,0.5, 0.6, 0.8, 0.85, 0.9, 0.93, 0.94,1]
    y_USAD = [0, 0.68, 0.7,0.74,0.78, 0.8, 0.82, 0.83, 0.84,0.87,0.92, 0.93,0.95, 0.96, 0.97, 0.98,1]
    x_trannd = [0, 0, 0.03,0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.85, 0.87, 0.9, 0.93, 0.94,0.95,1]
    y_trannd= [0, 0.6, 0.68,0.7, 0.74, 0.76, 0.78, 0.81, 0.84,0.87, 0.89, 0.91, 0.92, 0.92,0.93,1]
    x_thoc = [0, 0, 0.03,0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.85, 0.9, 0.93, 0.94,1]
    y_thoc = [0, 0.73, 0.77,0.78, 0.81, 0.83, 0.86, 0.89, 0.90,0.91, 0.93, 0.95, 0.97,1]

    # 绘制原始数据和平滑曲线

    plt.plot(x_USAD, y_USAD,'pink', label='USAD:AUC=0.8948')
    plt.plot(x_trannd, y_trannd, 'mediumseagreen', label='THOC:AUC=0.8821')
    plt.plot(x_thoc, y_thoc, 'purple', label='TRanAD:AUC=0.8315')
    plt.plot(x, y, 'r-', label='AGAE:AUC=0.9122')
    plt.plot([0, 1], [0, 1], '--')

    plt.xlabel('假阳率')
    plt.ylabel('真阳率')
    plt.title('ROC 曲线')
    plt.legend()
    plt.grid(True)
    plt.show()