myFruitList = ["apple", "banana", "cherry"]
print(myFruitList[0]+"  "+myFruitList[1])
print(type(myFruitList))

myFruitList.append("kiwi")
print(myFruitList[3])

myFruitList.insert(0,"naranja")
print(myFruitList[0])

myFruitList.remove("banana")
print(myFruitList[1])

myFruitList.pop(2)


print(len(myFruitList))

print("------------------------------------------------")

for value in myFruitList:
    print(value)
    
myFruitList.