class Grid:
    #grid = {}
    def __init__(self,map):
        self.grid = {}
        self.rows = map.splitlines()
        self.row = len(self.rows)
        for r in range(self.row):
            self.rows[r] = self.rows[r].replace(' ','')
            #print()
        self.col = len(self.rows[0])
        for r in range(self.row):
            for c in range(self.col):
                self.grid[(r,c)] = self.rows[r][c]


                
        
map = """
? ? ? ? 0 0 0
? ? ? ? 0 ? ?
? ? ? 0 0 ? ?
? ? ? 0 0 ? ?
0 ? ? ? 0 0 0
0 ? ? ? 0 0 0
0 ? ? ? 0 ? ?
0 0 0 0 0 ? ?
0 0 0 0 0 ? ?
""".strip()
g = Grid(map)
s=''
for r in range(9):
    for c in range(7):
        s += g.grid[(r,c)]
    print(s)
    s=''
