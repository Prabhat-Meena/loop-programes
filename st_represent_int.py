i = 0
count = 0
x = 1
st =input("Enter: ")
a = len(st)
while x<=a:
    if st[i]=="0" or st[i]=="1" or st[i]=="2" or st[i]=="3" or st[i]=="4" or st[i]=="5" or st[i]=="6" or st[i]=="7" or st[i]=="8" or st[i]=="9":
        count = count+1
    i = x-1
    x = x+1
if count==a:
    print("str represent int")
else:
    print("str not represent int")