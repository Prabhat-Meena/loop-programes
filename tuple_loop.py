number =  (1, 2, 3, 4, 5, 6, 7, 8, 9)
i = 1
oddCount = 0
evenCount = 0
a = len(number)
ind = 0
while(i<=a):
    ind = a-1
    print(ind)
    if number[ind]%2==0:
        evenCount = evenCount +1
    else:
        oddCount = oddCount+1
    a = a-1
print("Number of even numbers", ":", evenCount)
print("Number of odd numbers" ":", oddCount)