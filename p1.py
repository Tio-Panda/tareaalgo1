def perms(coins, max, actualValue, maxCoin, minCoin):
    # OJO, ME eche la wea por algun motivo spaneando weas. revisar si funca
    global coinsPerm
    global nPerms

    if (maxCoin < minCoin):

        if (maxCoin > 0):
            perms(coins, max, 0, maxCoin-1, 0)

        return

    aux = []
    status = True
    auxCoin = minCoin
    actualValue += coins[maxCoin]

    if (actualValue + coins[auxCoin] > max and auxCoin-1 != -1):
        status = False
    else:
        aux.append(coins[maxCoin])

    while (status):

        if (actualValue + coins[auxCoin] > max):
            auxCoin -= 1

        if (auxCoin < 0):
            break

        if ( actualValue + coins[auxCoin] <= max):
            actualValue += coins[auxCoin]
            aux.append(coins[auxCoin])

    if (len(aux) != 0):
        coinsPerm.append(aux)
        nPerms += 1

    perms(coins, max, 0, maxCoin, minCoin+1)

file = open('coins.txt', 'r')

value = int(file.readline())
n = int(file.readline())

coins = []
for line in file:
    coins.append(int(line))

file.close()

# n = 4
# value = 7
# coins = [1,5,3,2]

coins.sort()
coinsPerm = []
nPerms = 0
perms(coins, value, 0, n-1, 0)
# print(coinsPerm)
# print(nPerms)

minor = 0
for i in range(0, nPerms):
    if (len(coinsPerm[minor]) > len(coinsPerm[i])):
        minor = i

# print(coinsPerm[minor])
print(len(coinsPerm[minor]))

