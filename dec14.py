formula = """1 JNDQ, 11 PHNC => 7 LBJSB
1 BFKR => 9 VGJG
11 VLXQL => 5 KSLFD
117 ORE => 6 DMSLX
2 VGJG, 23 MHQGW => 6 HLVR
2 QBJLJ => 6 DBJZ
1 CZDM, 21 ZVPJT, 1 HLVR => 5 VHGQP
1 RVKX => 1 FKMQD
38 PHNC, 10 MHQGW => 5 GMVJX
4 CZDM, 26 ZVHX => 7 QBGQB
5 LBJSB, 2 DFZRS => 4 QBJLJ
4 TJXZM, 11 DWXW, 14 VHGQP => 9 ZBHXN
20 VHGQP => 8 SLXQ
1 VQKM => 9 BDZBN
115 ORE => 4 BFKR
1 VGJG, 1 SCSXF => 5 PHNC
10 NXZXH, 7 ZFXP, 7 ZCBM, 7 MHNLM, 1 BDKZM, 3 VQKM => 5 RMZS
147 ORE => 2 WHRD
16 CQMKW, 8 BNJK => 5 MHNLM
1 HLVR => 5 TJQDC
9 GSLTP, 15 PHNC => 5 SFZTF
2 MJCD, 2 RVKX, 4 TJXZM => 1 MTJSD
1 DBJZ, 3 SLXQ, 1 GMSB => 9 MGXS
1 WZFK => 8 XCMX
1 DFZRS => 9 GSLTP
17 PWGXR => 2 DFZRS
4 BFKR => 7 JNDQ
2 VKHN, 1 SFZTF, 2 PWGXR => 4 JDBS
2 ZVPJT, 1 PHNC => 6 VQKM
18 GMSB, 2 MGXS, 5 CQMKW => 3 XGPXN
4 JWCH => 3 BNJK
1 BFKR => 2 PWGXR
12 PHNC => 2 GMSB
5 XGPXN, 3 VQKM, 4 QBJLJ => 9 GXJBW
4 MHQGW => 9 DWXW
1 GMSB, 1 BFKR => 5 DBKC
1 VLXQL, 10 KSLFD, 3 JWCH, 7 DBKC, 1 MTJSD, 2 WZFK => 9 GMZB
4 JDBS => 8 BRNWZ
2 ZBHXN => 7 HMNRT
4 LBJSB => 7 BCXGX
4 MTJSD, 1 SFZTF => 8 ZCBM
12 BRNWZ, 4 TJXZM, 1 ZBHXN => 7 WZFK
10 HLVR, 5 LBJSB, 1 VKHN => 9 TJXZM
10 BRNWZ, 1 MTJSD => 6 CMKW
7 ZWHT => 7 VKHN
5 CQMKW, 2 DBKC => 6 ZFXP
1 CMKW, 5 JNDQ, 12 FKMQD, 72 BXZP, 28 GMVJX, 15 BDZBN, 8 GMZB, 8 RMZS, 9 QRPQB, 7 ZVHX => 1 FUEL
10 MGXS => 9 JWCH
1 BFKR => 8 SCSXF
4 SFZTF, 13 CZDM => 3 RVKX
1 JDBS, 1 SFZTF => 9 TSWV
2 GMVJX, 1 PHNC => 1 CZDM
6 JDBS => 1 BXZP
9 TSWV, 5 TJXZM => 8 NXZXH
1 HMNRT, 5 TSWV => 4 VLXQL
16 WZFK, 11 XCMX, 1 GXJBW, 16 NXZXH, 1 QBGQB, 1 ZCBM, 10 JWCH => 3 QRPQB
12 SCSXF, 6 VGJG => 4 ZVPJT
10 JNDQ => 3 ZWHT
1 DBJZ, 9 BCXGX => 2 CQMKW
1 WHRD, 14 DMSLX => 8 MHQGW
3 VKHN, 8 TJQDC => 4 MJCD
1 QBJLJ => 4 ZVHX
1 MHQGW, 4 ZVHX => 3 BDKZM"""

import math

class Molecule:
    def __init__(self, ratio):
        self.ratio = ratio
        self.recipe = {}
        self.processed = 0
        self.surplus = 0

    def DFS(self, amount): 
        new = math.ceil((amount - self.surplus)/self.ratio)
        self.processed += new
        self.surplus += self.ratio * new - amount

        for k, v in self.recipe.items():
            if k != None:
                k.DFS(v*new) 

def parse(formula):
    molecules = {"ORE": Molecule(1)}
    lines = formula.split("\n")

    # add products to dict
    for line in lines:
        product = line.split(" => ")[1].split(" ")
        name, ratio = product[1], int(product[0])
        molecules[name] = Molecule(ratio)

    # add the recipe from reactants
    for line in lines:
        product = line.split(" => ")[1].split(" ")[1]
        reactants = line.split(" => ")[0].split(", ")
        for reactant in reactants:
            temp = reactant.split(" ")
            name, ratio = temp[1], int(temp[0])
            molecules[product].recipe[molecules[name]] = ratio

    return molecules

def binSearch(estimate, molecules, target):
    left, right = 1, estimate * 2
    while right - left > 1:
        middle = (left + right) // 2
        ore = getOre(middle, molecules)
        if ore < target:
            left = middle
        else:
            right = middle
    return left

def getOre(amount, molecules):
    molecules["FUEL"].DFS(amount)
    ore = molecules["ORE"].processed

    # reset
    for moluecule in molecules.values():
        moluecule.processed = 0
        moluecule.surplus = 0

    return ore

# part 1
molecules = parse(formula)
one = getOre(1, molecules)
print(one)

# part 2 
target = 1000000000000
estimate = target // one
print(binSearch(estimate, molecules, target))