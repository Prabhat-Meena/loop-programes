mydict = {4:'sourabh', 2:'prabhat', 'rahul':'a coder', 'b':[1, 2, 'rohan'], "author": {"harry":"player"}, 1:2}
#print(mydict)
#updateDict = {"rohit":1000, "syam":"friend"}
mydict.update({"rohit":"friend", 1000:"ram"})
print(mydict)

print(mydict.get("rohit2"))
print(mydict["rahit2"])