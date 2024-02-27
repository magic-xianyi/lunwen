import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def t():
    # 原始数据
    x = [0, 0, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 1]
    y = [0, 0.78, 0.84, 0.86, 0.88, 0.9, 0.91, 0.95, 1]

    # 插值
    f = interp1d(x, y, kind='cubic')

    # 在相邻点之间插入20个值
    x_interp = np.linspace(0, 1, 20 * (len(x) - 1) + 1)
    y_interp = f(x_interp)

    # 绘制原始数据和插值曲线
    plt.plot(x, y, 'o', label='Original Data')
    plt.plot(x_interp, y_interp, '-', label='Interpolated Curve')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Interpolated Curve using Cubic Spline')
    plt.legend()

    plt.show()

def t2():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [0, 0, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 1]
    y = [0, 0.78, 0.84, 0.86, 0.88, 0.9, 0.91, 0.95, 1]
    # 绘制ROC曲线
    # plt.figure(figsize=(8, 8)) 图大小
    plt.plot(x, y, 'r-', lw=1, linestyle='--', label='AUC = {:.3f})'.format(0.912))
    # 第二条线
    plt.plot([0, 1], [0, 1], color='black', lw=1, linestyle='--', label='Random Guessing')

    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('ROC曲线')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    t()