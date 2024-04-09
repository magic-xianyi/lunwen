import matplotlib.pyplot as plt
import numpy as np

def draw_histogram_line():
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False
    # 创建数据
    y = [2300371,2978587,2724636,2124829,2155013,2811573,2265082,2409416,2966665,2942892,2728712,2310249,2547808,2581292,2439130,2904101,2895034,2382375,2934286,2574329,2095798,2260389,2168033,2060940,2710807,2581804,2012067,2622899,2981926,2026733,2441823,2513505,2000575,2483167,2179074,2902888,2215600,2519681,2067411,2235689,2187376,2428472,2328262,2142428,2037794,2180257,2765275,2806052,2394019,2847041,2228093,2967913,2356681,2584839,2579742,2426539,2494556,2111529,2497800,2836108,2164777,2424407,2429324,2213768,2495703,2892345,2618446,2202700,2860185,2997430,2141258,2395271,2264232,2344226,2025454,2972853,2377864,2091044,2866699,2495771,2211273,2822153,2475080,2534789,2790367,2384808,2144277,2727685,2068671,2131591,2028471,2667897,2425370,2518452,2222630,2003541,2665177,2071387,2358688,2780436,2052526,2743131,2552315,2087158,2915009,2766536,2518654,2919586,2980393,2641307,2279266,2078733,2368527,2971727,2844364,2698894,2960569,2756761,2076416,2545551,2417087,2371721,2415854,2153848,2646239,2210801,2884270,2380062,2983510,2806916,2242612,2846605,2357111,2421827,2186488,2925884,2993040,2084213,2068104,2107845,2749904,2404944,2562709,2815564,2181893,2176264,2497844,2180621,2532940,2843282,2472059,2722576,2996090,2008166,2104676,2311450,2254904,2700141,2557968,2910793,2063634,2542791,2130492,2358532,2845576,2444495,2278762,2530020,2808708,2940548,2834048,2357219,2495711,2438567,2024308,2501503,2059039,2391542,2291029,2612147,2031310,2169596,2726862,2114251,2922176,2279902,2253817,2136495,2632652,2223617,2023298,2934291,2367016,2154496,2448665,2427866,2991780,2534242,2933825,2422442,2363309,2517962,2814157,2189865,2302353,2857926,2706732,2362673,2881594,2503308,2629925,2893494,2030099,2906955,2506358,2751051,2666723,2338935,2167953,2582435,2030831,2822198,2249479,2981598,2170796,2592568,2113051,2998033,2432020,2923285,2506104,2674379,2405298,2717410,2850903,2316114,2921520,2153259,2301289,2160651,2992499,2621733,2921645,2797909,2043941,2976584,2603113,2263190,2487949,2398121,2409101,2533895,2307762,2544887,2668326,2609696,2440214,2448400,2398196,2736076,2657474,2342772,2183407,2655522,2794092,2083744,2865736,2801026,2705198,2121414,2859453,2905686,2463239,2618259,2161375,2553717,2470560,2793186,2600554,2517375,2241071,2121768,2622180,2117816,2909619,2215062,2983394,2217133,2878996,2247901,2315696,2158019,2320813,2580892,2347805,2008230,2339573,2947555,2049474,2624109,2063401,2765842,2164667,2781282,2251558,2134951,2767072,2788950,2164285,2168763,2202319,2200575,2697920,2827370,2354014,2388277,2382221,2150397,2154243,2707261,2066530,2418830,2027769,2966486,2711403,2588086,2040067,2967655,2083967,2248645,2910665,2659031,2976698,2426473,2233679,2853056,2222687,2505673,2993777,2996644,2142414,2409688,2539076,2122303,2692991,2028651,2427089,2216504,2419345,2873795,2664754,2885962,2007448,2982613,2826396,2466034,2317091,2140646,2693756,2910590,2853108,2915871,2123490,2070914,2843185,2984293,2505882,2945664,2690832,2896024,2828882,2915363,2158942,2598279,2497673,2381753,2355463,2258362,2599205,2371617,2555704,2703563,2445109,2299184,2021544,2002340,2977987,2546971,2514278,2445757,2645686,2724892,2052354,2122732,2169399,2625361,2379948,2297644,2610247,3480057,3480057,3480057,3480057,3480057,2105425,2554773,2925491,2782082,2874762,2534906,2928733,2073027,2392428,2509348,2609071,2679817,2390835,2329042,2636606,2143354,2253754,2379245,2247896,2067118,2587814,2747214,2679487,2320252,2273127,2103211,2906770,2969645,2962318,2587166,2433722,2853909,2437513,2883579,2136737,2676899,2333734,2971243,2587577,2623869,2767397,2705711,2832366,2615927,2781074,2395864,2707694,2996195,2840352,2490847,2369468,2348804,2626860,2871270,2069133,2678791,2504124,2966163,2618424,2836657,2184897,2905937,2997434,2786546,2251450,2129989,2090026,2649304,2839194,2767163,2349321,2657612,2867653,2590600,2660866,2195691,2895203,2221366,2965861,2807992,2983585,2060277,2649536,2373265,2660354,2243234,2896839,2458417,2263913,2614670,2125488,2177427,2164621,2849730,2960833,2889872,2445341,2626221,2540485,2412045,2732035,2298170,2646654,2464156,2570149,2832353,2983398,2439587,2765978,2750075,2293688,2126063,2261495,2895542,2233810,2149827,2016731,2778968,2078313,2414456,2101797,2708963,2679344,2352317,2908092,2937233,2163250,2853338,2123146,2328011,2826571,2107328,2730225,2862791,2798727,2614753,2573667,2195757,2573874,2648673,2956384,2261416,2427627,2244131,2626067,2819157,2042574,2459003,2410470,2306607,2424644,2068977,2944307,2762791,2914347,2023470,2523616,2880982,2626956,2541147,2845734,2966394,2848907,2282992,2447320,2990354,2494910,2986017,2097824,2732842,2348916,2121693,2631905,2769361,2714120,2271267,2994635,2236293,2267797,2317648,2528784,2205766,2437716,2868575,2016370,2902240,2266151,2604821,2698879,2850591,2946203,2320536,2936100,2642030,2617761,2702032,2466585,2676400,2452661,2338180,2958412,2647473,2432009,2101308,2760965,2140249,2426116,2031209,2898027,2623266,2323855,2683711,2490837,2795872,2833841,2390055,2301264,2825055,2301791,2744643,2395518,2683377,2163761,2003906,2692352,2064102,2797966,2810482,2813875,2580425,2469053,2890956,2147602,2264934,2255004,2319168,2174861,2384462,2120046,2946166,2490597,2330246,2242201,2053823,2257538,2715971,2797443,2545960,2377544,2662138,2670179,2496253,2520591,2345066,2994241,2265488,2176856,2464999,2214705,2520482,2531387,2109334,2522669,2541342,2601363,2275719,2231947,2199020,2571260,2624559,2114108,2675527,2181520,2572999,2753912,2508651,2843969,2198669,2025630,2610728,2483879,2259702,2173519,2010091,2899140,2183045,2268850,2489309,2710503,2822664,2662071,2930086,2220674,2130525,2772648,3200000,3200000,3200000,3200000,3200000,2618354,2522340,2739668,2742560,2280666,2148055,2969529,2955373,2766841,2332140,2350108,2930785,2197472,2685733,2196374,2255455,2440838,2428505,2468756,2109279,2515997,2578976,2662181,2011063,2987013,2081749,2450494,2665255,2475970,2184338,2657459,2434454,2439330,2320859,2468822,2100067,2533073,2122124,2578409,2760958,2015384,2745001,2989659,2237706,2579587,2216121,2058252,2678535,2801990,2587120,2675243,2759240,2704994,2654167,2210611,2431842,2171755,2016207,2349278,2431668,2900837,2574282,2357291,2913200,2368704,2479991,2179661,2973972,2857410,2414535,2619763,2389566,2259659,2208968,2187767,2244944,2993755,2231042,2121236,2569017,2787489,2766401,2319716,2334220,2044251,2677660,2410150,2862054,2081832,2330280,2705709,2377561,2289818,2137123,2159679,2775512,2462647,2865179,2351614,2751622,2391454,2415298,2350160,2721285,2292028,2629901,2929995,2833402,2755278,2343422,2405601,2912636,2988074,2788740,2202970,2703661,2974177,2745554,2981535,2830472,2910645,2670020,2127049,2998699,2096618,2141836,2282982,2236960,2171467,2223968,2777388,2073715,2677074,2212464,2918412,2466704,2645093,2922576,2818506,2638756,2304636,2204932,2326508,2231724,2625965,2935818,2981514,2854113,2611524,2647805,2227292,2570693,2187943,2837517,2125624,2493915,2678121,2136088,2212940,2529400,2238364,2035730,2267113,2055778,2774987,2428850,2082189,2254197,2348628,2902095,2123438,2521350,2819915,2088198,2640395,2112300,2147168,2533225,2907707,2476489,2882717,2699795,2736022,2357709,2443615,2244884,2000422,2504401,2639799,2986029,2575794,2466030,2693922,2488898,2194377,2433569,2925385,2613967,2355199,2131609,2973227,2289690,2167347,2017592,2418846,2331107,2289098,2758947,2936674,2548846,2722962,2327073,2359686,2498158,2001701,2039292,2031859,2287231,2805802,2627379,2664789,2690811,2755331,2372490,2449005,2909764,2320776,2381732,2687134,2607865,2922932,2365679,2603666,2895285,2177285,2326940,2079723,2713636,2046135,2351560,2597939,2131536,2937964,2319846,2097981,2128007,2167994,2941829,2247219,2527257,2768292,2276737,2975617,2491090,2544130,2353576,2593061,2160615,2212926,2027898,2030494,2500673,2854483,2506603,2882792,2460434,2499456,2814393,2240734,2890348,2409284,2304392,2034280,2165356,2436203,2311470,2671576,2231010,2599745,2529869,2467908,2778857,2566091,2653397,2373264,2156533,2215027,2811090,2199357,2544406,2748785,2033819,2719542,2652350,2967890,2097513,2481133,2578664,2225457,2590254,2525888,2933122,2731650,2305461,2898042,2557251,2367321,2455459,2160805,2815195,2300349,2148004,2440853,2780294,2808321,2963267,2968828,2783798,2458614,2199258,2748948,2016134,2398667,2703059,2638010,2003780,2594456,2514958,2408931,2860744,2607319,2610194,2328571,2668921,2284864,2565165,2343913,2122436,2638382,2087639,2312483,2308783,2933250,2120830,2032249,2307292,2078273,2684569,2784995,2901761,2197912,2412676,2561604,2145248,2914529,2992907,2787006,2804392,2050517,2658649,2285896,2033871,2348050,2734340,2283680,2866665,2134720,2767232,2982974,2877992,2208194,2097701,2492168,2997364,2981317,2630878,2341591,2186280,2603266,2618327,2320825,2044231,2899575,2061002,2749391,2194230,2493774,2951676,2386181,2239911,2907766,2470855,2388133,2085721,2034737,2425545,2426325,2896227,2483021,2091513,2175683,2749562,2568052,2280883,2059869,2593921,2627505,2453655,2696345,2233446,2666740,2343629,2086270,2835313,2060019,2198912,2767989,2598895,2364816,2828206,2663391,2642033,2200246,2338527,2388746,2896499,2967666,2371587,2781736,2086326,2327657,2713073,2193101,2206094,2511153,2011604,2035232,2298401,2397140,2225702,2311824,2242789,2116963,2325437,2473281,2113605,2898304,2186044,2926836,2586169,2554480,2639840,2556876,2292192,2901393,2281255,2337571,2976622,2686673,2660073,2562144,2885737,2876431,2723862,2624945,2202845,2388059,2125032,2578250,2718470,2615970,2299346,2278298,2376743,2401967,2040260,2721180,2028385,2259314,2156539,2907787,2596554,2619411,2002862,2444820,2500432,2284778,2537871,2817007,2785036,2640444,2651281,2243666,2097878,2160511,2161960,2036715,2451118,2876754,2590008,2229110,2805705,2824587,2537387,2735633,2147245,2159834,2238959,2834917,2214042,2539674,2119518,2256604,2048134,2834449,2428485,2161752,2688236,2122879,2758191,2253653,2635258,2724994,2923539,2816339,2144163,2802605,2423335,2469639,2337445,2330846,2285556,2063123,2992467,2643924,2083555,2645475,2091378,2275573,2347866,2952609,2154391,2343621,2076525,2747457,2233245,2309320,2497481,2185133,2334649,2336837,2290215,2919018,2006557,2046450,2144214,2186683,2878555,2034473,2593069,2750748,2901753,2179439,2886962,2625001,2023793,2010910,2978025,2667072,2069118,2929111,2743432,2455612,2786489,2276234,2578484,2723082,2847657,2151338,2136749,2057373,2806893,2967435,2933570,2909976,2192789,2105941,2285215,2772432,2430944,2553358,2888876,2858682,2975634,2649950,2061757,2406034,2426227,2773513,2465414,2458533,2890071,2472400,2172973,2946384,2375818,2394596,2993024,2564781,2216791,2407815,2933447,2859400,2268163,2953049,2251373,2334855,2717568,2514552,2376674,2880688,2409576,2985110,2695466,2295042,2197386,2867217,2089226,2738326,2625993,2447186,2043679,2484838,2292700,2161732,2836341,2212116,2384177,2691502,2343167,2072037,2292485,2978747,2974604,2708928,2613005,2252613,2672084,2853103,2701624,2746391,2435787,2631399,2537757,2822004,2144353,2707430,2884055,2661922,2378228,2338559,2119785,2002882,2084193,2481100,2980278,2960551,2505058,2473698,2237469,2190688,2764914,2668689,2612115,2205525,2747686,2743989,2205740,2545959,2686720,2742461,2330998,2664017,2828547,2801199,2194261,2504354,2980812,2120154,2215758,2568575,2789384,2529351,2396804,2108592,2011115,2524644,2940547,2861068,2963300,2954794,2102594,2770372,2489138,2072891,2316678,2648192,2251653,2332209,2282232,2835989,2453070,2965375,2640419,2231785,2433995,2576645,2887944,2084599,2457391,2710018,2838470,2380355,2365612,2270890,2195523,2325254,2977911,2221081,2096970,2937134,2374891,2228215,2671918,2869825,2896331,2880026,2859143,2937449,2280688,2525557,2885846,2783672,2476203,2335112,2796308,2249639,2190132,2176088,2066151,2797960,2835378,2875384,2705015,2569354,2798250,2200387,2259712,2144463,2787911,2173769,2850827,2508473,2329286,2118861,2820426,2704415,2123480,2174137,2707068,2408122,2664428,2337338,2231318,2956168,2452896,2218505,2549116,2253307,2619610,2500775,2648310,2358829,2079869,2406601,2355650,2239687,2618565,2860821,2072178,2634333,2814027,2356028,2797939,2147214,2760261,2579427,2783764,2519330,2481356,2904730,2415653,2622075,2436550,2853605,2536692,2333033,2400842,2537521,2580308,2229898,2395474,2235479,2202208,2676406,2887904,2134870,2437872,2714257,2143049,2799149,2597784,2062183,2186592,2531104,2578878,2061247,2853744,2269123,2132229,2338808,2389550,2814033,2752043,2980884,2406863,2413882,2432765,2599728,2280941,2387254,2054730,2875319,2067941,2665360,2502832,2817083,2514419,2276478,2279456,2625442,2221919,2352024,2825181,2138437,2222212,2690106,2322269,2121584,2148013,2884587,2631533,2407228,2262870,2963633,2217593,2901819,2327814,2082562,2225718,2390549,2253251,2165372,2946088,2350869,2029921,2934792,2656051,2133713,2298691,2707720,2452827,2730987,2173489,2955995,2907859,2214455,2893786,2006316,2158852,2234852,2373806,2494575,2674966,2783724,2331652,2783443,2532269,2097673,2767566,2587699,2898835,2527972,2661128,2952010,2304121,2124626,2652152,2720507,2232169,2969848,2618157,2784698,2173958,2146649,2649101,2136267,2950473,2286374,2570467,2419400,2518354,2334586,2955437,2671730,2664101,2808536,2045183,2045608,2271694,2926492,2227148,2261988,2537738,2498597,2613062,2852595,2309467,2790596,2009200,2448761,2394682,2267322,2484610,2839456,2799603,2378421,2240061,2788476,2346744,2649805,2423412,2120305,2839495,2820462,2687952,2493221,2383936,2265892,2347515,2421821,2328346,2869100,2223673,2014428,2882577,2242898,2506306,2575201,2735468,2128053,2337246,2473330,2364246,2113740,2500690,2360374,2055982,2763019,2994234,2539790,2366975,2009883,2911554,2400059,2728896,2361580,2937367,2314784,2041641,2520339,2378610,2993957,2646488,2176818,3300000,3300000,3300000,3300000,3300000,2936231,2273866,2926355,2425322,2780251,2648873,2438040,2772309,2110471,2994245,2471633,2313783,2713104,2854717,2035989,2705003,2850985,2413689,2505276,2634917,2256285,2023875,2452286,2385680,2742705,2626192,2921162,2195193,2069894,2515040,2398191,2814159,2226443,2114931,2710265,2116157,2892610,2612293,2065540,2099417,2017754,2275167,2352564,2312317,2020843,2165211,2127142,2937315,2572502,2771662,2645337,2758675,2368489,2174163,2334223,2506545,2085696,2854078,2079584,2171205,2131586,2216259,2595338,2226635,2921654,2982982,2717185,2817574,2499006,2393920,2941196,2610171,2235392,2550962,2690336,2988243,2698900,2943857,2415183,2675364,2051413,2098036,2153763,2332305,2930624,2963688,2577279,2408511,2263740,2903405,2358372,2241240,2656655,2289421,2456615,2082407,2199735,2989901,2983737,2420877,2151464,2012262,2254372,2601763,2395895,2500430,2303128,2623987,2103158,2558785,2032526,2296803,2521357,2919474,2491365,2745891,2425919,2045216,2875369,2667748,2804478,2807327,2489198,2469057,2363025,2698625,2981641,2189014,2613387,2951657,2130113,2081215,2073079,2090738,2542331,2566636,2910266,2053296,2549981,2430273,2695609,2138254,2917122,2420771,2883838,2656775,2641144,2217708,2015812,2438310,2354299,2908256,2177904,2364485,2530104,2617288,2275850,2864478,2351013,2586148,2648443,2932774,2568794,2720181,2004969,2285571,2608951,2929657,2740367,2265686,2298563,2915942,2589156,2261911,2667159,2254828,2384758,2342225,2911273,2499738,2278676,2431250,2396078,2016452,2031873,2973611,2361008,2630080,2421014,2584718,2342244,2718553,2259688,2209758,2341791,2364068,2507355,2326873,2116457,2436224,2049063,2105153,2200735,2158339,2861831,2057676,2314434,2319633,2100983,2657587,2717253,2910007,2346444,2175465,2677087,2568805,2743361,2230888,2422682,2908445,2049745,2564977,2350682,2916053,2551200,2539627,2707493,2826729,2090677,2467945,2501844,2583395,2963310,2403004,2672234,2781271,2480620,2133781,2305195,2126498,2067110,2898390,2356948,2857821,2016500,2745203,2678693,2927140,2098903,2084108,2189412,2055382,2906135,2143094,2746520,2510069,2931048,2520248,2064949,2764329,2720476,2272570,2406174,2962350,2054705,2743611,2146253,2247985,2599778,2512135,2191524,2569748,2782759,2261961,2652813,2591514,2199123,2208105,2603928,2622541,2692870,2550150,2054740,2395193,2934348,2944197,2747222,2475669,2137451,2269124,2552269,2878734,2332067,2129418,2814600,2299140,2361614,2440749,2167817,2112465,2871226,2476285,2335560,2338297,2200520,2888943,2527511,2716105,2667435,2345616,2813719,2257475,2754028,2002414,2171105,2753932,2612244,2045048,2965289,2535729,2784964,2540841,2973884,2039782,2236925,2882265,2320873,2387227,2838076,2338350,2482974,2634267,2779391,2127641,2201759,2988867,2895176,2997993,2480365,2043895,2248961,2451353,2123403,2227344,2425380,2485585,2688989,2268331,2951002,2575678,2662875,2136080,2715712,2231722,2159152,2380469,2361318,2193723,2230544,2248758,2243125,2831156,2730009,2804443,2827992,2607124,2192634,2515503,2947527,2733322,2944791,2464993,2887244,2767071,2954400,2303211,2789588,2047455,2523959,2292095,2626797,2957938,2969482,2852013,2726816,2019768,2713149,2279157,2118450,2973525,2426693,2999971,2959293,2460312,2339538,2340851,2716638,2369308,2172066,2861173,2575820,2956998,2593532,2800496,2383183,2617791,2729134,2612980,2463999,2621684,2711819,2582799,2860851,2931410,2525210,2546995,2370497,2445354,2998524,2788719,2575441,2373785,2520669,2977362,2050456,2991914,2784433,2066134,2472513,2166766,2770853,2621845,2422635,2913061,2957535,2457900,2166816,2197640,2975855,2214458,2654065,2346769,2279148,2037305,2600389,2104525,2675945,2185567,2614762,2292714,2570777,2114948,2411524,2058113,2802768,2824732,2189401,2870833,2365361,2560782,2404885,2616412,2310293,2698768,2736574,2225629,2089989,2957284,2056111,2119863,2613970,2485571,2337656,2091900,2708785,2242232,2239135,2981327,2029050,2228164,2292123,2863934,2786349,2857861,2057395,2472129,2444370,2568778,2271009,2455381,2523237,2319062,2264884,2358081,2508137,2757808,2427508,2478427,2379712,2074489,2530702,2665277,2143486,2475908,2765771,2725172,2093616,2101469,2746931,2229663,2323676,2884268,2075597,2042126,2322400,2499474,2555558,2200185,2299706,2943243,2234458,2209973,2050664,2375613,2924958,2701375,2305888,2444821,2968592,2670359,2283510,2535172,2757288,2910879,2935086,2252759,2486967,2639005,2704224,2666385,2567204,2086873,2154041,2977561,2766041,2232637,2284041,2458142,2605733,2793674,2672774,2793114,2063627,2689940,2540613,2045154,2040616,2505720,2089634,2621378,2807449,2781832,2453063,2935563,2095096,2924289,2403137,2480668,2384500,2349839,2760296,2774635,2607350,2668341,2491670,2075723,2676934,2701539,2830438,2817532,2138211,2828315,2024218,2253743,2951142,2549684,2734907,2567055,2962943,2690621,2392057,2563632,2578354,2895619,2743396,2907169,2167860,2176314,2015160,2126106,2485028,2556312,2917730,2090094,2899139,2493797,2040394,2459320,2426481,2135451,2420562,2737647,2974392,2221936,2603986,2107856,2152176,2653406,2957228,2300651,2570298,2965151,2200855,2361099,2805497,2914463,2696495,2736728,2032980,2604483,2325476,2186244,2721255,2529544,2273752,2158217,2314018,2090106,2567222,2033412,2238047,2009327,2377071,2202530,2623953,2837833,2737878,2497014,2851189,2319761,2278111,2457730,2718316,2168554,2706003,2483030,2802637,2566774,2015938,2108016,2624859,2320686,2383845,2767064,2624365,2797059,2138957,2720168,2691425,2860671,2793194,2659454,2367546,2422386,2151551,2802465,2791804,2563682,2888044,2125710,2221368,2407940,2025209,2440385,2174621,2854473,2862388,2641145,2363263,2688658,2329784,2972370,2049044,2202225,2041086,2928159,2806063,2748717,2797145,2865040,2899753,2796417,2268179,2354619,2405994,2192599,2367462,2099138,2697598,2431478,2365304,2688395,2120012,2389892,2872689,2581535,2932901,2585451,2598951,2800791,2244106,2997477,2888732,2226420,2684662,2080008,2909047,2668307,2480399,2150318,2750703,2312685,2570320,2439398,2225268,2211626,2767365,2540962,2282763,2709858,2488113,2860402,2356177,2166533,2271966,2123152,2990054,2993001,2840710,2760258,2987380,2892072,2891775,2295398,2523382,2263491,2410295,2457442,2049100,2867670,2246247,2994798,2745481,2507037,2804380,2442297,2016320,2085943,2461602,2572522,2873269,2775358,2127311,2101378,2945772,2837404,2642499,2112605,2776945,2866548,2203580,2234293,2714128,2317462,2242315,2890743,2633712,2961107,2223415,2714653,2928670,2112610,2933644,2611544,2605407,2665235,2401439,2974346,2936946,2125664,2049321,2962619,2979362,2004495,2661840,2114723,2920635,2596617,2928619,2630540,2294864,2748573,2571775,2640891,2366226,2667685,2684732,2725290,2282720,2839679,2113639,2230373,2250765,2466100,2786362,2962704,2226883,2975326,2884849,2445588,2090068,2409200,2512749,2243283,2329912,2116599,2833209,2508557,2936569,2930509,2275575,2679493,2911827,2158076,2303527,2400989,2742123,2697657,2392321,2821855,2117806,2436299,2443343,2439436,2953772,2476231,2875153,2135470,2357167,2068549,2012235,2004660,2698891,2771491,2436513,2647628,2567003,2481234,2643278,2762674,2484690,2539521,2619335,2758508,2055518,2276532,2673581,2012976,2734976,2919804,2905637,2752676,2240570,2050632,2197950,2990479,2680267,2698205,2172001,2517729,2883516,2690140,2382657,2526082,2521039,3350000,3350000,3350000,3350000,3350000,2693304,2774168,2347012,2803737,3350000,2145424,2205133,2720433,2355073,2312120,2570044,2266828,2284783,2163953,2760301,2474632,2789968,2446763,2097086,2024329,2701567,2722034,2295615,2178913,2281421,2293261,2840554,2968033,2384094,2213849,2656032,2580124,2702957,2249707,2526480,2810428,2551984,2418044,2330827,2108224,2992321,2239423,2164754,2632897,2412103,2164486,2985620,2639248,2613106,2493939,2306100,2197222,2222312,2421674,2361952,2939355,2037494,2004994,2934842,2121437,2119792,2958845,2783864,2644489,2512681,2692489,2789674,2660407,2975368,2405078,2424145,2210642,2478441,2048367,2915343,2424394,2592042,2095275,2229303,2851873,2303966,2161447,2716761,2216742,2992492,2636423,2561278,2324533,2270480,2346096,2697636,2463210,2915748,2939187,2343527,2578014,2138347,2941883,2913575,2067830,2736297,2161987,2522989,2494948,2599688,2402334,2604534,2654852,2173943,2687152,2775166,2125730,2866970,2618453,2850466,2674722,2105107,2878299,2661293,2838804,2252767,2339605,2489610,2170480,2147240,2447689,2853337,2739990,2665980,2921198,2865388,2541808,2555449,2963583,2265495,2887222,2399646,2042166,2125193,2055043,2615766,2057909,2638386,2907678,2934594,2003126,2799110,2766148,2682603,2408333,2836916,2631881,2651802,2846510,2826072,2791329,2005424,2282272,2393977,2614710,2252407,2546064,2962342,2900223,2468352,2538915,2592353,2763815,2466841,2950834,2882892,2580842,2404352,2699784,2960496,2804771,2366009,2038655,2403746,2932081,2119919,2519451,2275809,2346956,2397083,2427672,2289004,2360235,2667040,2482425,2643843,2405730,2256574,2550302,2368386,2204340,2656466,2675616,2385351,2986158,2081710,2538398,2074185,2005828,2992801,2679725,2893749,2535779,2850138,2669151,2714205,2401383,2352446,2922613,2684515,2678193,2413613,2695691,2352735,2142648,2466465,2990302,2657849,2860933,2323273,2730048,2978326,2823892,2483983,2596299,2335861,2149174,2689812,2247485,2256125,2843343,2263938,2558397,2381040,2732409,2821558,2120336,2766409,2680676,2895693,2415963,2962337,2422078,2779191,2878876,2335118,2504873,2525809,2178923,2657629,2516081,2393798,2042434,2131734,2711454,2801804,2591089,2128915,2726884,2089651,2598774,2823241,2408606,2450157,2915202,2789095,2810940,2952409,2705189,2595568,2738259,2512348,2658185,2029584,2076968,2610045,2865607,2326737,2562068,2710844,2877773,2311966,2640718,2806258,2267795,2721984,2517061,2339161,2506216,2143535,2689651,2788039,2687575,2215217,2053570,2807565,2461863,2833220,2030597,2120014,2477812,2364102,2163184,2843076,2440630,2945360,2461225,2103017,2999785,2491715,2502813,2672836,2340526,2409119,2410974,2327541,2541001,2276499,2002869,2530202,2837129,2921151,2088591,2385227,2389708,2882307,2024735,2941159,2410250,2371867,2370240,2924784,2048653,2679706,2526118,2220207,2347714,2407908,2528814,2608497,2817708,2047518,2590137,2267487,2888491,2127046,2980990,2859589,2814760,2838878,2457246,2724857,2001649,2613670,2469502,2745934,2448814,2052350,2111051,2470948,2288482,2285382,2835056,2412702,2261994,2202595,2952436,2427586,2017502,2410259,2889605,2875343,2634367,2389088,2990916,2258142,2528804,2646263,2252642,2622063,2320035,2850409,2953682,2511504,2161992,2901784,2301948,2208353,2384773,2610404,2947212,2603268,2446220,2427883,2786691,2532196,2027036,2785387,2163149,2101602,2122140,2808632,2631084,2927116,2267976,2589495,2661080,2318315,2240635,2387288,2175888,2752062]
    x = list(range(0, len(y)))
    yc = np.copy(y)
    yc = yc / 10000000
    # 绘制柱状图
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    fig = plt.figure()
    plt.bar(x, yc, width=1, color='blue',label='数据')
    plt.xlabel('数据项', fontsize=13, fontfamily='SimSun')  # 横轴标签
    plt.ylabel('数值', fontsize=13, fontfamily='SimSun')  # 纵轴标签
    # 绘制折线
    x2 = [0, 500, 1000, 1250, 1500, 2000, 2250, 2500, 3000]
    y2 = np.copy([3000000, 3020000, 3010000, 2980000, 2980000, 2990000, 2980000, 3000000, 3006000])
    y2 = y2 / 10000000
    plt.plot(x2, y2, 'r-',  label='阈值')
    plt.ylim(0.15, 0.4)
    legend_props = {'family': 'SimSun', 'size': 10}
    # 添加图例并设置字体属性
    plt.legend(prop=legend_props)
    # 显示图形
    plt.show()
    from matplotlib.backends.backend_svg import FigureCanvasSVG
    canvas = FigureCanvasSVG(fig)
    # 将绘图输出为SVG格式
    canvas.print_svg('C:\\Users\\helloworld\\Desktop\\svg\\算法1\\动态阈值.svg')


if __name__ == '__main__':
    draw_histogram_line()
