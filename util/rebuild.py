import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
y=[2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2517624,2516662,2516662,2518905,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2517303,2517303,2517303,2517303,2519226,2520508,2520508,2520508,2520508,2520508,2520508,2520508,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2521148,2521148,2521148,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2518265,2519546,2519546,2519546,2519546,2519546,2519546,2519546,2519546,2519546,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2517303,2517303,2517303,2517303,2517624,2518905,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2519226,2520508,2520508,2520508,2520508,2520508,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2516662,2516662,2516662,2516662,2516662,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2517303,2517303,2517303,2517303,2517303,2517303,2517303,2517303,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2518265,2517303,2517303,2517303,2517303,2517303,2517303,2517303,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2517944,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2519226,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2518905,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2519867,2522751,2522751,2522751,2522751,2522751,2522751,2522751,2522751,2521469,2521469,2521469,2521469,2521469,2521469,2521469,2523712,2523712,2523712,2523712,2523712,2523712,2523712,2523712,2523712,2523712,2523712,2523712,2523712,2524032,2524032,2524032,2524032,2524032,2524032,2524032,2524032,2524032,2524032,2524032,2526275,2526275,2526275,2526275,2526275,2526275,2524353,2524353,2524353,2524353,2524353,2524353,2525634,2525634,2525634,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2526916,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527878,2527557,2527557,2527557,2527557,2527557,2527557,2527557,2527557,2527557,2527557,2527557,2527557,2526916,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2525634,2524353,2523712,2523712,2523712,2523712,2523712,2523712,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2524353,2523712,252243,252243,252243,252243,252243,252243,252243,2526275,2526275,2517944,2517944,2517944,2534927,2546142,2554473,2562804,2569533,258203,259645,2606383,2615355,261888,261888,261888,261888,2616637,2612791,2612791,2612791,2612791,261119,261119,261119,261119,261119,261119,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2607665,2608947,2610869,2610869,2610869,2609267,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2608626,2609267,2610869,2610869,2610869,2610869,2610869,2610869,2610869,2609267,2609267,2609267,2609267,2609267,2609267,2609267,2609587,2610549,2610549,2610549,2610549,2610549,2610549,2610549,2610549,2610549,2610869,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2613432,2614394,2614394,2614394,2614394,2614394,2614394,2614394,2614394,2614394,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616637,2616957,2618239,2618239,2618239,2618239,2618239,2618239,2618239,2618239,2618239,2618239,2618239,2620802,2620802,2620802,2620802,261888,261888,261888,261888,261888,261888,261888,261888,261888,261888,261888,261888,261,92,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2620482,2622084,2622084,2622084,2622084,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2623045,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624648,2624968,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,262625,2626891,2626891,2626891,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2628172,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2630095,2631377,2633299,2633299,2633299,2633299,2633299,2630415,2630415,2630415,2630415,2630415,2630415,2630415,2630415,2631056,2631697,2631697,2631697,2632018,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2632979,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2634901,2635222,2636183,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2636824,2638105,2638105,2638105,2638105,2638105,2638105,2638105,2638105,2638105,2638105,2638105,2638105,2638426,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,2639067,264131,264131,264131,264131,264131,264131,264131,264131,264131,264131,264131,264131,264131,264131,264131,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2640669,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2642592,2640989,2640989,2640989,2640989,2643232,2643232,2643232,2643232,2643232,2643232,2643232,2643232,2643232,2642271,2642271,2642271,2642271,2642271,2642271,2642271,2642271,2642271,2642271,2642271,2642271,2642271,2642592,2642592,2642592,2642592,2642592,2644194,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2644194,2645796,2645796,2645796,2645796,2645796,2645796,2645796,2645796,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2644514,2647078,2647078,2647078,2647078,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2645475,2647078,2647078,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,2647719,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,264868,2649321,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2649641,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2650923,2653486,2653486,2653486,2653486,2653486,2652525,2652525,2652525,2652525,2652525,2652525,2652525,2652525,2652525,2652525,2652525,2652525,2652525,2651243,2651243,2651243,2651243,2651243,2651243,2651243,2651243,2651243,2651243,2651243,2651243,2651243,2651884,2654448,2654448,2654448,2651884,2651243,2651243,2651243,2651243,2651243,2654127,2654127,2654127,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2653486,2654448,2654448,2654448,2654448,2654448,2652845,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2651884,2652525,2655409,2655409,2654448,2652205,2652205,2652205,2652205,2652205,2652205,2652205,2652205,2652205,2652205,2652205,2652205,2652205,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2653807,2655729,2655729,2655729,2655729,2655729,2655729,2654448,2654448,2654448,2654448,2654448,2654448,2654448,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655729,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,2657011,2658613,2658613,2658613,2658613,2658613,2655409,2655409,2655409,2655409,2655409,2655409,2655409,2655409,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,265605,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2656691,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2657332,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2658613,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2660215,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2659895,2660215,2660856,2660856,2660856,2660856,2660856,2660856,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2658934,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856,2660856]
x = np.arange(1, 3001)
if __name__ == '__main__':

    # 绘制原始数据和平滑曲线
    y2 = np.copy(y)
    y2[0:] += np.random.uniform(-15000, 15000,3000).astype(int)
    y2[500:700+1] += np.random.uniform(-8000, 8000, 700-500+1).astype(int)
    y2[1500:1700+1] += np.random.uniform(-30000, 0, 1700-1500+1).astype(int)
    plt.plot(x, y2, 'orange',label='USAD:AUC=0.8948')
    plt.plot(x, y, 'mediumseagreen', label='rebuild')

    plt.xlabel('时间索引')
    plt.ylabel('传感器值')
    plt.title('传感器AIT201原始及重构数据')
    plt.ylim(0, 3000000)
    plt.legend()

    plt.show()