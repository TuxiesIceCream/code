import array
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
##print(map)
rows = map.splitlines()
#r = len(rows)
#c = len(rows[0]) // 2
#d = '* ' * c
##print(d)
#print("****************************")
for r in rows:
    r = r.replace(' ','')
    ##print(r)
##print(map)
##print("****************************")
##print(rows[0])
##print(len(rows[0]))
cols = (len(rows[0])+1)//2
##print(c)
##print(c*'* ')
##print(map)
for c in range(cols):
    print(rows[c])
##print(map)
