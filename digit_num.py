i = 1
n = 0
z = 0
d = input("enter:  ")
q = len(d)
while i<=q:
    z = i-1
    if d[z]=="0" or d[z]=="1" or d[z]=="2" or d[z]=="3" or d[z]=="4" or d[z]=="5" or d[z]=="6" or d[z]=="7" or d[z]=="8" or d[z]=="9":
        n = n+1
        print("n",n)
    i = i+1
    print("z",z)
    print("i",i)
print("digit" "=",n)
print("letter","=",q-n)
