fruits = ["apples","oranges","pineapples"]
for i in range(len(fruits)):
    print(fruits[i])
fruits.append("bananas")
for i in range(len(fruits)):
    print(fruits[i])
fruits.remove(fruits[1])
for i in range(len(fruits)):
    print(fruits[i])