import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('Wuerger', 't4iqJstmPhnps98v2ZbK')
data = {"summoners": {"someone": {"y": [3158, 2039, 1688, 1891, 796, 2751, 1413, 1346, 3315, 3264, 2812, 2086, 1120,
                                        4158, 509, 2414, 617, 11425, 1895, 10762, 3174, 3193, 7793, 6972, 11670, 584,
                                        6208, 6358, 5211, 5070, 7469, 13378, 12451, 3662, 2438, 11367, 8851, 2623, 2411,
                                        4414, 3495, 2094, 3024, 3365, 3183, 1254, 4268, 7193, 461, 6245, 6795, 8014,
                                        4955, 1558, 6247, 3807, 4596, 6747, 5090, 7356, 3067, 1820, 2923, 2969, 496,
                                        2751, 1495, 1184, 3547, 2043, 1827, 2180, 1976, 895, 3217, 6733, 7568, 3457,
                                        461, 9828, 1112, 1861, 1935, 1202, 2262, 1954, 1032, 1763, 2470, 1946, 5080,
                                        494, 6557, 952, 3392, 4982, 3867, 4817, 4433, 7386, 3065, 2013, 3243, 2972,
                                        2208, 1197, 4131, 2790, 1095, 3812, 1072, 3744, 6029, 7023, 10817, 10831, 12395,
                                        1934, 1796, 2409, 1980, 2678, 2950, 2692, 1660, 1462, 1874, 2675, 1303, 3713,
                                        3976, 856, 4206, 4253, 7362, 7890, 10114, 2891, 1789, 2119, 2060, 1671, 1998,
                                        3889, 3836, 780, 532, 3100, 2473, 3840, 1600, 3332, 6870, 461, 7467, 7357, 8887,
                                        3046, 1517, 750, 2282, 1687, 1056, 1281, 2488, 847, 3173, 641, 1676, 1731, 1666,
                                        2291, 3911, 7619, 8513, 3249, 5027, 3162, 1788, 1192, 1320, 1305, 1281, 2643,
                                        960, 2991, 1307, 1255, 2625, 1364, 2605, 2010, 1480, 1981, 3707, 792, 3252, 135,
                                        813, 1874, 1827, 3396, 743, 2231, 913, 5667, 3057, 3888, 3338, 6337, 5563, 1072,
                                        5927, 14072, 13748, 12502, 6298, 611, 1729, 1691, 2478, 2777, 2578, 2750, 578,
                                        1242, 2305, 3211, 4643, 4721, 3933, 1414, 2648, 13096, 2041, 6082, 4250, 4419,
                                        12339, 11440, 11855, 461, 10502, 2724, 11598, 11669, 461, 11821, 13238, 13736,
                                        10324, 10999, 3371, 4128, 8433, 9346, 10320, 611, 1791, 2875, 3368, 2801, 1912,
                                        1616, 1604, 1493, 860, 892, 1474, 912, 1497, 1150, 2732, 1652, 1759, 6586, 461,
                                        3294, 5323, 7280, 7604, 2424, 7485, 1617, 2518, 7862, 6408, 6459, 12473, 6326,
                                        2383, 5625, 3873, 6521, 8251, 3878, 461, 2369, 1895, 3106, 2490, 3229, 770,
                                        3305, 3350, 696, 3881, 1152, 606, 2368, 1634, 3830, 6321, 649, 2105, 5104, 6282,
                                        135, 1509, 11291, 12294, 2828, 11342, 12548, 6150, 12992, 11977, 12085, 10719,
                                        10312, 5546, 13004, 11899, 12366, 13735, 461, 11734, 2303, 1910, 2168, 3495,
                                        870, 1561, 1713, 2265, 2636, 3272, 1488, 2334, 1540, 3694, 1330, 6800, 8120,
                                        6310, 5441, 3502, 1836, 1922, 2728, 2098, 1303, 1306, 2784, 1253, 880, 1165,
                                        1789, 942, 2241, 3001, 1685, 1895, 1833, 4841, 3783, 3239, 611, 7093, 6751,
                                        6905, 7382, 4903, 7461, 6416, 7796, 6902, 6641, 7009, 6424, 7482, 10025, 7491,
                                        8029, 5046, 8828, 8945, 675, 1894, 1758, 1590, 3172, 1657, 4330, 1846, 2389,
                                        1716, 3869, 1190, 2475, 7507, 12168, 4508, 1323, 4027, 1068, 4589, 953, 1956,
                                        2482, 933, 2287, 2653, 3916, 767, 1776, 4956, 2450, 2742, 1525, 7146, 1284,
                                        1250, 1751, 2860, 7756, 12368, 761, 1845, 1416, 1378, 1256, 1800, 873, 4027,
                                        2289, 1268, 2571, 5722, 701, 1794, 9030, 8673, 2761, 4660, 4385, 5456, 285,
                                        11518, 11086, 11414, 10729, 11713, 10892, 11028, 11941, 10844, 12054, 8852,
                                        12371, 12552, 10344, 12609, 11322, 8037, 12369, 10840, 3169, 5342, 7759, 12334,
                                        7834, 2491, 7403, 461, 2696, 7797, 11669, 461, 4277, 1777, 5944, 12035, 2408,
                                        9135, 3211, 2667, 1172, 1791, 3199, 2651, 1310, 1639, 2682, 1133, 2636, 1598,
                                        2001, 924, 1985, 1115, 4017, 4784, 672, 7241, 5456, 796, 3527, 5530, 6725, 8641,
                                        12865, 5975, 3546, 5213, 10060, 13654, 461, 3506, 5768, 7758, 2658, 5502, 6567,
                                        11498, 5594, 6817, 3475, 2102, 2195, 1240, 3825, 1867, 1792, 1307, 705, 3115,
                                        729, 1813, 1499, 1537, 5044, 3519, 9458, 1138, 10038, 9652, 3109, 1859, 1421,
                                        2180, 1374, 1368, 1718, 461, 1530, 1808, 1460, 1712, 3245, 858, 1256, 611, 1930,
                                        2804, 2566, 1409, 2332, 2267, 1781, 3853, 6334, 2528, 3330, 3303, 1179, 4753,
                                        5904, 3538, 5957, 6786, 5598, 6392, 6612, 6887, 6628, 6874, 4190, 3123, 6599,
                                        6899, 6221, 7588, 7703, 6060, 6615, 6596, 8217, 4119, 6727, 9430, 5177, 3122,
                                        5549, 8995, 461, 3886, 2381, 4742, 2589, 9875, 713, 8459, 1115, 6158, 7988,
                                        8119, 1470, 550, 1588, 7222, 7712, 3383, 1672, 2147, 2057, 3215, 2280, 1742,
                                        2233, 1426, 3375, 1697, 2668, 3354, 2536, 2709, 3539, 2927, 1595, 1890, 11674,
                                        4126, 6359, 6419, 6410, 6266, 5350, 7016, 8279, 6678, 7216, 461, 6636, 461,
                                        3430, 1404, 7716, 7142, 10128, 6038, 8282, 672, 3476, 1382, 1659, 3009, 1115,
                                        2710, 861, 1022, 2297, 573, 1412, 6004, 3080, 7347, 2664, 461, 4143, 808, 1392,
                                        2174, 1370, 1129, 2389, 2493, 516, 988, 878, 1265, 2448, 1147, 1400, 1310, 1308,
                                        1064, 857, 1696, 1132, 1762, 1919, 5686, 11858, 11487, 12035, 5248, 6991, 6431,
                                        6513, 6030, 5294, 6795, 6733, 1892, 1868, 1343, 583, 3326, 5723, 9030, 7652,
                                        3042, 1796, 2107, 2213, 621, 2436, 1817, 1750, 1067, 1909, 1740, 4601, 1937,
                                        792, 3702, 6886, 461, 7804, 5841, 8138, 1490, 1839, 2388, 1222, 1990, 2657, 695,
                                        3690, 2334, 1377, 1418, 1523, 1932, 5977, 326, 9730, 12072, 12161, 9878, 11870,
                                        11455, 11201, 12069, 11502, 9452, 11710, 11819, 11709, 4921, 8233, 9399, 7756,
                                        8256, 6451, 7770, 1170, 6923, 7050, 4992, 3180, 3941, 6342, 2650, 2163, 7506,
                                        6577, 6126, 1444, 3972, 8798, 6316, 6208, 4822, 1645, 4790, 3129, 1971, 1163,
                                        3533, 1797, 461, 2185, 2913, 843, 3767, 686, 1893, 2038, 8669, 7775, 1587, 5252,
                                        7622, 8626, 461, 10073, 12226, 12621, 2571, 11900, 13374, 12617, 3436, 2970,
                                        12347, 10580, 11048, 10773, 13696, 461, 12428, 11390, 12034, 2424, 5734, 9178,
                                        12305, 11059, 10918, 11156, 12003, 12713, 11158, 1432, 13651, 13404, 2771, 4461,
                                        12416, 13260, 7411, 11023, 7450, 11098, 10638, 2515, 2167, 687, 1835, 1762,
                                        1872, 560, 8083, 3150, 1627, 1341, 1729, 925, 2023, 3747, 1811, 2344, 1611,
                                        7168, 7352, 10727, 12423, 10767, 10286, 11801, 12531, 11221, 1525, 11509, 13072,
                                        11615, 13246, 12979, 12662, 11678, 10754, 4440, 10912, 11423, 8570, 757, 2084,
                                        1194, 1214, 1027, 591, 1234, 1253, 1870, 6741, 1167, 2246, 1226, 2991, 2138,
                                        2466, 2980, 8720, 4826, 6815, 3090, 1720, 1469, 1385, 2163, 754, 2035, 461,
                                        1505, 1816, 461, 7195, 1771, 9493, 8148, 4162, 8597, 3933, 9814, 2806, 611, 930,
                                        1288, 1182, 1736, 2303, 2108, 2046, 2554, 1649, 986, 5242, 2769, 1761, 4534,
                                        5705, 9672, 10449, 7610, 6735, 288, 2656, 1358, 1714, 1834, 906, 461, 2466, 990,
                                        1419, 1241, 8188, 5914, 8483, 2459, 6649, 4951, 5538, 8122, 5302, 5184, 6617,
                                        6852, 4538, 1699, 6190, 5970, 6125, 7589, 7210, 6587, 1837, 6164, 6485, 1181,
                                        6635, 5428, 5560, 2634, 2680, 2467, 2637, 1585, 1390, 2125, 3151, 1484, 2618,
                                        1676, 912, 2294, 3680, 1428, 6870, 6030, 9236, 7064, 5337, 6428, 6971, 675,
                                        1180, 1157, 1688, 1550, 1191, 2989, 820, 1356, 1631, 894, 1800, 9913, 3106, 845,
                                        898, 8339, 1069, 8972, 5141, 611, 1811, 2311, 2305, 1358, 2490, 2282, 2027,
                                        2157, 1602, 1854, 2780, 2464, 715, 5097, 1511, 797, 461, 1503, 4995, 3106, 3197,
                                        1120, 1373, 1909, 1163, 6511, 1368, 1803, 2071, 1107, 2376, 461, 1914, 8769,
                                        6865, 6280, 4581, 1286, 1340, 6188, 1920, 1663, 1326, 2404, 1805, 1584, 643,
                                        1696, 1656, 3543, 906, 1456, 3773, 732, 461, 1741, 2466, 4946, 4432, 1219, 2127,
                                        1839, 1271, 1121, 1160, 2046, 1206, 2822, 1495, 3305, 819, 2184, 902, 996, 1325,
                                        1956, 4954, 3206, 6556, 285, 578, 1664, 3264, 1008, 2981, 1392, 1915, 2628,
                                        4557, 3147, 5269, 4580, 461, 3062, 3621, 9453, 5400, 3103, 7751],
                                  "x": [7058, 12000, 12254, 12636, 10030, 12777, 9974, 10721, 13525, 11612, 12798,
                                        13180, 8672, 14072, 859, 12182, 684, 5133, 2057, 10850, 7078, 7378, 3534, 6404,
                                        2684, 2016, 11175, 10057, 5055, 6970, 3159, 4370, 2259, 7667, 9038, 1406, 3601,
                                        2192, 7818, 8615, 7872, 11987, 13191, 13534, 13480, 8378, 13743, 13294, 394,
                                        9654, 6614, 8597, 8635, 11172, 13312, 13508, 10110, 6211, 6117, 7766, 7103,
                                        12429, 13551, 13425, 739, 13433, 12634, 7424, 13379, 12327, 11514, 13291, 12058,
                                        2900, 12501, 6187, 5972, 13245, 394, 7052, 1615, 11793, 12930, 11670, 13184,
                                        13068, 11352, 12745, 12544, 11153, 12662, 1066, 7862, 4400, 13640, 6888, 4274,
                                        10139, 4607, 8342, 6941, 11117, 12964, 13416, 12065, 7231, 13187, 13557, 10920,
                                        13264, 8725, 13279, 13566, 11580, 13418, 10783, 13213, 10726, 12399, 13249,
                                        12935, 13298, 12772, 13301, 10792, 11810, 11756, 13217, 11047, 11669, 13292,
                                        4376, 9676, 9784, 9817, 7623, 10206, 10279, 11943, 12185, 12335, 10313, 11767,
                                        13905, 13780, 4509, 1030, 12599, 13410, 13758, 4990, 12809, 14097, 394, 8173,
                                        9514, 8599, 7018, 11339, 3528, 13028, 12776, 11006, 12191, 10647, 5137, 13770,
                                        2363, 12336, 11135, 9870, 13218, 9096, 2685, 4854, 10733, 1642, 7315, 11850,
                                        11302, 10982, 11117, 11436, 13329, 10670, 13596, 11038, 11570, 12811, 11443,
                                        12368, 11680, 12250, 12539, 11764, 4089, 10131, 362, 2548, 12074, 12810, 13614,
                                        3433, 13239, 6959, 10081, 13614, 11296, 10848, 7386, 11665, 10168, 6001, 8509,
                                        6402, 2996, 9931, 603, 11881, 12742, 13445, 13566, 13132, 13510, 1549, 12332,
                                        13249, 12307, 10562, 10321, 13633, 10586, 3027, 2927, 3829, 6501, 10058, 770,
                                        2221, 1500, 1984, 394, 1350, 669, 1628, 1507, 394, 1982, 3500, 4061, 1346, 5671,
                                        10738, 806, 4972, 4059, 1402, 603, 12183, 13463, 13593, 13442, 12013, 11598,
                                        11088, 11825, 10491, 3485, 11084, 10695, 12458, 6403, 10587, 7731, 10681, 3581,
                                        394, 7237, 6981, 3720, 2112, 8430, 8557, 4268, 8414, 3638, 5654, 6446, 1312,
                                        6664, 8548, 5637, 4007, 3619, 8861, 7600, 394, 7890, 11428, 13698, 13400, 13586,
                                        3997, 13655, 13705, 2985, 13588, 11394, 1222, 11939, 7157, 9274, 6503, 723,
                                        8233, 5962, 6532, 362, 778, 1412, 1823, 810, 1688, 2131, 7211, 2756, 1802, 1465,
                                        1561, 1302, 1164, 3510, 1957, 2994, 4103, 394, 1770, 6275, 11986, 13105, 12945,
                                        3595, 11064, 12609, 12630, 13256, 13457, 11237, 12358, 11998, 13613, 7489, 6684,
                                        8334, 7387, 8034, 13019, 3390, 11714, 13361, 13106, 10749, 11600, 13505, 11558,
                                        1418, 10619, 12770, 5940, 12305, 12993, 11267, 12782, 12468, 5353, 4282, 7181,
                                        603, 7537, 7169, 6477, 7801, 5339, 7643, 6682, 7800, 6811, 6370, 6821, 6339,
                                        7837, 1374, 2164, 8443, 10182, 9385, 4785, 298, 11444, 12040, 11529, 13339,
                                        11921, 14012, 12268, 13319, 12186, 13755, 7870, 2991, 8218, 2332, 4619, 10878,
                                        11008, 1345, 4917, 10731, 11174, 12312, 9850, 13142, 12245, 13922, 4986, 11902,
                                        12333, 5093, 12530, 10304, 6887, 9354, 8040, 12744, 4589, 3190, 1717, 7813,
                                        11665, 11177, 12119, 10902, 12805, 10513, 11001, 12149, 10154, 12850, 5938,
                                        1583, 12998, 1276, 2397, 13451, 5087, 4511, 5274, 662, 1698, 1760, 1580, 1269,
                                        1505, 1310, 1564, 2007, 1279, 2444, 3632, 2008, 2318, 3682, 2349, 1641, 3575,
                                        2222, 1639, 7153, 6880, 3826, 1456, 3325, 8422, 7531, 394, 8404, 3748, 4109,
                                        394, 7051, 10812, 4515, 1946, 11914, 4597, 3473, 13072, 10754, 12313, 13657,
                                        12304, 11606, 11535, 13038, 10907, 13230, 12152, 12940, 5986, 10713, 6864, 4489,
                                        3786, 3325, 2858, 5835, 7290, 5690, 7067, 3466, 5915, 1651, 8475, 8230, 4886,
                                        1738, 3785, 394, 9616, 8391, 3316, 8394, 10875, 3613, 5182, 11305, 11324, 8284,
                                        12765, 12183, 10552, 13675, 12595, 12588, 11916, 2954, 13545, 2584, 12710,
                                        12608, 9961, 8264, 3811, 9130, 1645, 1758, 3914, 7065, 11495, 12396, 13287,
                                        12296, 12300, 12718, 394, 12731, 12789, 8900, 12881, 12758, 10772, 8144, 603,
                                        11408, 13637, 13431, 11022, 12768, 11971, 12805, 13485, 9553, 4391, 12816,
                                        12302, 10242, 13375, 6329, 5427, 5571, 7806, 6017, 6065, 6081, 6549, 6282,
                                        7500, 4306, 13487, 6091, 6467, 6158, 8285, 8344, 5741, 6757, 6689, 7936, 774,
                                        6000, 9634, 4798, 7083, 5324, 5121, 394, 11154, 2611, 6698, 8411, 864, 1424,
                                        2578, 6016, 6383, 3548, 6439, 5032, 1266, 9295, 3915, 8382, 7947, 11839, 12934,
                                        12995, 13208, 12369, 12360, 13096, 10543, 11913, 12648, 12776, 11670, 12287,
                                        13217, 13600, 13421, 11598, 12666, 5024, 3820, 6329, 6893, 6660, 6051, 9658,
                                        6839, 8877, 6197, 6525, 394, 6936, 394, 13173, 11195, 7761, 8254, 4969, 13956,
                                        13492, 943, 8420, 11968, 8881, 13218, 7056, 13495, 10529, 7447, 10929, 1191,
                                        12164, 5086, 3603, 5691, 12201, 394, 13672, 2812, 9281, 9379, 11805, 11239,
                                        12913, 13467, 590, 11283, 10606, 11856, 10696, 10724, 11575, 8072, 11708,
                                        11007, 2904, 12644, 10937, 8185, 8177, 851, 1996, 1659, 1954, 5183, 7202, 6106,
                                        6850, 8413, 4934, 6445, 6682, 11291, 12895, 1763, 1007, 13357, 5723, 9219, 8207,
                                        7054, 11120, 12529, 13002, 2340, 12726, 11786, 12114, 10878, 11297, 11921, 8578,
                                        9344, 3158, 13930, 13214, 394, 13712, 9981, 8557, 3361, 12760, 12757, 11195,
                                        12121, 12541, 2682, 11788, 11908, 7863, 10957, 10270, 7903, 5964, 577, 1100,
                                        2063, 1838, 1167, 1525, 1582, 1484, 1814, 1789, 2238, 1516, 1608, 1336, 974,
                                        3560, 1120, 2063, 8243, 3663, 1044, 1564, 7167, 6363, 6158, 2894, 8779, 6015,
                                        2883, 12035, 5321, 6277, 6302, 5371, 4973, 3657, 1461, 6008, 8916, 2231, 7945,
                                        7092, 11147, 11386, 13013, 12010, 394, 11967, 10576, 3504, 13534, 3397, 12791,
                                        2659, 9272, 8479, 2157, 8341, 6610, 8360, 394, 1097, 2280, 2356, 615, 1523,
                                        2364, 2360, 13530, 846, 2866, 1229, 1623, 1342, 4233, 394, 2218, 1900, 2370,
                                        12865, 5721, 3158, 2316, 1585, 1419, 1586, 2099, 2587, 1212, 566, 4204, 3667,
                                        12956, 796, 6313, 6485, 8292, 11181, 12477, 12814, 11143, 7680, 11620, 2862,
                                        11664, 12245, 12139, 959, 11652, 13690, 10142, 10379, 11015, 10195, 11856,
                                        13207, 11650, 12041, 12456, 12080, 6899, 1102, 1829, 1230, 1694, 1761, 2051,
                                        1370, 748, 1719, 3238, 1747, 3838, 3179, 2361, 1675, 3664, 1033, 1224, 1559,
                                        8345, 2518, 11756, 11612, 11764, 9730, 979, 11825, 11360, 12337, 8663, 11328,
                                        13038, 10495, 12695, 11742, 13195, 10493, 9224, 4011, 9968, 7107, 11537, 11287,
                                        11216, 12795, 4066, 12083, 394, 11108, 11214, 394, 7565, 10434, 9570, 8803,
                                        9946, 9249, 4190, 10346, 2737, 603, 4472, 12232, 11154, 11132, 13251, 12101,
                                        11083, 13006, 12860, 4240, 11297, 13501, 12362, 11437, 13397, 9286, 10921, 8408,
                                        6676, 727, 13382, 11066, 12471, 12812, 10122, 394, 12561, 6987, 12509, 6094,
                                        8994, 9401, 8364, 7747, 8813, 5638, 5762, 7742, 6261, 4773, 7203, 6725, 4677,
                                        12902, 5299, 13980, 8469, 7891, 6903, 6568, 2443, 5780, 6522, 11174, 6351, 5905,
                                        5214, 13070, 3254, 6390, 10475, 11370, 10524, 12746, 12766, 11168, 13471, 10076,
                                        4590, 10511, 7829, 10569, 6445, 5769, 1290, 1756, 4985, 8281, 3268, 298, 7241,
                                        11143, 11414, 10930, 10812, 13512, 4407, 10898, 12099, 10588, 12373, 11396,
                                        13514, 5799, 4134, 8707, 9699, 10033, 7963, 603, 12077, 12893, 12925, 11171,
                                        12092, 12680, 10954, 12317, 10999, 11673, 13051, 9722, 3332, 7697, 9270, 7905,
                                        394, 9022, 5565, 7095, 11294, 11379, 12319, 10834, 11296, 8442, 11496, 12803,
                                        12449, 5736, 10608, 394, 11243, 9872, 6275, 6774, 8595, 5844, 5503, 9755, 11968,
                                        12066, 11250, 13280, 12844, 12140, 2256, 11177, 10210, 13685, 3883, 11307,
                                        13899, 2605, 394, 12541, 10836, 4952, 7079, 10141, 12250, 12456, 10755, 11008,
                                        11374, 11983, 11182, 13003, 12501, 13673, 7881, 12510, 7847, 4554, 6926, 11801,
                                        5661, 3526, 6663, 662, 1564, 11204, 12374, 4688, 13443, 8885, 12310, 12372,
                                        13715, 13450, 10038, 10624, 394, 12717, 9442, 6936, 5609, 5021, 6899]}},
        "mode": "classic"}
mode_to_map = {"classic": 11, "aram": 12, "3v3": 10, "dominion": 8, "ascension": 8}
maps_info = {"8": {'bbox': {'x0': 0, 'y0': 0, 'x1': 13987, 'y1': 13987}, 'image_size': {'x': 512, 'y': 512}},
             "10": {'bbox': {'x0': 0, 'y0': 0, 'x1': 15398, 'y1': 15398}, 'image_size': {'x': 512, 'y': 512}},
             "11": {'bbox': {'x0': -120, 'y0': -120, 'x1': 14870, 'y1': 14980}, 'image_size': {'x': 512, 'y': 512}},
             "12": {'bbox': {'x0': -28, 'y0': -19, 'x1': 12849, 'y1': 12858}, 'image_size': {'x': 752, 'y': 752}}}


def create_map_graph(name, map_id, data):
    map_info = maps_info[map_id]
    map_url = "http://ddragon.leagueoflegends.com/cdn/6.8.1/img/map/map" + map_id + ".png"
    top_margin = 50
    trace_dots = {'x': data['x'], 'y': data['y'], 'mode': 'markers', 'name': 'points',
                  'marker': {'color': 'black', 'opacity': 0.5, 'size': 2}, 'type': 'scatter'}
    trace_density = {'x': data['x'], 'y': data['y'], 'name': 'density', 'ncontours': 20, 'nbinsx': 50, 'nbinsy': 50,
                     'colorscale': [[0, 'rgba(255,255,255,0)'], [0.2, 'rgb(255,255,0)'], [0.5, 'rgb(255,128,0)'],
                                    [1, 'rgb(255,0,0)']], 'opacity': 0.8, 'showscale': False,
                     'type': 'histogram2dcontour',
                     'histnorm': 'probability density', 'contours': {'coloring': 'heatmap'}, 'line': {'width': 0}}
    layout = {'title': name, 'width': map_info['image_size']['x'], 'height': map_info['image_size']['y'] + top_margin,
              'margin': {'b': 0, 'l': 0, 'r': 0, 't': top_margin}, 'autosize': False, 'showlegend': False,
              'images': [{'source': map_url, 'x': 0, 'y': 1, 'sizex': 1, 'sizey': 1, 'sizing': "stretch",
                          'opacity': 0.5, 'layer': "below"}],
              'xaxis': {'range': [map_info['bbox']['x0'], map_info['bbox']['x1']], 'showticklabels': False,
                        'showgrid': False, 'zeroline': False, 'ticks': ""},
              'yaxis': {'range': [map_info['bbox']['y0'], map_info['bbox']['y1']], 'showticklabels': False,
                        'showgrid': False, 'zeroline': False, 'ticks': ""}}
    fig = go.Figure(data=[trace_dots, trace_density], layout=layout)
    py.plot(fig)


def update_graphs(data):
    map_id = mode_to_map[data['mode']]
    for name in data['summoners']:
        create_map_graph(name, str(map_id), data['summoners'][name])


update_graphs(data)