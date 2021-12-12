list1 = [1452, 11.23, 1+2j, True, "w3resource", (0,-1), [5, 12],{"class":"V", "section":"A"}]
a = len(list1)
i = 1
index = 0
while(i<=a):
    index = i-1
    print("Item", ":", list1[index], "Type of item", ":", type(list1[index]))
    i = i+1