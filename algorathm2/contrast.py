import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

def xingdian():

    name = ['THOC','USAD', 'TRANAD', 'AGAE', 'LSTM_NDT', 'LW_LSTM_VAE', 'MICNN', 'TFAD']
    cost = [24.3846 + 46, 5.4781 + 20, 15.1929 + 22, 11.0518 + 24, 8.23 + 20, 10.21 + 21, 39.9 + 16, 15.7 + 23]
    score = [0.8421, 0.8077, 0.8254, 0.8571, 0.8201, 0.8318, 0.8453, 0.8058]
    markers = ['d', 's', '^', 'h', 'p', 'D', '*', 'v']
    # 绘制散点图，并指定每个点的形状和标签
    plt.scatter(cost[0], score[0], marker = markers[0], label=name[0])
    plt.scatter(cost[1], score[1], marker = markers[1], label=name[1])
    plt.scatter(cost[2], score[2], marker = markers[2], label=name[2])
    plt.scatter(cost[3], score[3], marker = markers[3], label=name[3])
    plt.scatter(cost[4], score[4], marker = markers[4], label=name[4])
    plt.scatter(cost[5], score[5], marker = markers[5], label=name[5])
    plt.scatter(cost[6], score[6], color='r',marker = markers[6], label=name[6])
    plt.scatter(cost[7], score[7], marker = markers[7], label=name[7])

    plt.annotate('MICNN', (cost[6], score[6]), textcoords="offset points", xytext=(2, 9), ha='center', fontsize=9)
    plt.annotate('AGAE', (cost[3], score[3]), textcoords="offset points", xytext=(9, 0), ha='left', fontsize=9)
    plt.xlabel('资源消耗', fontsize=12)
    plt.ylabel('F1_Score', fontsize=12, labelpad=10)
    plt.legend()
    plt.grid()
    plt.show()

def shang():
    entropy = [2.23, 3.4, 4.4, 5.3, 8.4, 12.6]
    AGAE = [0.8571, 0.8573, 0.8563, 0.8541, 0.84, 0.828]
    MICNN = [0.8453, 0.8441, 0.8442, 0.84, 0.836, 0.831]
    LSTM_NDT = [0.8201, 0.820, 0.812, 0.801, 0.78, 0.745]
    LW_LSTM_VAE = [0.8318, 0.836, 0.830, 0.821, 0.81, 0.77]
    TFAD = [0.8058, 0.8056, 0.78, 0.778, 0.76, 0.747]
    TranAD = [0.8254, 0.825, 0.82, 0.8, 0.77, 0.752]
    THOC = [0.8421, 0.8422, 0.8321, 0.8351, 0.82, 0.8]
    USAD = [0.8077, 0.8, 0.78, 0.77, 0.73, 0.71]
    plt.plot(entropy, AGAE, marker='*', linewidth=1, label='AGAE')
    plt.plot(entropy, MICNN, marker='x', linewidth=1, label='MICNN')
    plt.plot(entropy, LSTM_NDT, marker='o', markersize=5, linewidth=1, label='LSTM_NDT')
    plt.plot(entropy, LW_LSTM_VAE, marker='s', markersize=4, linewidth=1, label='LW_LSTM_VAE')
    plt.plot(entropy, TFAD, marker='^', linewidth=1, label='TFAD')
    plt.plot(entropy, TranAD, marker='D', markersize=4, linewidth=1, label='TranAD')
    plt.plot(entropy, THOC, marker='+', linewidth=1, label='THOC')
    plt.plot(entropy, USAD, marker='v', linewidth=1, label='USAD')
    plt.xlabel('熵大小', fontsize=12)
    plt.ylabel('F1_Score', fontsize=12, labelpad=10)
    plt.legend(fontsize=9)
    plt.show()
if __name__ == '__main__':
    #xingdian()
    shang()