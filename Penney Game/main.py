'''
Input:
4
1
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
2
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
3
HHTTTHHTTTHTHHTHHTTHTTTHHHTHTTHTTHTTTHTH
4
HTHTHHHTHHHTHTHHHHTTTHTTTTTHHTTTTHTHHHHT

Output:
1 0 0 0 0 0 0 0 38
2 38 0 0 0 0 0 0 0
3 4 7 6 4 7 4 5 1
4 6 3 4 5 3 6 5 6

'''

seq = int(input())
data = {}
for i in range(seq):
    n = input()
    s = input()
    data[n]= s

# print(data)
ans = []
# print(data.values())
for k, v in data.items():
    stuff = {"key": int(k), "TTT":0, "TTH":0, "THT":0, "THH":0, "HTT":0, "HTH":0, "HHT":0, "HHH":0}

    for i in range(38):
        stuff[v[i:i+3]] +=1   
    ans.append([x for x in stuff.values()])        

for element in ans:
    for item in element:
        print(item, end=" " )