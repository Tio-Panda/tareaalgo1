file = open('coins.txt', 'r')

value = int(file.readline())
m = int(file.readline())

coins = []
for line in file:
    coins.append(int(line))

print(coins)
