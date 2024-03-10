import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

if __name__ == '__main__':
    # 原始数据
    y1 = [4, 5, 4, 5, 4, 5, 10, 4, 5, 4, 5, 4, 5, 4, 1, 5, 4, 5, 4]
    y2 = [4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5]
    y3 = [5, 5.2, 6, 6.3, 6.5, 7, 7.2, 7.5, 7.7, 8, 8.1, 7.9, 8.2, 8.5]
    y4 = [6.2, 6.5, 6.7, 7, 7.1, 6.9, 7.2, 7.5]
    y5 = [4, 4.2, 5, 5.3, 5.5, 6, 6.2, 6, 5.4, 5.1, 4.2, 4, 3.8, 3.6]

    # 设置子图布局
    fig, axes = plt.subplots(3, 1, figsize=(8, 6))

    # 第一个子图
    axes[0].plot(list(range(len(y1))), y1, label='整体数据变化')
    axes[0].set_title('数据点跃变异常')
    axes[0].set_xlabel('时间')
    axes[0].set_ylabel('值')
    axes[0].legend(fontsize=7)
    axes[0].set_xticks(list(range(len(y1))))

    # 第二个子图
    axes[1].plot(y2, label='整体数据变化')
    axes[1].set_title('数据变化模式异常')
    axes[1].set_xlabel('时间')
    axes[1].set_ylabel('值')
    axes[1].legend(fontsize=7)
    axes[1].set_xticks(list(range(len(y2))))

    # 第三个子图
    axes[2].plot(y3, label='维度1值')
    axes[2].plot([6,7,8,9,10,11,12,13],y4, '--', color='gray', label='维度2预期值')
    axes[2].plot(y5, label='维度2实际值')
    axes[2].set_title('维度关系异常')
    axes[2].set_xlabel('时间')
    axes[2].set_ylabel('值')
    axes[2].set_xticks(list(range(len(y3))))
    axes[2].legend(fontsize=7)
    # 调整子图之间的间距
    plt.tight_layout()
    # 显示图形
    plt.show()