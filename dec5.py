def build(directions):
    coord = (0, 0)
    wire = set()

    for direction in directions:
        dist = int(direction[1:])

        if direction[0] == 'R':
            for x in range(1,dist+1):
                wire.add((coord[0]+x, coord[1]))
            coord = (coord[0]+dist, coord[1])

        elif direction[0] == 'L':
            for x in range(1,dist+1):
                wire.add((coord[0]-x, coord[1]))
            coord = (coord[0]-dist, coord[1])

        elif direction[0] == 'U':
            for y in range(1,dist+1):
                wire.add((coord[0], coord[1]+y))
            coord = (coord[0], coord[1]+dist)

        elif direction[0] == 'D':
            for y in range(1,dist+1):
                wire.add((coord[0], coord[1]-y))
            coord = (coord[0], coord[1]-dist)

    return wire

def getDist(directions, intersect):

    coord = (0, 0)
    counter = 0
    counters = {}
    for direction in directions:
        dist = int(direction[1:])

        if direction[0] == 'R':
            for x in range(1,dist+1):
                coord = (coord[0]+1, coord[1])
                counter += 1
                if coord in intersect:
                    counters[coord] = counter

        elif direction[0] == 'L':
            for x in range(1,dist+1):
                coord = (coord[0]-1, coord[1])
                counter += 1
                if coord in intersect:
                    counters[coord] = counter

        elif direction[0] == 'U':
            for x in range(1,dist+1):
                coord = (coord[0], coord[1]+1)
                counter += 1
                if coord in intersect:
                    counters[coord] = counter

        elif direction[0] == 'D':
            for x in range(1,dist+1):
                coord = (coord[0], coord[1]-1)
                counter += 1
                if coord in intersect:
                    counters[coord] = counter

    return counters

if __name__== "__main__":
    directions1 = "R995,D882,R144,U180,L638,U282,L907,D326,R731,D117,R323,U529,R330,U252,R73,U173,R345,U552,R230,U682,R861,U640,L930,U590,L851,D249,R669,D878,R951,D545,L690,U392,R609,D841,R273,D465,R546,U858,L518,U567,L474,D249,L463,D390,L443,U392,L196,U418,R433,U651,R520,D450,R763,U714,R495,D716,L219,D289,L451,D594,R874,U451,R406,U662,R261,D242,R821,D951,R808,D862,L871,U133,R841,D465,R710,U300,R879,D497,R85,U173,R941,U953,R705,U972,R260,D315,L632,U182,L26,D586,R438,U275,L588,U956,L550,D576,R738,U974,R648,D880,R595,D510,L789,U455,R627,U709,R7,D486,L184,U999,L404,U329,L852,D154,L232,U398,L587,U881,R938,D40,L657,D164,R45,D917,R106,U698,L824,D426,R879,U700,R847,D891,L948,U625,R663,D814,R217,U30,R610,D781,L415,D435,L904,U815,R152,U587,R287,U141,R866,D636,L290,D114,L751,D660,R6,U383,L263,U799,R330,U96,L6,U542,L449,D361,R486,U278,L990,U329,L519,U605,R501,D559,R916,U198,L499,D174,R513,U396,L473,D565,R337,D770,R211,D10,L591,D920,R367,D748,L330,U249,L307,D645,R661,U266,R234,D403,L513,U443,L989,D1,L674,D210,L537,D872,L607,D961,R894,U632,L195,U744,L426,U531,R337,D821,R113,U436,L700,U779,R555,U891,R268,D30,R958,U411,R904,U24,R760,D958,R231,U229,L561,D134,L382,D961,L237,U676,L223,U324,R663,D186,R833,U188,R419,D349,L721,U152,L912,U490,R10,D995,L98,U47,R140,D815,R826,U730,R808,U256,R479,D322,L504,D891,L413,D848,L732,U375,L307,U7,R682,U270,L495,D248,R691,D945,L70,U220,R635,D159,R269,D15,L161,U214,R814,D3,R354,D632,R469,D36,R85,U215,L243,D183,R140,U179,R812,U180,L905,U136,L34,D937,L875"
    directions2 = "L999,D22,L292,U843,R390,U678,R688,D492,L489,U488,R305,U951,L636,U725,R402,U84,L676,U171,L874,D201,R64,D743,R372,U519,R221,U986,L393,D793,R72,D184,L553,D137,L187,U487,L757,U880,L535,U887,R481,U236,L382,D195,L388,D90,R125,U414,R512,D382,R972,U935,L172,D1,R957,U593,L151,D158,R396,D42,L30,D178,R947,U977,R67,D406,R744,D64,L677,U23,R792,U864,R259,U315,R314,U17,L37,D658,L642,U135,R624,U601,L417,D949,R203,D122,R76,D493,L569,U274,L330,U933,R815,D30,L630,D43,R86,U926,L661,D491,L541,D96,R868,D565,R664,D935,L336,D152,R63,U110,L782,U14,R172,D945,L732,D870,R404,U767,L907,D558,R748,U591,R461,D153,L635,D457,R241,U478,L237,U218,R393,U468,L182,D745,L388,D360,L222,D642,L151,U560,R437,D326,R852,U525,R717,U929,L470,U621,R421,U408,L540,D176,L69,U753,L200,U251,R742,U628,R534,U542,R85,D71,R283,U905,L418,D755,L593,U335,L114,D684,L576,D645,R652,D49,R86,D991,L838,D309,L73,U847,L418,U675,R991,U463,R314,D618,L433,U173,R869,D115,L18,U233,R541,U516,L570,U340,R264,D442,L259,U276,R433,D348,R524,D353,R336,D883,R580,U157,R79,D27,L134,D161,L748,D278,R322,D581,R654,D156,L930,D293,L156,U311,R807,D618,R408,U719,R366,D632,R307,D565,R478,D620,R988,D821,R365,D581,L946,D138,L943,U69,R620,U208,L407,U188,L122,U353,L751,U565,R849,D874,R668,D794,L140,D474,R289,D773,R344,D220,L55,D385,L394,U208,R305,U736,L896,D376,R331,D855,L466,U516,L741,U124,L825,U467,L525,D911,R76,U220,L610,U102,L261,D891,L585,U397,L152,U753,R822,D252,R106,U145,L7,U524,R343,U352,L357,D399,L446,D140,L723,U46,R687,D409,R884"

    dir1 = directions1.split(",")
    dir2 = directions2.split(",")

    wire1 = build(dir1)
    wire2 = build(dir2)
    intersect = wire1.intersection(wire2)


    distances = [abs(x)+abs(y) for x, y in list(intersect)]
    closest = min(distances)
    print(f"part1: {closest}")

    wire1Dist = getDist(dir1, intersect)
    wire2Dist = getDist(dir2, intersect)

    total = [value + wire2Dist[key] for key, value in wire1Dist.items()]
    print(f"part2: {min(total)}")