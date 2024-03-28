import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
y_normal = [-0.2574864,-0.2574616,-0.2574006,-0.2573122,-0.25719385,-0.25706403,-0.2569219,-0.2574864,-0.2574616,-0.2574006,-0.2573122,-0.25719385,-0.25706403,-0.2569219,-0.25676083,-0.2566054,-0.2564543,-0.25631737,-0.25619393,-0.25609617,-0.25602733,-0.2559872,-0.25596802,-0.2559767,-0.25600093,-0.2560424,-0.25611334,-0.2559864,-0.2559616,-0.2559006,-0.2558122,-0.25569385,-0.25556403,-0.2554219,-0.25526083,-0.2551054,-0.2549543,-0.25481737,-0.25469393,-0.25459617,-0.25452733,-0.2544872,-0.25446802,-0.2544767,-0.25450093,-0.2545424,-0.25461334,-0.25468203,-0.25475106,-0.2547999,-0.25485024,-0.25490555,-0.25495768,-0.2549856,-0.25498146,-0.25493896,-0.2548594,-0.25475553,-0.25485045,-0.25493607,-0.25498146,-0.25493896,-0.25468203,-0.25475106,-0.2547999,-0.25485024,-0.25490555,-0.25495768,-0.2549856,-0.25498146,-0.25493896,-0.2548594,-0.25475553,-0.25485045,-0.25493607,-0.25498146,-0.25493896,-0.2548594]
y_attack = [-0.2559864, -0.2559616, -0.2559006, -0.2558122, -0.25569385, -0.25556403, -0.2554219,-0.2559864, -0.2559616, -0.2559006, -0.2558122, -0.25569385, -0.25556403, -0.2554219, -0.25526083, -0.2551054, -0.2549543, -0.25481737, -0.25469393, -0.25459617, -0.25452733, -0.2544872, -0.25446802, -0.2544767, -0.25450093, -0.2545424, -0.25461334, -0.25468203, -0.25475106, -0.2547999, -0.25485024, -0.25490555, -0.25495768, -0.2549856, -0.25498146, -0.25493896, -0.2548594, -0.25475553, -0.25485045, -0.25493607, -0.25664738, -0.25858563, -0.2608454, -0.26370472, -0.26677293, -0.2702589, -0.2741961, -0.27756503, -0.28110075, -0.28316438, -0.285196, -0.28546947, -0.28359014, -0.28047094, -0.27594104, -0.270804, -0.26456067, -0.26025072, -0.25791478, -0.25557652, -0.2526468, -0.25098673, -0.2491112, -0.24906875, -0.2496371, -0.25131595, -0.2524975, -0.25374573, -0.25603694, -0.25529763, -0.2522108, -0.24981293, -0.24798912, -0.24642351, -0.2449933, -0.24347463, -0.24176402, -0.23990783]
data_attack = [0.2729987,0.27286366,0.27275194,0.27265169,0.27268711,0.27280936,0.27314225,0.27346321,0.27378629,0.27421398,0.2744493,0.27460317,0.27472154,0.27468265,0.27472021,0.27466063,0.27464239,0.27457431,0.27448425,0.27438619,0.2745659,0.27451356,0.27436974,0.27429671,0.27421838,0.27407674,0.27381944,0.27369325,0.27360629,0.27359413,0.27366237,0.27408204,0.27445094,0.27471766,0.27500627,0.27526988,0.27536806,0.27551966,0.27558808,0.27544093,0.27550588,0.27557284,0.27555357,0.27544743,0.27533651,0.27541535,0.27534096,0.27524429,0.27517177,0.27504513,0.27496534,0.27502209,0.27502209,0.27475794,0.27465357,0.27466789,0.27463906,0.27460082,0.27498497,0.27530083,0.27530083,0.27562008,0.27598981,0.27645329,0.27674485,0.27681039,0.27679953,0.27659583,0.27661636,0.276644,0.27665845,0.27655593,0.27643331,0.276273,0.27626358,0.27616246,0.27609264,0.27610508,0.27609592,0.27597123,0.27588522,0.27597073,0.2761077,0.27611228,0.27631458,0.27675998,0.27701333,0.27732853,0.27757613,0.27771886,0.27771886,0.27786725,0.27786721,0.27777929,0.27767161,0.27766378,0.27772053,0.27776802,0.27766662,0.27772671,0.27758018,0.27750842,0.27740238,0.27747044,0.27733764,0.2774417,0.27736139,0.27745485,0.27757844,0.27808333,0.27859389,0.27892991,0.27921132,0.27934824,0.27946364,0.27963951,0.27964088,0.27950015,0.27946883,0.27932008,0.27922166,0.27899869,0.27896022,0.27890772,0.27883757,0.27882307,0.27882724,0.2787293,0.27870587,0.27862735,0.27872014,0.27870011,0.27867169,0.27870917,0.27917503,0.2796776,0.27990481,0.28020997,0.28066401,0.28092367,0.28101058,0.28102717,0.28086282,0.28079751,0.28078467,0.28070792,0.28058457,0.28052806,0.28039193,0.28025886,0.28025886,0.28011815,0.28000695,0.27990525,0.27985584,0.27977306,0.2797426,0.27975824,0.27970949,0.27977527,0.2798657,0.28021049,0.2805683,0.28086617,0.2810892,0.2813513,0.28143788,0.28150487,0.28170559,0.28165487,0.28155595,0.28144454,0.2813711,0.28140265,0.28140484,0.28135853,0.28132565,0.28124995,0.28115277,0.28101103,0.28085132,0.28082,0.28071623,0.28084793,0.28075518,0.28072737,0.28076921,0.28101621,0.28137536,0.2817651,0.28211975,0.28227284,0.27830392,0.27835392,0.25834309,0.25569442,0.25146953,0.24380959,0.2409876,0.23598843,0.23043437,0.23761549,0.2356506,0.25376271,0.25288792,0.27482068,0.28099706,0.29389633,0.30733325,0.30733325,0.31835986,0.28429822,0.2549926,0.26208672,0.26750328,0.2696779,0.27191229,0.27059861,0.2694491,0.26838342,0.28816653,0.26750328,0.2696779,0.27191229,0.27059861,0.2694491,0.26838342,0.28816653]
data_normal = [0.54590235,0.54591941,0.54587215,0.54505808,0.54507999,0.54529897,0.54574767,0.54602815,0.54601941,0.54632651,0.54653445,0.54696146,0.54705239,0.54683034,0.54668151,0.54672836,0.54666669,0.54654007,0.54627397,0.54627648,0.54635346,0.5470422,0.54689861,0.54657566,0.54634094,0.54631886,0.54628163,0.54615009,0.54619459,0.54556497,0.54579992,0.54601654,0.54632156,0.54681353,0.54697918,0.54702068,0.54683526,0.54665903,0.54659185,0.54659185,0.5464233,0.54643468,0.54625626,0.5462774,0.54606283,0.54620362,0.54693018,0.54673787,0.54659304,0.54631026,0.54596739,0.54600906,0.54476376,0.5447019,0.54521448,0.54591058,0.54640552,0.54833278,0.54848749,0.54840462,0.548292,0.54802059,0.54772567,0.5464834,0.54647913,0.54663909,0.54664733,0.54659631,0.54657988,0.54657988,0.54629389,0.54713515,0.54708419,0.54698498,0.54668827,0.546447,0.54621893,0.54635194,0.54655842,0.54687367,0.54689574,0.54747708,0.54781558,0.54813664,0.54963162,0.54988701,0.54978289,0.54994228,0.54932276,0.54939563,0.54981664,0.5498968,0.54988544,0.54978769,0.54970302,0.54980566,0.54973707,0.54990216,0.54827361,0.54818894,0.54851679,0.54862382,0.54870133,0.54857677,0.54870493,0.54978245,0.55002238,0.54863871,0.54885522,0.55026246,0.55052916,0.55090148,0.55117465,0.55114889,0.55114889,0.55111656,0.55220741,0.55212561,0.55127302,0.55032078,0.55021253,0.55016714,0.55174015,0.55218024,0.55200478,0.55191298,0.55014519,0.55017227,0.55014924,0.54990558,0.54997311,0.55010184,0.55038916,0.55070379,0.55099282,0.55116417,0.55130892,0.55147219,0.55150877,0.55150877,0.55147902,0.55129158,0.55139678,0.55137913,0.55084587,0.55055953,0.55042055,0.55035568,0.55033612,0.55036719,0.55103771,0.55097523,0.55063986,0.55061673,0.54915238,0.54905518,0.54927884,0.54961051,0.54972995,0.55019099,0.55060968,0.55070942,0.55101691,0.550915,0.55049056,0.55040115,0.55023844,0.55031094,0.55037363,0.55052091,0.55032726,0.54990681,0.54949,0.54914069,0.54898668,0.54904639,0.54903082,0.54892774,0.5488919,0.54870135,0.54873747,0.5490414,0.5490414,0.55011886,0.55074184,0.55107501,0.55029054,0.55020838,0.55005275,0.55006045,0.54997852,0.5502451,0.55027173,0.5507331,0.55050318,0.55025445,0.55007222,0.54991415,0.549488,0.54922698,0.54906547,0.54915778,0.54926721,0.54936676,0.54937575,0.54960825,0.54970767,0.54965906,0.54983108,0.55014649,0.55074531,0.55105936,0.551054,0.55071744,0.55056069,0.55048689,0.55048689,0.55032651,0.54997866,0.54961916,0.54948263,0.55056069,0.55048689,0.55048689,0.55032651,0.54997866,0.54961916,0.54948263]
def score():
    x = range(78)

    from scipy.interpolate import interp1d
    y2 = np.copy(y_normal) + 0.27
    # 原始数据
    x = np.linspace(0, 1, len(y2))
    x_new = np.linspace(0, 1, 2000)

    # 对每个数组进行插值
    f_normal = interp1d(x, y2, kind='cubic')
    f_attack = interp1d(x, y_attack, kind='cubic')
    f_data_attack = interp1d(x, data_attack[150:], kind='cubic')
    f_data_normal = interp1d(x, data_normal[150:], kind='cubic')

    # 对数据进行插值，增加或减少数据点的数量
    y_normal_interp = f_normal(x_new)
    y_attack_interp = f_attack(x_new)
    data_attack_interp = f_data_attack(x_new)
    data_normal_interp = f_data_normal(x_new)
    x = [i + 1000 for i in range(len(y_normal_interp))]

    plt.figure(figsize=(8, 6))

    plt.subplot(2, 1, 1)

    plt.plot(x, y_attack_interp, 'r', label='异常数据')
    plt.plot(x, y_normal_interp, label='正常数据')
    plt.title('异常得分')
    plt.xlabel('时间索引', fontsize=12)
    plt.ylabel('数值', fontsize=12)
    plt.legend(fontsize='9')
    plt.text(0.5, -0.35, '(a)', ha='center', va='center', transform=plt.gca().transAxes, fontsize=16)
    plt.subplot(2, 1, 2)
    plt.plot(x, data_attack_interp, 'r', label='异常数据')
    plt.plot(x, data_normal_interp, label='正常数据')
    plt.title('原始数据')
    plt.xlabel('时间索引', fontsize=12)
    plt.ylabel('数值', fontsize=12)
    plt.legend(fontsize='9')
    plt.text(0.5, -0.35, '(b)', ha='center', va='center', transform=plt.gca().transAxes, fontsize=16)
    plt.tight_layout()

    plt.show()

def relitu():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    # 读取CSV文件
    file_path = 'D:\\DataContainer\\NutCloud\\实验图\\算法2\\attack.csv'  # 将'your_file.csv'替换为您的CSV文件路径
    data = pd.read_csv(file_path)
    # 将每一列转换为数组
    column_arrays = []
    column_names = []
    for column_name in data.columns:
        column_array = data[column_name].values
        # 最大最小归一化
        min_val = np.min(column_array)
        max_val = np.max(column_array)
        if max_val != min_val and column_name not in ['AIT501', 'AIT502', 'FIT401', 'P302', 'DPIT301']:
            normalized_data = (column_array - min_val) / (max_val - min_val)
            column_arrays.append(normalized_data.tolist())
            column_names.append(column_name)
    # 绘制热力图
    print(len(column_names))
    plt.imshow(column_arrays, cmap='Blues', aspect=80,interpolation='nearest')
    plt.colorbar()  # 添加颜色条
    # 设置纵坐标刻度标签为每列的名称
    plt.yticks(np.arange(len(column_names)), column_names, fontsize=9, fontfamily='Arial')
    plt.xlabel('时间索引', fontsize=12)
    plt.ylabel('传感器名字', fontsize=12)
    plt.show()

def js():

    array = [0.11124759,0.11364279,0.12270737,0.15650916,0.20075947,0.20360334,0.21504774,0.25263647,0.25791212,0.27685827,0.37277895,0.49083194,0.49209234,0.53796822,0.57327349,0.61326266,0.61659177,0.62900208,0.63531454,0.64469796,0.80753367,0.8128935,0.81544938,1.09946343,1.13404915,1.14177373,1.17016933,1.27850315,1.3983461,1.41858352,1.59752099,1.66324124]
    name = ['FIT101', 'AIT203', 'P203', 'P205', 'P101', 'MV201', 'FIT301', 'P602', 'P402', 'MV304', 'FIT201', 'FIT502',
     'MV302', 'LIT301', 'MV303', 'AIT401', 'LIT101', 'AIT202', 'AIT503', 'MV301', 'LIT401', 'AIT201', 'FIT601',
     'AIT504', 'AIT402', 'FIT501', 'FIT503', 'PIT503', 'PIT501', 'PIT502', 'P501', 'UV401']

    for i in range(len(array)):
        array[i] = round(array[i], 4)
    # 打印排序后的结果
    print("排序后的值数组：", array)
    print("对应的名字数组：", name)

    # 绘制横向柱状图
    plt.barh(name, array)
    # 添加数值标签
    for i, v in enumerate(array):
        plt.text(v + 0.02, i, "{:.4f}".format(v), va='center')
    plt.xlabel('异常得分绝对值', fontsize=12)
    plt.ylabel('传感器名字', fontsize=12)
    # 调整 y 轴刻度范围，从而设置柱体的宽度
    plt.ylim(-0.6, len(name))
    plt.xlim(0, 1.9)
    plt.yticks(fontsize=9, fontfamily='Arial')
    plt.show()

if __name__ == '__main__':
    #relitu()
    #score()
    js()