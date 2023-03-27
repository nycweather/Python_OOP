# Given list and amount get min coin count to get amount

coins = [1,2,5,10,20,50,100,1000]

# O(n^2)
def numCoins(coinList, amount):
    count = 0
    usedCoins = []
    while amount > 0:
        coinList = list(filter(lambda x: x<= amount, coinList))
        count += 1
        amount -= coinList[-1]
        usedCoins.append(coinList[-1])
    print("Count:", count, "\nCoins:", usedCoins)

# O(n)
def numCoins2(coinList, amount):
    usedCoins = []
    # Run as long as we have leftover
    while amount > 0:
        # If the largest coin in list is larger than our amount delete it
        if amount < coinList[-1]:
            coinList.pop()
        # Largest coin is smaller than our amount so we can add it to our list
        else:
            amount -= coinList[-1]
            usedCoins.append(coinList[-1])
    print("Count:", len(usedCoins), "\nCoins:", usedCoins)


numCoins2(coins, 210)
